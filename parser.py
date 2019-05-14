
import re
import spacy
import sys
reload(sys)
#import pandas as pd
sys.setdefaultencoding('utf8')
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
import numpy as np
from docx import Document
from tika import parser

def todoc (f) :
    document = Document(f)
    for p in document.paragraphs:
       return p.text
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    #print(text)
    return text
def extract_clg(string):
    r1 = unicode(string)
    nlp = spacy.load("en")
    doc = nlp(r1)
    l=[]
    for ent in doc.ents:	
        if(ent.label_ == 'ORG'):
            print(ent.text)
            break
#Function to extract names from the string using spacy
def extract_name(string):
    r1 = unicode(string)
    nlp = spacy.load("xx")
    doc = nlp(r1)
    for ent in doc.ents:	
        if(ent.label_ == 'PER'):
            print(ent.text)
            break
#Function to extract Phone Numbers from string using regular expressions
def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]
#Function to extract Email address from a string using regular expressions
def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)
#Converting pdf/doc to string
f =""
f = raw_input("Enter the name of your text file - please use / backslash when typing in directory path: ");
if f.find("docx") == -1 or f.find("doc") == -1 : 
    input_string = convert(f)
if f.find("pdf") == -1 :
    input_string = todoc(f)

input_string1 = input_string
#Removing commas in the resume for an effecient check
input_string = input_string.replace(',',' ')
#Converting all the charachters in lower case
input_string = input_string.lower()
print('\n')
extract_name(input_string1)
print ("college name ")
extract_clg(input_string1)
print('\n')
print('Phone Number is')
y = extract_phone_numbers(input_string)
y1 = []
for i in range(len(y)):
    if(len(y[i])>9):
        y1.append(y[i])
print(y1)
print('\n')
print('Email id is')
print(extract_email_addresses(input_string))

print('\n \n')
