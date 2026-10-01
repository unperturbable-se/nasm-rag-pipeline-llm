from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI(
    api_key="redacted",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

system_prompt = (
f"""You are a technical documentation formatter.
    Reformat this specific section for a vector database index:
    1. Locate all legacy/unformatted code, function signatures, and parameter lists.
    2. Enclose them strictly in  code fences.
    3. Do NOT omit, summarize, or alter any text or code logic.
    4. make sure to emphasize important logics
"""
)
fileCount=0

#--------------------+++++++++++++-------------+++++++++++------------++++++++++++----------+++++


def DocumentLoader(filePath,fileCount):
    print("Loading Document...")
    md=MarkItDown()
    result = md.convert(filePath)
    open(f"processed/loaded{fileCount}.md", "w").write(result.markdown)
#def DocumentCleaner(fileCount):
#    print("Cleaning Document...")
#    document=""
#    document=open(f"processed/loaded{fileCount}.md", "r").read()
#    response = client.chat.completions.create(
#        model="gemini-3.5-flash",
#        messages=[
#            {"role": "system", "content": system_prompt},
#            {"role": "user", "content": document}
#        ],
#        temperature=0.2
#    )
#    cleaned_document = response.choices[0].message.content
#    open(f"cleaned/cleaned{fileCount}.md", "w").write(cleaned_document)
#    pass
def TextSplitter():
    pass

def Indexer():
    pass

DocumentLoader ("documents/nasmv4.html",4)
#DocumentCleaner(2)

    
