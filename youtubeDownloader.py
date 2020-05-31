'''This program will help you in downloading youtube videos with
the help of a library called as pytube3'''
#This code is contributed by Rishabh Narayan

from pytube import *
import time

print("----------Welcome to YouTube downloader purely made in python----------\n    -------- Made by Rishabh Narayan --------")

def ytDownloader():
    url = input("Paste the YouTube video's URL here :")
    videoPath = "C:\\Users\\uday_\\Downloads"
    yt = YouTube(url)
    print("The name of the video is : ",yt.title)
    print("\n Select the format and the resolution from the following streams")
    for i in range(12):
        stream = yt.streams[i]
        print("\n",stream)
    streamIndex = int(input("Enter the index number of the stream :"))
    print(yt.streams[streamIndex])
    userChoice = input("Do you want the download to start now ? (Y / N) :")

    if userChoice == 'y' or userChoice == 'Y':
        print('Okay, your download will start in a moment')
        time.sleep(2)
        print("Download started...")
        yt.streams[streamIndex].download(videoPath)
        print("Download Completed, Check downloads")
    else:
        exit()




ytDownloader()
