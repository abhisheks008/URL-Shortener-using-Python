'''
Create a URL Shortner in Python
Author: Abhishek Sharma
'''

import pyshorteners
import pyperclip 
from tkinter import *

root = Tk()
root.geometry("500x250")
root.title("My URL shortener")
root.configure(bg = "#49A")
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root, text = "My URL Shortener", font = "Arial").pack(pady=20)
Entry(root,textvariable = url).pack(pady=10)
Button(root, text = "Generate Short URL", command = urlshortener).pack(pady=7)
Entry(root,textvariable=url_address).pack(pady=10)
Button(root,text = "Copy URL", command = copyurl).pack(pady=5)

root.mainloop()