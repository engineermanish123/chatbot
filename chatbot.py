from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("chatbot")
        self.root.geometry("730x620+0+0")

        main_frame = Frame(self.root, bd=4, bg='powder blue', width=610)
        main_frame.pack()

        img_chat = Image.open('bot.jpg')
        img_chat = img_chat.resize((200, 70), resample=2)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730, compound=LEFT, image=self.photoimg, text='Have a Chat', font=('arial', 30, 'bold'), fg='blue', bg='white')
        title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('arial', 14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, bd=4, bg='white', width=730)
        btn_frame.pack()

        label_1 = Label(btn_frame, text="Type Something", font=('arial', 14, 'bold'), fg='blue', bg='white')
        label_1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = ttk.Entry(btn_frame, width=40, font=('times new roman', 16, 'bold'))
        self.entry.grid(row=0, column=1, padx=5, sticky=W)

        self.send = Button(btn_frame, text="Send>>", command=self.send, font=('arial', 15, 'bold'), width=8, bg='blue')
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear = Button(btn_frame, text="Clear Data>>", font=('arial', 15, 'bold'), width=13, bg='green', fg='white', command=self.clear_data)
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.msg=''
        self.label_11 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), fg='blue', bg='white')
        self.label_11.grid(row=0, column=0, padx=5, sticky=W)


    def send(self):
        send_msg = '' + 'You:' + self.entry.get()#\t\t\t
        self.text.insert(END, '\n' + send_msg)

        if(self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_11.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi there')

        elif(self.entry.get()=='Hii'):
            self.text.insert(END,'\n\n'+'Bot:Hello there')

        elif(self.entry.get()=='hey'):
            self.text.insert(END,'\n\n'+'Bot:Hello there')

        elif(self.entry.get()=='hii'):
            self.text.insert(END,'\n\n'+'Bot:Hello there')

        elif(self.entry.get()=='How are you'):
            self.text.insert(END,'\n\n'+'Bot:Im great! Thanks for asking.')
        
        elif(self.entry.get()=='nice to meet you'):
            self.text.insert(END,'\n\n'+'Bot:The pleasure is all mine!')

        elif(self.entry.get()=='Weekend Getaway'):
            self.text.insert(END,'\n\n'+'Enjoy a complimentary breakfast for weekend stays')

        elif(self.entry.get()=='bye'):
            self.text.insert(END,'\n\n'+'Thank You For Chatting')

        else:
            self.text.insert(END,"\n\n"+"Bot : Sorry I dindn't get it ")



    def clear_data(self):
        self.text.delete(1.0, END)
        self.entry.delete(0, 'end')

if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
