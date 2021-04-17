import requests
import selenium
chunk_size=1000
url="https://p16-sign-sg.tiktokcdn.com/obj/tos-maliva-p-0068/9a1c26b477e143d588b48f876e9cd1be?x-expires=1602342000&amp;x-signature=6MTpdmEmDCtTMbh2o9zzgGTHcdY%3D&quot"
print("ffff")

r=requests.get(url,stream=True)
print(r)

#from pathlib import Path
#Path("downloads").mkdir(exist_ok=True) # creates folder
print("ddd")

with open('downloads/hacked222.mp4','wb') as f :
    print("ttt")
    obj=open("ff.txt","rb")
    
    
   
    for chunk in r.iter_content(chunk_size=chunk_size):
        
        f.write(chunk)
      
    