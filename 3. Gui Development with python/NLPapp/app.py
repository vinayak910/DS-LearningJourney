from tkinter import *
from mydb import Database
from myapi import API
from tkinter import messagebox
class NLPApp:

    def __init__(self):
        self.dbo = Database()
        self.apimy = API()

        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon-96x96.png')
        self.root.geometry('350x600')
        self.root.config(bg = '#A569BD')

        self.login_gui()
        self.root.mainloop()

    def login_gui(self):

        self.clear()
        heading = Label(self.root , text = "NLP App",bg = '#A569BD')
        heading.pack(pady = (30 , 30))
        heading.configure(font = ('verdana','18','bold'))

        label1 = Label(self.root , text = "Enter Email:",bg = '#A569BD')
        label1.pack(pady = (10 , 10))

        self.email_input = Entry(self.root , width = 50)
        self.email_input.pack(pady = (5 , 10) , ipady = 3)

        label2 = Label(self.root, text="Enter Password:",bg = "#A569BD")
        label2.pack(pady=(10, 10))

        self.password = Entry(self.root , width = 50,show = "*")
        self.password.pack(pady = (5 , 10) , ipady = 3)

        loginbtn = Button(self.root , text = 'Login' , width = 30  ,height = 1,bg = '#17202A',fg = 'white',command=self.perform_login)
        loginbtn.pack(pady = (10 , 10))

        label3 = Label(self.root , text = 'Not a member?',bg = "#A569BD")
        label3.pack(pady = (20 , 10))

        redirect_btn = Button(self.root , text = "Register Now" ,bg = '#17202A',fg = 'white', command = self.register_gui)
        redirect_btn.pack(pady = (10 , 10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text="NLP App", bg='#A569BD')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', '18', 'bold'))

        label0 = Label(self.root , text = "Enter Name:",bg='#A569BD')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=3)

        label1 = Label(self.root, text="Enter Email:", bg='#A569BD')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=3)

        label2 = Label(self.root, text="Enter Password:", bg="#A569BD")
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show="*")
        self.password_input.pack(pady=(5, 10), ipady=3)

        register_btn = Button(self.root, text='Register', width=30, height=1, bg='#17202A', fg='white',command = self.perform_registeration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?', bg="#A569BD")
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text="Login Now", bg='#17202A', fg='white', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def perform_registeration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name , email , password)

        if response:
            messagebox.showinfo('Sucess' , 'Registeration Successful. You can login now')
        else:
            messagebox.showinfo('Error' , 'User already exists with this email')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password.get()

        response = self.dbo.search(email , password)
        if response:
            self.home_gui()
        else:
            messagebox.showinfo("Incorrect email/password")

    def home_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP App", bg='#A569BD')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', '18', 'bold'))

        label1 = Label(self.root, text="Welcome , Which nlp task you would like to perform?", bg='#A569BD')
        label1.pack(pady=(10, 10))

        sentimentbtn = Button(self.root, text='Sentiment Analysis', width=30, height=4, bg='white', fg='black',command= self.sentiment_gui
                          )
        sentimentbtn.pack(pady=(10, 10))

        nerbtn = Button(self.root, text='Named Entity Recognition', width=30, height=4, bg='white', fg='black' , command=self.ner_gui
                              )
        nerbtn.pack(pady=(10, 10))

        emotionbtn = Button(self.root, text='Emotion Prediction', width=30, height=4, bg='white', fg='black'
                              )
        emotionbtn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text="Logout Now", bg='#17202A', fg='white', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):

        self.clear()

        heading = Label(self.root, text="NLP App", bg='#A569BD')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', '18', 'bold'))

        heading = Label(self.root, text="Sentiment Analysis", bg='#A569BD')
        heading.pack(pady=(10, 20))
        heading.configure(font=('verdana', '18'))

        label1 = Label(self.root, text="Enter the text:", bg='#A569BD')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady= 20)

        sentimentbtn = Button(self.root, text="Analyze Sentiment", bg='#17202A', fg='white' , command=self.do_sentiment_analysis)
        sentimentbtn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text="", bg="#A569BD")
        self.sentiment_result.pack(pady=(10, 10))
        heading.configure(font=('verdana', '16'))

        backbtn = Button(self.root, text="Go Back", bg='#17202A', fg='white', command=self.home_gui)
        backbtn.pack(pady=(10, 10))


    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apimy.sentiment_analysis(text)
        print(result)
        scores = result['sentiment']
        display = ""
        for i , j in scores.items():
            display = display + i + " ==> " + str(j) + '\n'

        self.sentiment_result['text'] = display

    def ner_gui(self):

        self.clear()

        heading = Label(self.root, text="NLP App", bg='#A569BD')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', '18', 'bold'))

        heading = Label(self.root, text="Named Entity Recognition", bg='#A569BD')
        heading.pack(pady=(10, 20))
        heading.configure(font=('verdana', '18'))

        label1 = Label(self.root, text="Enter the text:", bg='#A569BD')
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady= 20)

        nerbtn = Button(self.root, text="Perform NER", bg='#17202A', fg='white' , command=self.do_ner)
        nerbtn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text="", bg="#A569BD")
        self.ner_result.pack(pady=(10, 10))
        heading.configure(font=('verdana', '16'))

        backbtn = Button(self.root, text="Go Back", bg='#17202A', fg='white', command=self.home_gui)
        backbtn.pack(pady=(10, 10))

    def do_ner(self):
        text = self.ner_input.get()
        result = self.apimy.ner_nlp(text)
        display = ""
        for i in result['entiies']:
            display = display + (f"{i['name']}  ==>  {i['category']} \n")

        self.ner_result['text'] = display
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

nlp = NLPApp()