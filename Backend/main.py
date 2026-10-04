from markitdown import MarkItDown
from openai import OpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L3-v2")

#client = OpenAI(
#    api_key="",
#    base_url="https://api.groq.com/openai/v1",
#)

llm_model="openai/gpt-oss-120b"

system_prompt = (
f"""You are a technical documentation formatter.
    Reformat this specific section for a vector database index:
    1. Locate all legacy/unformatted code, function signatures, and parameter lists.
    2. Enclose them strictly in  code fences.
    3. Do NOT omit, summarize, or alter any text or code logic.
    4. make sure to emphasize important logics
"""
)

query_prompt = " "\
    "you are an agent that parses through documentation for an assembly language documentation and gives a user answer" \
    "the question is given and then multiple relevant information retrieved from a source database are given in the format" \
    "Question:<>  Reference:<> answer the question if any otherwise only send out code block"\
    "your answers must be in 64 bit unless specified and if its not a code-only prompt then you are supposed to give as much of"\
    "a lengthy and descriptive answer as you can( but must not be too long). but your only allowed to fetch info from the docs and dont make up any info. if you cant"\
    "find enough information to give a reliable answer then remain silent"

question_improver= ""\
    "[64 bit, memory, space, stack, heap, loop, condition]"

markdown_code_splitter = RecursiveCharacterTextSplitter(
    separators=[
        r"\n# ",       # Split on Top headings
        r"\n## ",      # Split on Sub headings
        r"\n```",      # Split right at code block boundaries
        r"\n\n",       # Split on paragraphs
        r"\n",         # Split on lines
        r" ",          # Split on words
        r""            # Ultimate fallback
    ],
    is_separator_regex=True,
    chunk_size=250,
    chunk_overlap=100
)
fileCount=0

#--------------------+++++++++++++-------------+++++++++++------------++++++++++++----------+++++


def DocumentLoader(filePath,fileCount):
    print("Loading Document...")
    md=MarkItDown()
    result = md.convert(filePath)
    open(f"processed/loaded{fileCount}.md", "w").write(result.markdown)

def TextSplitter():
    full_text=""
    with open("processed/nasm_final_doc.md", "r") as f:
        full_text = f.read()
    document_chunks=markdown_code_splitter.split_text(full_text)# error in this line: str object has no attribute page content
    return document_chunks

def vectorizer(document_chunks):
    vector_store = FAISS.from_texts(document_chunks, embeddings)
    return vector_store

def Indexer(vector_store):
    retriever = vector_store.as_retriever(
         search_type="similarity",
         search_kwargs={"k": 20}
        )
    return retriever
    

#DocumentLoader ("documents/nasmv4.html",4)
chunks=TextSplitter()
vectors=vectorizer(chunks)
retriever=Indexer(vectors)


def select_client(key,url,model):
    global client
    client= OpenAI(
        api_key=key,
        base_url=url,
    )
    global llm_model
    llm_model=model

def get_rag_response(question: str):
    reference=retriever.invoke(question+question_improver)
    try:
        response = client.chat.completions.create(
        model=llm_model,  # Or another supported model like gemini-2.5-pro
        messages=[
            {"role": "system", "content": query_prompt},
            {"role": "user", "content": f"Question:<{question}>   Reference:<{reference}>"}
        ]
        )
    except:
        return "llm communication error"
    return response.choices[0].message.content


    
