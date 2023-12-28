from django import forms

class Search(forms.Form):
    search_box = forms.CharField(label='Search')

class DlQueue(forms.Form):
	queue = forms.CharField(label='Queue')