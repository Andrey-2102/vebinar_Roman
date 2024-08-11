import pytube

video_url = input("Enter YouTube video link: ")
yt = pytube.YouTube(video_url)
stream = yt.streams.Stream.get_highest_resolution()
output_path = "PATH/PATH/PATH"
stream.download(output_path)

print("Download completed!")