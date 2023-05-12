markdown_text = ""

import markdown  # pip install markdown
from bs4 import BeautifulSoup


def md_to_text(md):
    md = md.replace("```","")
    md = md.replace("**","")
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features='html.parser')
    plain_text = soup.get_text()
    return plain_text

text = md_to_text(markdown_text)
print(text)