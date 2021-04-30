from django.shortcuts import render, redirect
from slick_service.models import Artist, Album
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from .forms import album_form

# Create your views here.
@login_required()
def add_artist(request):
    if request.method == "POST":
        artist_name = request.POST.get('artist_name')
        music_style = request.POST.get('music_style')
        Artist.objects.create(artist_name=artist_name, music_style=music_style)
        return redirect('slick_service:add_album')
    else:
        return render(request, 'add_artist.html', {'msg': 'Artist'})

@login_required()
def add_album(request):
    if request.method == "POST":
        album_name = request.POST.get('album_name')
        release_date = request.POST.get('release_date')
        artist_id = request.POST.get('ref_artist')
        artists = Artist.objects.get(id = artist_id)
        Album.objects.create(album_name=album_name, release_date=release_date, get_artist=artists)
        return redirect('slick_service:home')
    else:
        return render(request, 'add_album.html', {'all_artist': Artist.objects.all(), 'msg': 'Artist successfully added!'})

def home(request):
    add_artist_ref = Artist.objects.all()
    add_album_ref = Album.objects.all()

    for artist_data in add_artist_ref:
        print("Artist_Data: ", artist_data)

    for album_data in add_album_ref:
        print("Album_Data: ",album_data)
    return render(request, 'home.html', {'artist_name': add_artist_ref, 'add_album_ref': add_album_ref} )

@login_required()
def album_detail_ajax(request, artist_id):
    if artist_id:
        artist_data =  Artist.objects.get(id=artist_id)
        # album_data = Album.objects.get(id=8)
        print(artist_data.artist_name, artist_data.music_style)
        # print(album_data.album_name, album_data.release_date, album_data.id)
    return render(request, 'album_detail.html', {'artist_data': artist_data})

def f_search(request):
    search_query = request.GET.get('s_form', None)
    if len(search_query) > 50:
        user_ref = []
    else:
        user_ref = Artist.objects.filter(artist_name__icontains=search_query)
    return render(request, 'search.html', {'user_ref':user_ref, "search_query":search_query})

# def update_item(request, artist_id):
#     artist_ref =  Artist.objects.get(id=artist_id)
#     form = artist_form(request.POST or None, instance=artist_data)

#     if form.is_valid():
#         form.save()
#         return redirect('slick_service:home')
#     return render(request, 'update.html', {'form': form, 'artist_ref': artist_ref})


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account created successfully!")
            fm.save()
    else:
        fm=SignUpForm()
    fm=SignUpForm()
    return render(request, 'signup.html', {'form': fm})

def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('slick_service:home')
    else:
        fm = AuthenticationForm()
    fm = AuthenticationForm()
    return render (request, 'user_login.html', {'form': fm})

def user_logout(request):
    logout(request)
    return redirect('slick_service:logout')