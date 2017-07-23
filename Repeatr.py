import praw;
import youtube_dl
import soundscrape
import os

reddit = praw.Reddit(client_id='rt70vub5_R-vmg', client_secret="TqM7MOpZufD2XSixb7F-LE0HOPI",
        password='12341234-12341234', user_agent='Gengar!',
        username='NexusMusic-Bot')

DLinks=[]
CloudLinks=[]
subreddit = reddit.subreddit('Techno')
for submission in subreddit.hot(limit=30):
    print("Title: ",submission.title)

    print(submission.url)

   # if "youtube" in submission.url:
   #     print("Youtube Link Found!")
   #     DLinks.append(submission.url);
   #     print(DLinks)
    if "soundcloud" in submission.url:
        print("Soundcloud Link Found!")
        CloudLinks.append(submission.url)
        print(CloudLinks)

ydl_opts = {
        'ignoreerrors':True,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(DLinks)
arglist = CloudLinks
SoundCloudDownload ="soundscrape " + str(arglist)
print(arglist)
os.system("python soundscrape.py " + " ".join(CloudLinks))


