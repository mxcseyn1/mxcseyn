from pytube import YouTube
while True:

    link = input('enter url: ')
    yt = YouTube(link)
    high =yt.streams.get_highest_resolution()
    high.download()
    print('Dowloaded', link)
    if link == "b":
        break