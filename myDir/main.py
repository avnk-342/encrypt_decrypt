from tkinter import *



def exit():
    root.destroy()
    

def results():
    
    ch = var.get()
    
    if ch==1 :
        text = text1.get()
        result = ""
        s = int(text2.get()) #shift in the value
        # traverse text
        for i in range(len(text)):
            char = text[i]
    
            # Encrypt uppercase characters
            if (char == " "):
                result += " "
                
            elif (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
    
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
    
        text3 = Entry(root)
        text3.place(x=350,y = 300)
        text3.insert(0,result)
        
    elif ch == 2:
        text = text1.get()
        
        
        letters="abcdefghijklmnopqrstuvwxyz"
    
        #enter the key value to decrypt
        k = int(text2.get())
        decrypted_message = ""

        for ch in range(len(text)):
            char = text[ch]
            
            if char == " ":
                decrypted_message += " "
            
            elif char in letters:
                position = letters.find(char)
                new_pos = (position - k) % 26
                new_char = letters[new_pos]
                decrypted_message += new_char
            else:
                decrypted_message += char
        
        text3 = Entry(root)
        text3.place(x=350,y = 300)
        text3.insert(0,decrypted_message)



     
root = Tk()
root.geometry('952x491')
root.resizable(0,0)
root.title("encryption & decryption")
root.config(bg='#ccf5ac')


heading = Label(root, text="Welcome to encryption-n-decryption",bg='#caf0f8',padx=10,pady=10)
heading.config(font=('Helvetica', 15))


text1 = Entry(root)
text1.place(width=200, height=35)

text2 = Entry(root)
text2.place(width=200, height=35)

lable1 = Label(root, text="Enter your message here: ", bg='#ccf5ac')
label2 = Label(root, text="Please insert a key: ", bg='#ccf5ac')
label3 = Label(root, text="RESULT = ", bg='#ccf5ac')


button1 = Button(root, text='Action', command=results, bg='#26C485')
button2 = Button(root, text='Exit', command=exit, bg='red')


var = IntVar()
radio1 = Radiobutton(root, text='Encryption ', variable=var,value=1)
radio2 = Radiobutton(root, text='Decryption ', variable=var,value=2)


heading.place(x=325,y=20)

lable1.place(x=250,y=110)
label2.place(x=250,y=165)
label3.place(x=275,y=303)

text1.place(x=450,y=100)
text2.place(x=450,y=150)

button1.place(x=450,y=235)
button2.place(x=300, y=235)

radio1.place(x=350,y=200)
radio2.place(x=500,y=200)

root.mainloop()