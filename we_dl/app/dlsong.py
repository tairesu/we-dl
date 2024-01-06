#Pass me a link and I will download it for you

import yt_dlp
from django.shortcuts import render
from django.http import HttpResponse

music_folder_path = "/home/tyro/music/"


def on_finish(dl):
	if(dl['status'] == 'finished'):
		message = '/nDownload Finished Converting to mp3'
def dl(url):
	ydl_opts = {
		'xyz': '%(playlist)s',
	    'format':'bestaudio/best',
	    'outtmpl':'{}%(title)s.%(ext)s'.format(music_folder_path),
	    'noplaylist': True,
	    'quiet':False,
	    'progress_hooks':[on_finish],
	    'postprocessors':[{
	        'key':'FFmpegExtractAudio',
	        'preferredcodec':'mp3',
	        'preferredquality':'192',
	        }]
	}

	# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
 # 		ydl.download(url)

