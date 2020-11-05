from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import filedialog
import os
import pathlib
import glob

import cv2

import requests
import io
import json
from tkinter import ttk

import pytesseract
import enchant 


def logout():
    global screen4
    global EXIT_Frame
    def cntinue():
        uploading()
    def lgout():
        main_screen()
        
    
    screen4=Tk()
    screen4.geometry("300x250")
    screen4.title("TEXT-RECOGNITION")
    '''Label(text="EXTRACT THE TEXT",bg="grey",width="300",height="2",font=("calibri",13)).place(x=0,y=0,relwidth=1)
    Label(text="").pack()'''

    Label(screen4,text="EXTRACT THE TEXT",font=("times new roman",40,"bold"),bg="black",fg="white",bd=10,relief=GROOVE).place(x=0,y=0,relwidth=1)
    
    EXIT_Frame=Frame(screen4)
    EXIT_Frame.place(x=700,y=250)
    
    Button(EXIT_Frame,text="CONTINUE",height="2",width="30",font=("times new roman",14,"bold"),bg="black",fg="white",command=cntinue).grid(row=1,column=0,padx=20)

    Label(EXIT_Frame,text="").grid(row=2,column=0,padx=20)

    Button(EXIT_Frame,text="LOGOUT",height="2",width="30",font=("times new roman",14,"bold"),bg="black",fg="white",command=lgout).grid(row=3,column=0,padx=20)


    screen4.attributes("-fullscreen",True)
    


