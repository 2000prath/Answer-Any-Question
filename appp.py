from flask import Flask,render_template,redirect,request
import urllib.parse
import webbrowser
from googlesearch import search 
import winsound

import datetime as dt
import time
import threading
app=Flask("__name__")

def startt():
    t = dt.datetime.now()

    while True:
        delta = dt.datetime.now()-t
        if delta.seconds >= 5:
            frequency = 500
            duration = 2000 
            winsound.Beep(frequency, duration)
            time.sleep(2)
            winsound.Beep(frequency, duration)
            time.sleep(3)
            winsound.Beep(frequency, duration)
            time.sleep(4)

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

            t = dt.datetime.now()


@app.route("/",methods=["POST","GET"])
def main():
    
    if request.method == "GET":
        return render_template("home.html")
    if request.method == "POST":

        text=request.form.get('question')
        query = urllib.parse.quote(text)
        searchq=list()
        
        count=0
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 2000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        
        webbrowser.open_new("https://www.google.com/search?safe=active&sxsrf=ALeKk00jByk114c1VoSfxBk30QIauaM6VQ%3A1600787458861&ei=AhRqX5CZNKGU4-EPzN-_0Ao&q="+query)
        
        for j in search(text, tld="co.in", num=10, stop=4, pause=2): 
            searchq.append(str(j))
            #webbrowser.open_new_tab(j)
            print(j)
            count=count+1
        
        
        return render_template("home.html",text=text)


#l0=searchq[0],l1=searchq[1],l2=searchq[2],l3=searchq[3],l4=searchq[4]
if __name__ == "__main__" :
    threading.Thread(target=startt).start()
    
    app.run(debug=True)s