from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import Songs_static, Songs, Playlist
from django.db.models import F
from django.contrib.auth.decorators import login_required

def login(request):
    return render_to_response('login.html')


def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username = username, password = password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/index')
    else:
        return HttpResponse('NOT AUTHORIZED')


def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('login.html')
    args= {}
    args['form'] = UserCreationForm()
    return render_to_response('register.html',args)


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


@login_required(login_url="/login/")
def index(request):
    num=request.REQUEST.get("id",None)
    album_list=Songs_static.objects.all()
    songs_list=[]
    if num:
        songs_list=Songs.objects.filter(static_id=num)

    return render_to_response('index.html',{'a':album_list,'b':songs_list,'num':num})


@login_required(login_url="/login/")
def add_playlist(request):
    uid=request.user
    static_id=request.GET.get('num',None)
    all_songs = Songs.objects.filter(static_id=static_id)
    selected_song_list=[]
    for song in all_songs:
        if (request.REQUEST.get(song.song_track,None)):
            selected_song_list.append(song)
    for sid in selected_song_list:
        playlist_object= Playlist.objects.create(u_id=uid,s_id=sid)


@login_required(login_url="/login/")
def playlist(request):
    user = request.user
    sids = list()
    user_playlist = Playlist.objects.filter(u_id = user)
    for sid in user_playlist:
        sids.append(sid.s_id_id)
    user_playlist = Songs.objects.filter(id__in = sids).order_by('-song_hits')
    return render_to_response('playlist.html',{'playlist':user_playlist})


@login_required(login_url="/login/")
def route(request):
    try:
        if(request.GET.get('button') == 'BUY'):
            buy(request)
        else:
            add_playlist(request)
    except:
        return HttpResponse('Please select some song first')
    return HttpResponseRedirect('/index')
        

@login_required(login_url="/login/")
def buy(request):
    static_id=request.GET.get('num',None)
    all_songs = Songs.objects.filter(static_id=static_id)
    selected_song_list=[]
    for song in all_songs:
        if (request.REQUEST.get(song.song_track,None)):
            selected_song_list.append(song.id)
    for sid in selected_song_list:
        playlist_object= Songs.objects.filter(id__in = selected_song_list).update(song_hits = F('song_hits')+1)


@login_required(login_url="/login/")
def dashboard(request):
    if (request.GET):
        dct = request.GET.keys()
        songs_list1 = Songs.objects.filter(song_genre__in =  dct).order_by('-song_hits','song_genre')
    else:
        songs_list = Songs.objects.order_by('-song_hits','song_genre')
    genres = list()
    genres1 = list()
    genres = Songs.objects.distinct('song_genre')
    for i in genres:
        genres1.append(i.song_genre)
    genres = set(genres1)
    try:
        songs_list = songs_list1;
    except: pass
    return render_to_response('dashboard.html',{'a':songs_list,'b':genres})
