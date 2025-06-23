🧠 Local Document Question Answering with LangChain & Chroma

This project is a simple yet powerful **local question-answering system** that allows you to query your own `.txt` files using semantic search powered by **LangChain**, **Hugging Face embeddings**, and **Chroma vector storage**.



📂 Project Structure
Great! Here's everything you asked for — a **complete GitHub-ready setup** including:

1. ✅ `README.md`
2. ✅ `requirements.txt`
3. ✅ Sample `.txt` document
4. ✅ Sample user query
5. ✅ Optional: instructions for turning it into a **Streamlit web app**

---

## 📁 Final Folder Structure


LangChain_QA_Project/
│
├── app.py
├── README.md
├── requirements.txt
├── documents/
│   └── sample.txt
```



## 📄 1. `README.md` 

Here's the updated README including demo query and streamlit extension idea:


```markdown
# 🧠 Local Document Question Answering with LangChain & Chroma

This project lets you **ask questions** from your own `.txt` documents using **semantic search**. It's powered by **LangChain**, **Hugging Face sentence embeddings**, and **Chroma** as a local vector database.


## 📂 Project Structure

```

LangChain\_QA\_Project/
├── app.py                # Main Python script
├── documents/            # Your .txt files go here
│   └── sample.txt
├── requirements.txt      # Python dependencies
└── README.md             # Project guide (this file)


🛠️ Setup Instructions
✅ Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/LangChain_QA_Project.git
cd LangChain_QA_Project
````

### ✅ Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📜 Sample Document

Put `.txt` files in the `documents/` folder.

**Example:** `documents/sample.txt`

```text
Artificial Intelligence (AI) is the simulation of human intelligence in machines programmed to think and learn like humans.
It includes fields like machine learning, deep learning, and natural language processing.
```

---

## ▶️ Run the App

```bash
python app.py
```

Then type your question:

```
🔎 Ask your question: What is AI?
```

**Output:**

```
🧠 Top Results from Documents:

[1] Artificial Intelligence (AI) is the simulation of human intelligence in machines...

📄 Source Files:
- sample.txt
```

---

## 🔧 requirements.txt

```txt
langchain
langchain-community
langchain-huggingface
chromadb
sentence-transformers
```

Install via:

```bash
pip install -r requirements.txt
```

---

## 🌐 Want a Web App?

You can convert this to a **web interface using Streamlit**. Just install it:

```bash
pip install streamlit
```

Then replace `input()` in `app.py` with:

```python
import streamlit as st
query = st.text_input("🔎 Ask your question:")
```

And run:

```bash
streamlit run app.py
```

---

## 📄 License

MIT License — free for personal and commercial use.

---

# 🙌 Author

Developed by \Manne SanjayKumar
📧 sanjaykumar@gmail.com
🌐 GitHub: https://github.com/ManneSanjayKumar

2. `requirements.txt`

> Save this as `requirements.txt` in the project root:

```txt
langchain
langchain-community
langchain-huggingface
chromadb
sentence-transformers
````

---

## 📃 3. `documents/sample.txt`

> Create a file `documents/sample.txt` and paste this:

```txt
Artificial Intelligence (AI) is the simulation of human intelligence in machines programmed to think and learn like humans.
It includes fields like machine learning, deep learning, and natural language processing.
```

---

✅ 4. Sample Query

When you run:

```bash
python app.py
```

And type:

```
🔎 Ask your question: What is Artificial Intelligence?
```

Expected Output:

```
🧠 Top Results from Documents:

[1] Artificial Intelligence (AI) is the simulation of human intelligence in machines...

📄 Source Files:
- sample.txt
```




