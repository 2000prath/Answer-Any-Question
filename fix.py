import urllib3
uri="https://www.tiktok.com/@swapatkar/video/6844097549318507777?lang=en"
uri="https://v16-web-newkey.tiktokcdn.com/5209a6f789a95266a7292592629e7b88/5f81cc97/video/tos/useast2a/tos-useast2a-ve-0068c004/a322f4dfab4d4524b85079bbb61dd3c4/?a=1988&br=844&bt=422&cr=0&cs=0&dr=0&ds=3&er=&l=202010100900270101890360232D0046F1&lr=tiktok_m&mime_type=video_mp4&qs=0&rc=MztoOXdrN3ZrdTMzZjczM0ApNzRnNWg2M2Q2NzM8OWU6M2c0aTRoMHJtcHFfLS0tMTZzczY1MWIyNDZgNTM0YTJjYzU6Yw%3D%3D&vl=&vr="

UA_CHROME = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
http = urllib3.PoolManager(10, headers={ 'User-Agent': UA_CHROME })
print("getting url data...")
r1 = http.urlopen('GET', uri)
print(r1.stream)

print(r1.data)
#outf = open('hacked1111.mkv',"wb")
#outf.write(r1.data)

#outf.close()

