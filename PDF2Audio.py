# Importing the required packages.
import sys
import PyPDF2
from tkinter import messagebox
import pyttsx3
from tkinter import filedialog
text = None

from deep_translator import GoogleTranslator
Translator = GoogleTranslator(source="auto",target="en")

def translate(text,from_lang="en",to_lang="hi"):
    return Translator.translate(text,from_code=from_lang,to_code=to_lang)

# Reading a PDF file from your computer by specifying the path and setting the read mode to binary.
filename = filedialog.askopenfilename(filetype=(["filetype:","*.pdf"],["all files","*.*"]))
if filename == "":
    messagebox.showerror("No PDF File Selected","You did not selected any PDF file.")
    sys.exit()
pdf_reader = PyPDF2.PdfReader(open(filename, "rb"))

# Getting the handle to speaker i.e. creating a reference to pyttsx3.Engine instance.
speaker = pyttsx3.init()

# Splitting the PDF file into pages and reading one at a time.
for page_number in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[page_number].extract_text()

# Saving the audiobook to your computer.
engine = pyttsx3.init()
output = filedialog.asksaveasfilename(filetype=(["filetype:",".mp3"],["All types:","*.*"]))
if output == "":
    messagebox.showwarning("No output Path Selected","You did not selected any path where to save the generated audio file. \n File is saved as: audio.mp3 in local directory")
    output = "audio.mp3"
engine.save_to_file(text, output+".mp3")
engine.runAndWait()
