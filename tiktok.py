import re



def Find(text): 
    
    # findall() has been used  
    # with valid conditions for urls in string 
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,text)
    
    
    url=re.findall(regex, text)
       
    return [x[0] for x in url] 
      
# Driver Code 
data=open("text.txt",encoding="utf-8")
text=data.read()
#text="https://www.tiktokfffff.com/@swapatkar/video/6844106037922893057 is the https://www.tiktok.com/@swapatkar/video/6844106037922893059 and https://www.tiktok.com/@swapatkar/video/68441060379228930500 end"

print("Urls: ", Find(text)) 

