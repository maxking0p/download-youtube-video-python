from pytube import YouTube

url ="https://youtu.be/GrAchTdepsU"

video = YouTube(url)
stream = video.streams.get_highest_resolution()

stream.download(output_path= 'D:/')
