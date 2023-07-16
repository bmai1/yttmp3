# pip install pytube

# importing packages
from pytube import YouTube
import os
import sys
  
def convert_youtube_url(url):
    # url input from user
    yt = YouTube(str(url))

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    
    # config destination
    destination = 'mp3files'
    
    # download the file
    out_file = video.download(output_path=destination)
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")

if __name__ == '__main__':
    # Check if a URL argument is provided
    if len(sys.argv) > 1:
        url = sys.argv[1]
        convert_youtube_url(url)
    else:
        print("No YouTube URL provided.")

    
