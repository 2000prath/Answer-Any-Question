import wget
url="https://v16-web-newkey.tiktokcdn.com/5209a6f789a95266a7292592629e7b88/5f81cc97/video/tos/useast2a/tos-useast2a-ve-0068c004/a322f4dfab4d4524b85079bbb61dd3c4/?a=1988&amp;br=844&amp;bt=422&amp;cr=0&amp;cs=0&amp;dr=0&amp;ds=3&amp;er=&amp;l=202010100900270101890360232D0046F1&amp;lr=tiktok_m&amp;mime_type=video_mp4&amp;qs=0&amp;rc=MztoOXdrN3ZrdTMzZjczM0ApNzRnNWg2M2Q2NzM8OWU6M2c0aTRoMHJtcHFfLS0tMTZzczY1MWIyNDZgNTM0YTJjYzU6Yw%3D%3D&amp;vl=&amp;vr="
filename = wget.download(url)



print("done")