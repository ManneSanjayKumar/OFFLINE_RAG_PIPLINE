import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

#  Step 1: Load all text files from documents/
folder_path = "documents"
docs = []
for file in os.listdir(folder_path):
    if file.endswith(".txt"):
        loader = TextLoader(os.path.join(folder_path, file))
        docs.extend(loader.load())

# Step 2: Split documents into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

#  Step 3: Load local sentence-transformer embeddings
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

#  Step 4: Create Chroma vector database
vectorstore = Chroma.from_documents(chunks, embedding_model)

#  Step 5: Input user query
query = input("🔎 Ask your question: ")

#  Step 6: Retrieve relevant chunks using vector similarity
retriever = vectorstore.as_retriever()
docs = retriever.get_relevant_documents(query)

#  Step 7: Display top 3 relevant chunks
print("\n🧠 Top Results from Documents:\n")
for i, doc in enumerate(docs[:3], 1):
    print(f"[{i}] {doc.page_content.strip()}\n")

#  Step 8: Show source files
print("\n📄 Source Files:")
for doc in docs[:3]:
    print("-", doc.metadata["source"])
