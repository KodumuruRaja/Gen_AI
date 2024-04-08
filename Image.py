#!/usr/bin/env python
# coding: utf-8

# ### Pytesseract

# In[1]:


import pytesseract as py
from PIL import Image
img = Image.open("GoToWebinar 004.png")


# In[2]:


img


# In[3]:


text = py.image_to_string(img)
text


# In[4]:


import re
text = re.sub('\n'," ",text)
text = re.sub(" +"," ",text)
text


# ### EasyOCR

# In[5]:


import easyocr


# In[6]:


text = easyocr.Reader(['en'])
text = text.readtext("GoToWebinar 004.png")
text


# In[7]:


text1 = []
for i in range(len(text)):
    text1.append(text[i][1])


# In[8]:


text1


# In[9]:


text2 = " "
text2.join(text1)


# In[ ]:





# ### LangChain

# In[32]:


from langchain_community.document_loaders.image import UnstructuredImageLoader


# In[49]:


loader = UnstructuredImageLoader("pict.jpg")
text = loader.load()
text


# In[76]:


l = []
for t in text:
    page_content = t.page_content
    l.append(page_content)


# In[77]:


l


# In[78]:


text1 = " "
text1 = text1.join(l)


# In[79]:


text1


# In[80]:


import re
text1 = re.sub('\n'," ",text1)
text1 = re.sub(" +"," ",text1)
text1


# In[ ]:





# ### cv2

# In[84]:


import cv2
import pytesseract


# In[86]:


img = cv2.imread("pict.jpg")
text = pytesseract.image_to_string(img)
print(text)


# In[ ]:





# ### Converting PDF to Images

# In[87]:


import pypdfium2 as pdfium
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO


# In[88]:


def convert_pdf_to_images(file_path, scale=300/72):
    
    pdf_file = pdfium.PdfDocument(file_path)  
    page_indices = [i for i in range(len(pdf_file))]
    
    renderer = pdf_file.render(
        pdfium.PdfBitmap.to_pil,
        page_indices = page_indices, 
        scale = scale,
    )
    
    list_final_images = [] 
    
    for i, image in zip(page_indices, renderer):
        
        image_byte_array = BytesIO()
        image.save(image_byte_array, format='jpeg', optimize=True)
        image_byte_array = image_byte_array.getvalue()
        list_final_images.append(dict({i:image_byte_array}))
    
    return list_final_images


# In[89]:


def display_images(list_dict_final_images):
    
    all_images = [list(data.values())[0] for data in list_dict_final_images]

    for index, image_bytes in enumerate(all_images):

        image = Image.open(BytesIO(image_bytes))
        figure = plt.figure(figsize = (image.width / 100, image.height / 100))

        plt.title(f"----- Page Number {index+1} -----")
        plt.imshow(image)
        plt.axis("off")
        plt.show()


# In[90]:


convert_pdf_to_images = convert_pdf_to_images('C:/Users/Raja/Downloads/LlamaIndex Talk (MistralAI).pdf')


# In[91]:


display_images(convert_pdf_to_images)


# ### Pytesseract

# In[95]:


from pytesseract import image_to_string 


# In[96]:


def extract_text(list_dict_final_images):
    
    image_list = [list(data.values())[0] for data in list_dict_final_images]
    image_content = []
    
    for index, image_bytes in enumerate(image_list):
        
        image = Image.open(BytesIO(image_bytes))
        raw_text = str(image_to_string(image))
        image_content.append(raw_text)
    
    return "\n".join(image_content)


# In[97]:


text = extract_text(convert_pdf_to_images)
text


# ### EasyOCR

# In[98]:


from easyocr import Reader
language_reader = Reader(["en"])


# In[99]:


def extract_text(list_dict_final_images):
    
    image_list = [list(data.values())[0] for data in list_dict_final_images]
    image_content = []
    
    for index, image_bytes in enumerate(image_list):
        
        image = Image.open(BytesIO(image_bytes))
        raw_text = language_reader.readtext(image)
        raw_text = "\n".join([res[1] for res in raw_text])
                       
        image_content.append(raw_text)
    
    return "\n".join(image_content)


# In[100]:


text1 = extract_text(convert_pdf_to_images)
text1


# In[ ]:





# ### PyPDF

# In[101]:


from PyPDF2 import PdfReader


# In[102]:


def extract_text(PDF_File):

    pdf_reader = PdfReader(PDF_File)
    
    raw_text = ''

    for i, page in enumerate(pdf_reader.pages):
        
        text = page.extract_text()
        if text:
            raw_text += text

    return raw_text


# In[104]:


text2 = extract_text("C:/Users/Raja/Downloads/LlamaIndex Talk (MistralAI).pdf")
text2


# ### LangChain

# In[110]:


from langchain.document_loaders import UnstructuredFileLoader

def extract_text(pdf_file):
    
    loader = UnstructuredFileLoader(pdf_file)
    documents = loader.load()
    pdf_pages_content = '\n'.join(doc.page_content for doc in documents)
    
    return pdf_pages_content


# In[ ]:


text3 = extract_text("C:/Users/Raja/Downloads/LlamaIndex Talk (MistralAI).pdf")
text3


# In[ ]:




