from django import forms
# from .models import Artist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email Adress'}
# class artist_form(forms.ModelForm):
#     class Meta:
#         model=Artist
#         fields = ['artist_name', 'music_style']

    # artist_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter name...'}))
    # music_style = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter music type...'}))
    # album_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter album name...'}))
    # release_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    # get_artist = models.ForeignKey(Artist, on_delete = models.CASCADE)