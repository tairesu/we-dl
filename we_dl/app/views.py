from django.shortcuts import render
from .forms import Search, DlQueue
from youtube_search import YoutubeSearch
from django.http import HttpResponse
from . import dlsong 
import json
def handleSearch(req,form):
	
	context = {'error':form}
	
def index(request):
	if request.method == 'POST':
		if request.POST.__contains__('search_box'):
			form = Search(request.POST)
			if form.is_valid():
			    search_query = form.cleaned_data['search_box']
			    video_data = YoutubeSearch(search_query, max_results=5).to_dict()
			    for song in video_data:
			    	url = song['url_suffix']
			    	song['url_suffix'] = url.split("&")[0]
			    context = {
			        'search_query': search_query,
			        'song_data': (video_data),
			        'search':form,
			        'dl_queue':DlQueue(),
			        'dl_list':''

			    }
			    return render(request, 'index.html', context)
			    #return HttpResponse(video_data)
	
		elif request.POST.__contains__('queue'):
			form = DlQueue(request.POST)
			if form.is_valid():
			    songs = form.cleaned_data['queue']
			    dl_list = json.loads(songs)
			    for song in dl_list.keys():
			    	dlsong.dl(dl_list[song]['url_suffix'])

			    context = {
			    	'dl_list': "Download Finished",
			    	'search': Search(),
			        'dl_queue':DlQueue()
			    }

			    return render(request, 'index.html', context)
	return render(request, 'index.html', {'search': Search(),'dl_queue':DlQueue()})

