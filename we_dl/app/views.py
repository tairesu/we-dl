from django.shortcuts import render
from .forms import Search, DlQueue
from youtube_search import YoutubeSearch
from django.http import HttpResponse
def handleSearch(req,form):
	
	context = {'error':form}
	
def index(request):
	if request.method == 'POST':
		if request.POST.__contains__('search_box'):
			form = Search(request.POST)
			if form.is_valid():
			    search_query = form.cleaned_data['search_box']
			    video_data = YoutubeSearch(search_query, max_results=5).to_dict()
			    context = {
			        'search_query': search_query,
			        'song_data': video_data,
			        'search':form,
			        'dl_queue':DlQueue()

			    }
			    return render(request, 'index.html', context)
	
		elif request.POST.__contains__('queue'):
			form = DlQueue(request.POST)
			if form.is_valid():
			    dl_list = form.cleaned_data['queue']
			    context = {
			    	
			    }
			    return HttpResponse(f"""<h3>{request.body}</h3>""")

	return render(request, 'index.html', {'search': Search(),'dl_queue':DlQueue()})

