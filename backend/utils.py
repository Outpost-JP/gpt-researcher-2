import os
import aiofiles
import urllib
import uuid
from md2pdf.core import md2pdf

async def write_to_file(filename: str, text: str) -> None:
    text_utf8 = text.encode('utf-8', errors='replace').decode('utf-8')
    async with aiofiles.open(filename, "w", encoding='utf-8') as file:
        await file.write(text_utf8)

async def create_css_file(css_file_path: str) -> None:
    css_text = """
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&display=swap');

    body {
      font-family: 'Noto Sans', sans-serif;
    }
    """
    if not os.path.exists(css_file_path):
        async with aiofiles.open(css_file_path, "w") as file:
            await file.write(css_text)

async def write_md_to_pdf(text: str) -> str:
    css_file_path = "your_css_file.css"
    await create_css_file(css_file_path)

    task = uuid.uuid4().hex
    file_path = f"outputs/{task}"
    await write_to_file(f"{file_path}.md", text)

    try:
        md2pdf(f"{file_path}.pdf",
               md_content=None,
               md_file_path=f"{file_path}.md",
               css_file_path=css_file_path,
               base_url=None)
        print(f"Report written to {file_path}.pdf")
    except Exception as e:
        print(f"Error in converting Markdown to PDF: {e}")
        return ""

    encoded_file_path = urllib.parse.quote(f"{file_path}.pdf")
    return encoded_file_path
