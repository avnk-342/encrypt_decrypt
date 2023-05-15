
from tkinter import *

root = Tk()
root.geometry('300x200')
# root.resizable(False,False)
root.title("encryption & decryption")

def caesar_cipher():
    text = text1.get()
    result = ""
    s = 2 #shift in the value
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    label = Label(root , text=result)
    label.pack()
    button1["state"] = DISABLED

def decode():
    text = text2.get()
    result = ""
    s = 26-2 #shift in the value
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    label = Label(root , text=result)
    label.pack()
    button2["state"] = DISABLED

text1 = Entry(root, text='please enter your message here')
text2 = Entry(root , text='please enter your encryption')
text1.place(width=100, height=100, x=10, y=10)
text1.pack()
text2.place(width=100, height=100, x=10, y=10)
text2.pack()
button1 = Button(root, text='encrypt', command=caesar_cipher)
button1.pack()
button2 = Button(root, text='decode', command=decode)
button2.pack()




root.mainloop()