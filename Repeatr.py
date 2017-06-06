import praw;
import youtube_dl

reddit = praw.Reddit(client_id='rt70vub5_R-vmg', client_secret="TqM7MOpZufD2XSixb7F-LE0HOPI",
        password='12341234-12341234', user_agent='Gengar!',
        username='NexusMusic-Bot')

DLinks=[]
subreddit = reddit.subreddit('khiphop')
for submission in subreddit.hot(limit=30):
    print("Title: ",submission.title)

    print(submission.url)

    if "youtube" in submission.url:
        print("Link Found!")
        DLinks.append(submission.url);
        print(DLinks)

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