def uploading():
    global screen3
    global frame4
    global combo
    global lng
    global options
    #def comboclick(event):
        
        #lng=combo.get()
        
    def upload():
        global b
        global img
        global config
        global d
        global text_
        global t
        global s
        global u
        global lg

        global m
        global api_key
        global data
        global params
        global headers
        global response
        global json_response
        global d1
        global a
        global j
        global pre
        global language_list
        global lol1,lol2
        global l
        '''lg=lng.get()
        lg=lg[:3]
        b=filedialog.askopenfilename(initialdir="/Desktop",title="select a file")
        #c=str(b)
        pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        img=cv2.imread(b)
        config="--psm 3"
        text=pytesseract.image_to_string(img,config=config,lang=lg)
        #print(text)

        d = enchant.Dict("en_US")
        t=text.split()
        
        for i in t:
            if d.check(i)==False:
                u="\u0332".join("i")
                text=text.replace(i,u)

        file=open("text_recognised.txt","w")
        file.write(text+"\n \n \n")


        #file=open("text_recognised.txt","r")
        #ch=file.read().split()

        
        for i in t:
            if d.check(i)==False:

                s=d.suggest(i)
                s=",".join(s)
                file.writelines(i +":"+ s+"\n") 

        file.close()'''
        j=0;pre={};l=[]
        language_list=["ara","rus","dan","fin","ita","kor","nor"]
        lg=lng.get()
        lg=lg[:3]
        b=filedialog.askopenfilename(initialdir="/Desktop",title="select a file")
        #c=str(b)
        
        pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        img=cv2.imread(b)
        config="--psm 3"
        if lg=="chi":
            
            text_=pytesseract.image_to_string(img,config=config,lang="chi-sim")
            api_key = "4c1889c72069433c89b67b6532729a16"
            #example_text = "hello man iam here where are yu this is the time u migt be daing" # the text to be spell-checked
            endpoint = "https://api.cognitive.microsoft.com/bing/v7.0/spellcheck"
            data = {'text':text_}
            params = {
                'mkt':'zh-CN',
                'mode':'spell'
                }
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Ocp-Apim-Subscription-Key': api_key,
                }
            response = requests.post(endpoint, headers=headers, params=params, data=data)
            json_response = response.json()
            d=json.dumps(json_response, indent=4)
            #print(json_response)
            #print(d)
            file=open("text_recognised.txt","w")
            file.writelines(text_+"\n \n \n")

            a=json.loads(d)
            
            for i in a['flaggedTokens']:
                        lol1=i['token']
                        #for j in range(len(a['flaggedTokens'])):
                        lol2=a['flaggedTokens'][j]['suggestions'][0]['suggestion']
                        pre={'misspelled':lol1,'suggestions':lol2}
                        l.append(pre)
                        j+=1
                        
            for o in l:
                
                file.writelines(o['misspelled']+':'+o['suggestions']+'\n')
            file.close()
            
            
        elif lg=="eng":

            text_=pytesseract.image_to_string(img,config=config,lang=lg)
            
            d1 = enchant.Dict("en_GB")
            t=text_.split()

            file=open("text_recognised.txt","w")
            file.write(text_+"\n \n \n")


            
            for i in t:
                if d1.check(i)==False:

                    s=d1.suggest(i)
                    s=",".join(s)
                    file.writelines(i +":"+ s+"\n") 

            file.close()
        else:
            if lg in language_list:
                lg=lg[:2]
                m=lg
                #text_=pytesseract.image_to_string(img,config=config,lang=lg)
            elif lg=="spa":
                #text_=pytesseract.image_to_string(img,config=config,lang=lg)
                m='en-ES'
            elif lg=="nld":
                #text_=pytesseract.image_to_string(img,config=config,lang=lg)
                m='nl-NL'
            elif lg=="fra":
                #text_=pytesseract.image_to_string(img,config=config,lang=lg)
                m='fr-FR'
            elif lg=="swe":
                #text_=pytesseract.image_to_string(img,config=config,lang=lg)
                m='sv'
            elif lg=="tur":
                #text_=pytesseract.image_to_string(img,config=config,lang=lg)
                m='tr'
            elif lg=="due":
                #text_=pytesseract.image_to_string(img,config=config,lang=lg)
                m='de-DE'
            elif lg=="jpn":
                #text_=pytesseract.image_to_string(img,config=config,lang=lg)
                m='ja'
            elif lg=="pol":
                #text_=pytesseract.image_to_string(img,config=config,lang=lg)
                m='pl'
            elif lg=="por":
                #text_=pytesseract.image_to_string(img,config=config,lang=lg)
                m='pt-PT'
            api_key = "4c1889c72069433c89b67b6532729a16"
            #example_text = "hello man iam here where are yu this is the time u migt be daing" # the text to be spell-checked
            text_=pytesseract.image_to_string(img,config=config,lang=lg)
            endpoint = "https://api.cognitive.microsoft.com/bing/v7.0/spellcheck"
            data = {'text':text_}
            params = {
                'mkt':m,
                'mode':'spell'
                }
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Ocp-Apim-Subscription-Key': api_key,
                }
            response = requests.post(endpoint, headers=headers, params=params, data=data)
            json_response = response.json()
            d=json.dumps(json_response, indent=4)#python to json
            #print(json_response)
            #print(d)
            file=open("text_recognised.txt","w")
            file.writelines(text_+"\n \n \n")

            a=json.loads(d)
            
            for i in a['flaggedTokens']:
                        lol1=i['token']
                        lol2=a['flaggedTokens'][j]['suggestions'][0]['suggestion']
                        pre={'misspelled':lol1,'suggestions':lol2}
                        l.append(pre)
                        j+=1
                        #print("Misspelled word :",a['flaggedTokens'][k]['token'])
                        #print("Suggested word :",a['flaggedTokens'][k]['suggestions'][k]['suggestion'])
            for o in l:
                file.writelines(o['misspelled']+':'+o['suggestions']+'\n')
            file.close()

        
                
        cv2.imshow("inserted_image",img)

        logout()


    lng=StringVar()    
    screen3=Toplevel(screen)
    screen3.title("Uploading an image")
    screen3.geometry("1350x700")
    frame4=Frame(screen3)
    frame4.place(x=700,y=250)
    Label(screen3,text="SELECT AN IMAGE TO BE CONVERTED",font=("times new roman",20,"bold"),bg="black",fg="white",bd=10,relief=GROOVE).place(x=0,y=0,relwidth=1)

    #ttk.Label(screen3, text = "Select the Month :",font = ("Times New Roman", 10)).grid(column = 0,row = 15, padx = 10, pady = 25)     
    Label(frame4,text="SELECT LANGUAGE",font=("times new roman",10,"bold"),bg="black",fg="white",bd=10,relief=GROOVE).grid(row=1,column=0,padx=20)
    options=["afr(Afrikans)","amh(Amharic)","ara(Arabic)","asm(Assamese)","aze(Azerbaijani)","bel(Belarsian)","ben(Bengali)","bod(Tebetan)","bos(Bosnian)","bul(Bulgarian)","cat(Catalan)","ceb(Cebuano)","ces(Czech)","chr(Cherokee)","cym(Welsh)","chi-sim(Chinese)","dan(Danish)","deu(German)","dzo(Dzongkha)","eng(English)","epo(Esperanto)","est(Estonian)","eus(Basque)","fas(Persian)","fin(Finish)","fra(French)","gle(Irish)","glg(Galicium)","grc(Ancient)","guj(Gujarati)","hat(Haitian)","Heb(Hebrew)","hin(Hindi)","hrv(Croatian)","hun(Hungarian)","iku(Inuktitut)","ind(Indonesian)","isl(Icelandic)","ita(Italian)","jpn(Japanese)","kan(Kannada)","kat(Georgian)","kaz(Kazakh)","kir(Kirghiz)","kor(Korean)","lat(Latin)","lit(lithuaninan)","mal(Malayalam)","mar(Marathi)","mkd(Macedonian)","mlt(Maltese)","mya(Burmese)","nep(Nepali)","nld(Dutch)","nor(Norwegian)","ori(Odiya)","pan(Punjab)","pol(Polish)","por(Portuguese)","ron(Romania)","rus(Russian)","san(Sanskrit)","sin(Sinhala)","spa(Spanish)","srp(Serbian)","swe(Swedish)","syr(Syriac)","tam(Tamil)","tel(Telugu)","tgl(Tagalog)","tha(Thai)","tur(Turkish)","ukr(Ukrinian)","urd(Urdu)","uzb(Uzbek)","vie(Vietnamese)","yid(Yiddish)"]
    Label(frame4,text="").grid(row=2,column=0,padx=20)
    combo=ttk.Combobox(frame4,value=options,height="10",width="30",textvariable=lng)
    combo.set("select")
    combo.grid(row=3,column=0,padx=20)
    Label(frame4,text="").grid(row=4,column=0,padx=20)
    Label(frame4,text="").grid(row=5,column=0,padx=20)
    Label(frame4,text="").grid(row=6,column=0,padx=20)



    Button(frame4,text="UPLOAD",height="2",width="20",font=("times new roman",14,"bold"),bg="black",fg="white",command=upload).grid(row=7,column=0,padx=20)
    
        
    #Button(frame4,text=" ",height="2",width="30",font=("times new roman",14,"bold"),bg="black",fg="white",command=register).grid(row=3,column=0,padx=20)

    screen3.attributes("-fullscreen",True)



   

















