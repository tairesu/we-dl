from django import forms

class MyForm(forms.Form):
    search_box = forms.CharField(label='Search')
    dropdown_list = forms.ChoiceField(choices=[
        ('youtube', 'Youtube'),
        ('spotify', 'Spotify'),
        ('shazam', 'Shazam'),
        ('mixcloud','Mixcloud')
    ])