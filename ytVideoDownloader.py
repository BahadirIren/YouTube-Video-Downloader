from pytube import YouTube
from pytube.cli import on_progress
import ffmpeg
import os

downloadPath = '/Users/bahadir/Downloads'


def combine_audio(fileName):
    print('\nAudio and video files are being merged...')
    input_video = ffmpeg.input(downloadPath + '/.v.mp4')

    input_audio = ffmpeg.input(downloadPath + '/.a.mp4')

    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(
        downloadPath + '/'+fileName + '.mp4').run(quiet=True)

    os.remove(downloadPath + '/.v.mp4')
    os.remove(downloadPath + '/.a.mp4')
    print('Completed')


ytLink = input("Enter YouTube url: ")
yt = YouTube(ytLink, on_progress_callback=on_progress)

try:
    video = yt.streams.filter(
        resolution="1080p", mime_type="video/mp4").first()
    fileName = video.title

    video.download(
        downloadPath, ".v.mp4")
    audio = yt.streams.filter(only_audio=True).first().download(
        downloadPath, ".a.mp4")

    combine_audio(fileName)
except:
    video = yt.streams.get_highest_resolution()
    video.download(downloadPath)