def message():
    global p1
    global u1
    u1=user_n.get()
    p1=pass_n.get()
    u1+=".txt"
    path="C:/Users/nikhil/AppData/Local/Programs/Python/Python38-32"

    list_of_files=os.listdir(path)
    
    if u1=="" or p1=="":
        messagebox.showerror("Error","All the fields are required!")
    elif u1=="" and p1.get()=="":
        messagebox.showerror("Error","All the fields are required!")
        
    
    elif u1 in list_of_files:
        
        file1=open(u1,"r")
        verify=file1.read().splitlines()
        if p1 in verify:
            
            messagebox.showinfo("successful","You are logged in successfully!")
            uploading()
        else:
            messagebox.showinfo("Unsuccessful","Wrong Password!")
            
    else:
        messagebox.showinfo("Unsuccessful","Username is not Valid!")




def register_user():
    
    username_info=username.get()
    password_info=password.get()
    file=open(username_info+".txt","w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    if username_info=="" and password_info=="":
        messagebox.showerror("Error","All fields are required")
    elif username_info=="" or username_info=="":
        messagebox.showerror("Error","All fields are required")
    else:
        messagebox.showinfo("Successful","Successfully Registered")
        uploading()


    
def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("REGISTER")
    screen1.geometry("1350x700")
    
    global username
    global password
    global username_entry
    global password_entry

    global Register_Frame
    global u_icon2
    global p_icon2
    u_icon2=PhotoImage(file="C:/Users/nikhil/Desktop/PROJECT/username_icon2.png")
    p_icon2=PhotoImage(file="C:/Users/nikhil/Desktop/PROJECT/pass_icon.png")
    
    
    username=StringVar()
    password=StringVar()

    Label(screen1,text="REGISTER",font=("times new roman",40,"bold"),bg="blue",fg="white",bd=10,relief=GROOVE).place(x=0,y=0,relwidth=1)

    
    Register_Frame=Frame(screen1)
    Register_Frame.place(x=700,y=250)


   
    Label(Register_Frame).grid(row=0,columnspan=2)







    Label(Register_Frame,text="USERNAME *",image=u_icon2,compound=LEFT,font=("times new roman",20,"bold")).grid(row=1,column=0,padx=20)
    username_entry=Entry(Register_Frame,textvariable=username)
    username_entry.grid(row=1,column=1,padx=20)


    Label(Register_Frame,text="PASSWORD *",image=p_icon2,compound=LEFT,font=("times new roman",20,"bold")).grid(row=2,column=0,padx=20)
    password_entry=Entry(Register_Frame,textvariable= password,show="*")
    password_entry.grid(row=2,column=1,padx=20)


    Button(Register_Frame,text="Register",width=15,height=1,font=("times new roman",14,"bold"),bg="blue",fg="white",command=register_user).grid(row=3,column=1,pady=10)


    screen1.attributes("-fullscreen",True)
def login():
    global screen2
    global logo 
    global user_n
    global pass_n
    global p
    global u
    global u_icon
    global p_icon
    global Login_Frame
    user_n=StringVar()
    pass_n=StringVar()
    screen2=Toplevel(screen)
    screen2.title("LOGIN")

    screen2.geometry("1350x700")
    screen2.configure(background="black")

    logo=ImageTk.PhotoImage(file="C:/Users/nikhil/Desktop/PROJECT/user_icon.jpg")
   
    
    u_icon=PhotoImage(file="C:/Users/nikhil/Desktop/PROJECT/username_icon2.png")
    p_icon=PhotoImage(file="C:/Users/nikhil/Desktop/PROJECT/pass_icon.png")


    
    Label(screen2,text="LOGIN",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE).place(x=0,y=0,relwidth=1)
    
    Login_Frame=Frame(screen2)
    Login_Frame.place(x=700,y=250)


    Label(Login_Frame,image=logo).grid(row=0,columnspan=2)


    Label(Login_Frame,text="Username",image=u_icon,compound=LEFT,font=("times new roman",20,"bold")).grid(row=1,column=0,padx=20)

    u=Entry(Login_Frame,textvariable=user_n,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)
    Label(Login_Frame,text="Password",image=p_icon,compound=LEFT,font=("times new roman",20,"bold")).grid(row=2,column=0,padx=20)                                  


    p=Entry(Login_Frame,textvariable=pass_n,bd=5,relief=GROOVE,show="*",font=("",15)).grid(row=2,column=1,padx=20)
    Button(Login_Frame,text="LOGIN",width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red",command=message).grid(row=3,column=1,pady=10)

    screen2.attributes("-fullscreen",True)
def main_screen():
    global screen
    global Main_Frame
    screen=Tk()
    screen.geometry("300x250")
    screen.title("TEXT RECOGNITION")
    '''Label(text="EXTRACT THE TEXT",bg="grey",width="300",height="2",font=("calibri",13)).place(x=0,y=0,relwidth=1)
    Label(text="").pack()'''

    Label(screen,text="EXTRACT THE TEXT",font=("times new roman",40,"bold"),bg="black",fg="white",bd=10,relief=GROOVE).place(x=0,y=0,relwidth=1)
    
    Main_Frame=Frame(screen)
    Main_Frame.place(x=700,y=250)
    
    Button(Main_Frame,text="LOGIN",height="2",width="30",font=("times new roman",14,"bold"),bg="black",fg="white",command=login).grid(row=1,column=0,padx=20)

    Label(Main_Frame,text="").grid(row=2,column=0,padx=20)

    Button(Main_Frame,text="SIGN-IN",height="2",width="30",font=("times new roman",14,"bold"),bg="black",fg="white",command=register).grid(row=3,column=0,padx=20)


    screen.attributes("-fullscreen",True)
    screen.mainloop()
    

main_screen()
