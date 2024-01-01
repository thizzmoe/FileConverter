import docx
import os
import comtypes
import comtypes.client

word_path = "testt.docx"
pdf_path = "testtt.pdf"
doc = docx.Document(word_path)
word = comtypes.client.CreateObject("Word.Application")
docx_path = os.path.abspath(word_path)
pdf_path = os.path.abspath(pdf_path)

pdf_format = 17
word.Visible = False
in_file = word.Documents.Open(docx_path)
in_file.SaveAs(pdf_path, FileFormat=pdf_format)
in_file.Close()
word.Quit()
#convert("testt.docx", "PDFtest.pdf")
"""
docx2pdf/convert("")
with open('data/testt.pdf', 'r') as f:
    data = f.read()
pdf_file= /data
docx_file =
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
"""




