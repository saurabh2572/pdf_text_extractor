import pdf2image
import pytesseract
from pytesseract import Output, TesseractError
import streamlit as st
# @st.cache_data
# def images_to_txt(path, language):
#     images = pdf2image.convert_from_bytes(path)
all_text = []
#     for i in images:
pil_im = "/Users/saurabh.prajapati/Downloads/1697372940826.jpeg"
text = pytesseract.image_to_string(pil_im, lang="eng")
# ocr_dict = pytesseract.image_to_data(pil_im, lang='eng', output_type=Output.DICT)
# ocr_dict now holds all the OCR info including text and location on the image
# text = " ".join(ocr_dict['text'])
# text = re.sub('[ ]{2,}', '\n', text)
all_text.append(text)
print(all_text)
