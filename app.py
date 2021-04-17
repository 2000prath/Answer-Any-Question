from flask import Flask,render_template,redirect,request
import urllib.parse
import webbrowser
from googlesearch import search 
import wikipedia
import summary
import datetime as dt
import time
import threading
import winsound

import pyttsx3
app=Flask("__name__")

def startt():
    t = dt.datetime.now()
    temp=1
    while True:
        delta = dt.datetime.now()-t
        if delta.seconds >= 40:
            frequency = 500
            duration = 500
            winsound.Beep(frequency, duration)
            time.sleep(0.5)
            winsound.Beep(frequency, duration)
            time.sleep(0.5)
            winsound.Beep(frequency, duration)
            time.sleep(0.5)
            winsound.Beep(frequency, duration)
            time.sleep(0.5)
            winsound.Beep(frequency, duration)
            time.sleep(0.5)
            
            temp=temp+1
            t = dt.datetime.now()

@app.route("/",methods=["POST","GET"])
def main():
    if request.method == "GET":
        return render_template("home.html")
    if request.method == "POST":
        text=request.form.get('question')
      
        
        
        #for j in search(text, tld="co.in", num=10, stop=5, pause=2): 
           # webbrowser.open(str(j))
            


        query = urllib.parse.quote(text)
        
        l0="https://en.wikipedia.org/w/index.php?search="+query+"&title=Special:Search&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1"
        try:
            wikip=wikipedia.summary(text, sentences=1)
        except:
            wikip="not found"
        count=0
        webbrowser.open_new("https://www.google.com/search?safe=active&sxsrf=ALeKk00jByk114c1VoSfxBk30QIauaM6VQ%3A1600787458861&ei=AhRqX5CZNKGU4-EPzN-_0Ao&q="+query)
        
        for j in search(text, tld="co.in", num=10, stop=4, pause=2): 
            
            webbrowser.open_new_tab(j)
        
            count=count+1
        return render_template("home.html",text=text,l0=l0,l1="p",wikip=wikip)

if __name__ == "__main__" :
    #threading.Thread(target=startt).start()
    app.run(debug=True)
    
    #Which of the following is Type 2 VM?
    #computing refers to applications and services that run on a distributed network using virtualized resources.