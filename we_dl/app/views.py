from django.shortcuts import render
from .forms import MyForm
from youtube_search import YoutubeSearch

def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            selected_option = form.cleaned_data['dropdown_list']
            search_query = form.cleaned_data['search_box']
            video_data = YoutubeSearch(search_query, max_results=5).to_dict()
            context = {
                'search_query': search_query,
                'selected_option': selected_option,
                'song_data': video_data
            }
            return render(request, 'results.html', context)
    else:
        form = MyForm()
    return render(request, 'form.html', {'form': form})

