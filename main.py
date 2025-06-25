
import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


# Step 1: Load documents
folder_path = "documents"
all_docs = []
for file in os.listdir(folder_path):
    if file.endswith(".txt"):
        loader = TextLoader(os.path.join(folder_path, file))
        docs = loader.load()
        for doc in docs:
            doc.metadata["source"] = file
        all_docs.extend(docs)

# Step 2: Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(all_docs)

# Step 3: Use sentence-transformers model directly
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}  # use "cuda" if you have GPU
)

# Step 4: Create/load Chroma DB
persist_dir = "chroma_db"
if not os.path.exists(persist_dir):
    vectorstore = Chroma.from_documents(
        chunks, embedding=embedding, persist_directory=persist_dir
    )
    vectorstore.persist()
else:
    vectorstore = Chroma(
        persist_directory=persist_dir, embedding_function=embedding
    )

# Step 5: User query loop
retriever = vectorstore.as_retriever()

while True:
    query = input("\n🔍 Ask something (or 'exit'): ")
    if query.lower() in ["exit", "quit"]:
        print("👋 Bye!")
        break

    results = retriever.get_relevant_documents(query)
    if not results:
        print("❗ No match found.")
        continue

    print("\n🧠 Top 3 Matches:\n")
    for i, doc in enumerate(results[:3], 1):
        print(f"[{i}] {doc.page_content.strip()}\n")

    print("📄 Source Files:")
    for doc in results[:3]:
        print("-", doc.metadata.get("source", "unknown"))
