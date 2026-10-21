from pymupdf import open
import re
from typing import List
from pathlib import Path


def extract_paragraphs(pdf_path : str | Path) -> List[str]:
    """This function takes a PDF path and returns a list of its paragraph"""
    doc = open(pdf_path)
    paragraphs = []

    for page in doc:
        #GET blocks from page
        blocks = page.get_text("blocks")

        #sort blocks from top to bottom
        blocks = sorted(blocks , key = lambda b:(b[1] , b[0]))

        for block in blocks:
            text = block[4]

            #REPLACE line breaks inside a paragraph wirh spaces
            text = re.sub(r"\r+" , " ", text).strip()


            if text:
                paragraphs.append(text)
    return paragraphs
