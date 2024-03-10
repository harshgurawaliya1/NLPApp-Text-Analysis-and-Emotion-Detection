from tkinter import *
from mydb import Database
from tkinter import messagebox
from newapi import SentimentAnalysisAPI



class NLPApp:

    def __init__(self):

        #database object
        self.dbo = Database()

        # GUI for Login
        self.root = Tk()
        self.root.title("NLPApp")
        self.root.geometry("350x600")
        self.root.configure(bg='#CACFD2')
        p1 = PhotoImage(file='hq.png')
        self.root.iconphoto(FALSE, p1)

        # call to method
        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", bg='#CACFD2', fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=30)
        self.email_input.pack(pady=(5,10))

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=30,show="*")
        self.password_input.pack(pady=(5, 10) )

        login_btn = Button(self.root,text="Login",width=15,height=2,bg="green",fg="green",command=self.perform_login)
        login_btn.configure(font=('verdana',15,'bold'),bg="green")
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text="Register Now", width=10, height=1, bg="green",fg="blue",command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", bg='#CACFD2', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(5, 10))

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5, 10))

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=30, show="*")
        self.password_input.pack(pady=(5, 10))

        register_btn = Button(self.root, text="Register", width=15, height=2, bg="green", fg="green",command=self.perform_registration)
        register_btn.configure(font=('verdana', 15, 'bold'), bg="green")
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text="Login Now", width=10, height=1, bg="green", fg="blue",command= self.login_gui)
        redirect_btn.pack(pady=(10, 10))



    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def perform_registration(self):
        # fetch data
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response1 = self.dbo.add_data(name,email,password)

        if response1:
            messagebox.showinfo('Success','Registration Successfull . You can login Now ')
        else:
            messagebox.showerror('Error','Email already exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response2 = self.dbo.search(email,password)

        if response2:
            messagebox.showinfo('Success', 'Login Successfull ')
            self.NLPgame()
        else:
            messagebox.showerror('Error', 'Incorrect Email/Password ')


    def NLPgame(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", bg='#CACFD2', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text="Sentiment Analysis", width=20, height=3, bg="green", fg="green", command=self.sentiment_gui)
        sentiment_btn.configure(font=('verdana', 15, 'bold'), bg="green")
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text="Named Entitiy Recognition", width=20, height=3, bg="green", fg="green",command=self.named_entity_recognition_gui)
        ner_btn.configure(font=('verdana', 15, 'bold'), bg="green")
        ner_btn.pack(pady=(10, 10))

        ep_btn = Button(self.root, text="Emotion Prediction", width=20, height=3, bg="green", fg="green",command=self.emotion_gui)
        ep_btn.configure(font=('verdana', 15, 'bold'), bg="green")
        ep_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text="Logout", width=10, height=1, bg="green", fg="blue",
                              command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", bg='#CACFD2', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Sentiment Analysis", bg='#CACFD2', fg='black')
        heading2.pack(pady=(15, 15))
        heading2.configure(font=('verdana', 20,))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=30,)
        self.sentiment_input.pack(pady=(5, 10))

        sentiment_btn = Button(self.root, text="Analyize Sentiment", width=20, height=2, bg="green", fg="green",command=self.do_sentiment_analysis)
        sentiment_btn.configure(font=('verdana', 18, 'bold'))
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='',bg='#CACFD2')
        self.sentiment_result.configure(font=('verdana', 16))
        self.sentiment_result.pack(pady=(10, 10))

        goback_btn = Button(self.root, text="BACK", width=10, height=1, bg="green", fg="blue",command=self.NLPgame)
        goback_btn.pack(pady=(10, 10))


    def do_sentiment_analysis(self):
        text1 = self.sentiment_input.get()

        if __name__ == "__main__":
            api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNmM2NDkxMTUtNzZhNy00MWJkLThjMWMtZDY0ZGM5Nzg5NzlmIiwidHlwZSI6ImFwaV90b2tlbiJ9.PBKWqCva2wPLnOPsJf7yt4vBJF5ZaLjr4CmrDxG5r9E"
            api_instance = SentimentAnalysisAPI(api_key)




            result = api_instance.analyze_sentiment(text1)

            self.sentiment_result['text'] = f"The sentiment is {result['amazon']['general_sentiment']}. The rate is {result['amazon']['general_sentiment_rate']}"
            if "error" in result:
                print(result["error"])
            else:
                print("The sentiment is ",result['amazon']['general_sentiment'],"The rate is ",result['amazon']['general_sentiment_rate'])


    def named_entity_recognition_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", bg='#CACFD2', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Named Entity Recognition", bg='#CACFD2', fg='black')
        heading2.pack(pady=(15, 15))
        heading2.configure(font=('verdana', 20,))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=30,)
        self.ner_input.pack(pady=(5, 10))

        ner_btn = Button(self.root, text="Named Entity Recognition", width=20, height=2, bg="green", fg="green",command=self.do_ner)
        ner_btn.configure(font=('verdana', 18, 'bold'))
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='',bg='#CACFD2')
        self.ner_result.configure(font=('verdana', 16))
        self.ner_result.pack(pady=(10, 10))

        goback_btn = Button(self.root, text="BACK", width=10, height=1, bg="green", fg="blue",command=self.NLPgame)
        goback_btn.pack(pady=(10, 10))


    def do_ner(self):
        text1 = self.ner_input.get()

        if __name__ == "__main__":
            api_key = "(your api key)"
            api_instance = SentimentAnalysisAPI(api_key)




            result = api_instance.analyze_ner(text1)
            items_list = result["amazon"]["items"]

            # Assuming self.ner_result is a Tkinter label
            self.ner_result['text'] = "\n".join(
                [f"Entity: {item['entity']}, Category: {item['category']}, Importance: {item['importance']}" for item in
                 items_list])



    def emotion_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", bg='#CACFD2', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Emotion Detection", bg='#CACFD2', fg='black')
        heading2.pack(pady=(15, 15))
        heading2.configure(font=('verdana', 20,))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.emotion_input = Entry(self.root, width=30,)
        self.emotion_input.pack(pady=(5, 10))

        emotion_btn = Button(self.root, text="Emotion Detection", width=20, height=2, bg="green", fg="green",command=self.do_emotion)
        emotion_btn.configure(font=('verdana', 18, 'bold'))
        emotion_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text='',bg='#CACFD2')
        self.emotion_result.configure(font=('verdana', 16))
        self.emotion_result.pack(pady=(10, 10))

        goback_btn = Button(self.root, text="BACK", width=10, height=1, bg="green", fg="blue",command=self.NLPgame)
        goback_btn.pack(pady=(10, 10))


    def do_emotion(self):
        text1 = self.emotion_input.get()

        if __name__ == "__main__":
            api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNmM2NDkxMTUtNzZhNy00MWJkLThjMWMtZDY0ZGM5Nzg5NzlmIiwidHlwZSI6ImFwaV90b2tlbiJ9.PBKWqCva2wPLnOPsJf7yt4vBJF5ZaLjr4CmrDxG5r9E"
            api_instance = SentimentAnalysisAPI(api_key)




            result = api_instance.analyze_emotion(text1)
            items_list = result["nlpcloud"]["items"]

            # Assuming self.ner_result is a Tkinter label
            self.emotion_result['text'] = "\n".join(
                [f"Emotion: {item['emotion']}, Emotion Score: {item['emotion_score']}" for item in
                 items_list])
















nlp = NLPApp()
