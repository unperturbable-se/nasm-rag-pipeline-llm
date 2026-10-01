
import glob
from bs4 import BeautifulSoup

files = sorted(glob.glob("/home/raed/Documents/nasm docs/**/*.html", recursive=True))
cleaned_bodies = []
skipped_count = 0

for f in files:
    content = open(f, errors="ignore").read()
    
    # 1. Skip server directory listings and auto-generated file index pages
    if "Index of /" in content or "Browse source code for this build" in content:
        skipped_count += 1
        continue

    soup = BeautifulSoup(content, "html.parser")

    # 2. Skip pages where the title/h1 indicates an index directory
    title = soup.find(["title", "h1"])
    if title and "Index of /" in title.get_text():
        skipped_count += 1
        continue

    # 3. Strip images completely
    for img in soup.find_all("img"):
        img.decompose()

    # 4. Remove Table of Contents & Navigation DOM nodes
    for nav in soup.find_all(["nav", "aside"]):
        nav.decompose()
        
    for toc in soup.find_all(class_=["toc", "contents_toc", "navtree", "index"]):
        toc.decompose()

    # 5. Unwrap <a> tags (keep function/class names as text, destroy URLs)
    for a in soup.find_all("a"):
        a.unwrap()

    # 6. Save clean body content
    if soup.body:
        cleaned_bodies.append(str(soup.body))

# Output clean single HTML file
open("documents/nasmv4.html", "w", encoding="utf-8").write(
    f"<!DOCTYPE html><html><body>{''.join(cleaned_bodies)}</body></html>"
)

print(f"Done! Processed {len(files) - skipped_count} documentation pages.")
print(f"Skipped {skipped_count} server directory index pages.")