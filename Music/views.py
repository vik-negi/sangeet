from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    #Display recent songs
    if not request.user.is_anonymous :
        recent = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
        recent_id = [each['song_id'] for each in recent]
        recent_id = recent_id if len(recent_id) < 10 else recent_id[:10]
        recentlyPlayed_unsorted = Song.objects.filter(id__in=recent_id,recent__user=request.user)
        recentlyPlayed = list()
        for id in recent_id:
            recentlyPlayed.append(recentlyPlayed_unsorted.get(id=id))
        if recent:
            last_played_id = recent[0]['song_id']
            last_played_song = Song.objects.get(id=last_played_id)
    else:
        recent = None
        recentlyPlayed = None
        last_played_song = None

    #Display all songs
    songs = Song.objects.all()
    qs_singers = Song.objects.values_list('singer').all()
    s_list = [s.split(',') for singer in qs_singers for s in singer]
    singers = sorted(list(set([s.strip() for singer in s_list for s in singer])))
    qs_languages = Song.objects.values_list('language').all()
    languages = sorted(list(set([l.strip() for lang in qs_languages for l in lang])))

    #Display few songs on home page
    songs_all = list(Song.objects.all().values('id').order_by('?'))
    sliced_ids = [each['id'] for each in songs_all][:5]
    indexpage_songs = Song.objects.filter(id__in=sliced_ids)

    # For Hindi Songs
    songs_hindi = list(Song.objects.filter(language='Hindi').values('id'))
    sliced_ids = [each['id'] for each in songs_hindi][:]
    indexpage_hindiSongs = Song.objects.filter(id__in=sliced_ids)

    # For English Songs
    songs_english = list(Song.objects.filter(language='English').values('id'))
    sliced_ids = [each['id'] for each in songs_english][:]
    indexpage_englishSongs = Song.objects.filter(id__in=sliced_ids)

    # For Korean Songs
    korean_songs = list(Song.objects.filter(language='korean').values('id'))
    sliced_ids = [each['id'] for each in korean_songs][:]
    KoreanSongs = Song.objects.filter(id__in=sliced_ids)

    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        filtered_songs = songs.filter(Q(name__icontains=search_query)).distinct()
        # context = {'allSongs': filtered_songs,'last_played':last_played_song,'query_search':True}
        context = {'allSongs': filtered_songs,'query_search':True}

        return render(request, 'Music/index.html', context)
    context = {
        'allSongs':indexpage_songs,
        'recentlyPlayed': recentlyPlayed,
        'hindiSongs':indexpage_hindiSongs,
        'englishSongs':indexpage_englishSongs,
        'koreanSongs': KoreanSongs,
        'last_played':last_played_song,
        # 'newUser': newUser,
        'singers': singers,
        'languages': languages,
        'query_search':False,
    }
    return render(request, 'Music/index.html', context=context)


def hindiSongs(request):
    hindiSongs = Song.objects.filter(language='Hindi')
    #Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=7)

    query = request.GET.get('q')

    if query:
        hindiSongs = Song.objects.filter(Q(name__icontains=query)).distinct()
        context = {'hindiSongs': hindiSongs}
        return render(request, 'Music/hindiSongs.html', context)

    context = {'hindiSongs':hindiSongs,'last_played':last_played_song}
    return render(request, 'Music/hindi.html',context=context)


def englishSongs(request):

    englishSongs = Song.objects.filter(language='English')

    #Last played song
    # last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    # if last_played_list:
    #     last_played_id = last_played_list[0]['song_id']
    #     last_played_song = Song.objects.get(id=last_played_id)
    # else:
    #     last_played_song = Song.objects.get(id=7)
    #     last_played_song = None
    query = request.GET.get('q')

    if query:
        englishSongs = Song.objects.filter(Q(name__icontains=query)).distinct()
        context = {'englishSongs': englishSongs}
        return render(request, 'Music/englishSongs.html', context)

    # context = {'englishSongs':englishSongs,'last_played':last_played_song}
    context = {'englishSongs':englishSongs}

    return render(request, 'Music/english.html',context=context)
    # return HttpResponse("<h2>hello</h2>", englishSongs[0].name)


def albums(request):
    songs_list = Song.objects.all()
    return render(request, 'Music/albums.html', context={"song_list": songs_list})

@login_required(login_url='login')
def play_song(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    # Add data to recent database
    if list(Recent.objects.filter(song=songs,user=request.user).values()):
        data = Recent.objects.filter(song=songs,user=request.user)
        data.delete()
    data = Recent(song=songs,user=request.user)
    data.save()
    return redirect('songs')


@login_required(login_url='login')
def play_song_index(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    if list(Recent.objects.filter(song=songs,user=request.user).values()):
        data = Recent.objects.filter(song=songs,user=request.user)
        data.delete()
    data = Recent(song=songs,user=request.user)
    data.save()
    return redirect('index')

@login_required(login_url='login')
def play_recent_song(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    # Add data to recent database
    if list(Recent.objects.filter(song=songs,user=request.user).values()):
        data = Recent.objects.filter(song=songs,user=request.user)
        data.delete()
    data = Recent(song=songs,user=request.user)
    data.save()
    return redirect('recently')


def song(request):
    songs = Song.objects.all()
    newUser = False
    #Last played song
    if not request.user.is_anonymous:
        last_played_list = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
        if last_played_list:
            last_played_id = last_played_list[0]['song_id']
            last_played_song = Song.objects.get(id=last_played_id)
        else:
            last_played_song = None
    else:
        newUser = True
        last_played_song = None

    
    # apply search filters
    print(request.GET)
    qs_singers = Song.objects.values_list('singer').all()
    s_list = [s.split(',') for singer in qs_singers for s in singer]
    singers = sorted(list(set([s.strip() for singer in s_list for s in singer])))
    qs_languages = Song.objects.values_list('language').all()
    languages = sorted(list(set([l.strip() for lang in qs_languages for l in lang])))
    
    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        search_singer = request.GET.get('singers') or ''
        search_language = request.GET.get('languages') or ''
        filtered_songs = songs.filter(Q(name__icontains=search_query)).filter(Q(language__icontains=search_language)).filter(Q(singer__icontains=search_singer)).distinct()
        context = {
        'songs': filtered_songs,
        'last_played':last_played_song,
        'singers': singers,
        'languages': languages,
        'query_search': True,
        }
        return render(request, 'Music/search_result.html', context)

    context = {
        'songs': songs,
        'last_played':last_played_song,
        'newUser':newUser,
        'singers': singers,
        'languages': languages,
        'query_search' : False,
        }
    return render(request, 'Music/search_result.html', context=context)


def recently(request):
    
    #Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=7)

    #Display recent songs
    recent = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
    if recent and not request.user.is_anonymous :
        recent_id = [each['song_id'] for each in recent]
        recentlyPlayed_unsorted = Song.objects.filter(id__in=recent_id,recent__user=request.user)
        recentlyPlayed = list()
        for id in recent_id:
            recentlyPlayed.append(recentlyPlayed_unsorted.get(id=id))
    else:
        recentlyPlayed = None

    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        filtered_songs = recentlyPlayed_unsorted.filter(Q(name__icontains=search_query)).distinct()
        context = {'recentlyPlayed': filtered_songs,'last_played':last_played_song,'query_search':True}
        return render(request, 'Music/recently.html', context)

    context = {'recentlyPlayed':recentlyPlayed,'last_played':last_played_song,'query_search':False}
    return render(request, 'Music/recently.html', context=context)


@login_required(login_url='login')
def detail(request, song_id):
    songs = Song.objects.filter(id=song_id).first()

    # Add data to recent database
    if list(Recent.objects.filter(song=songs,user=request.user).values()):
        data = Recent.objects.filter(song=songs,user=request.user)
        data.delete()
    data = Recent(song=songs,user=request.user)
    data.save()

    #Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=7)


    playlists = Playlist.objects.filter(user=request.user).values('playlist_name').distinct
    is_favourite = Favourite.objects.filter(user=request.user).filter(song=song_id).values('is_fav')

    if request.method == "POST":
        if 'playlist' in request.POST:
            playlist_name = request.POST["playlist"]
            q = Playlist(user=request.user, song=songs, playlist_name=playlist_name)
            q.save()
            messages.success(request, "Song added to playlist!")
        elif 'add-fav' in request.POST:
            is_fav = True
            query = Favourite(user=request.user, song=songs, is_fav=is_fav)
            print(f'query: {query}')
            query.save()
            messages.success(request, "Added to favorite!")
            return redirect('details', song_id=song_id)
        elif 'rm-fav' in request.POST:
            is_fav = True
            query = Favourite.objects.filter(user=request.user, song=songs, is_fav=is_fav)
            print(f'user: {request.user}')
            print(f'song: {songs.id} - {songs}')
            print(f'query: {query}')
            query.delete()
            messages.success(request, "Removed from favorite!")
            return redirect('detail', song_id=song_id)

    context = {'songs': songs, 'playlists': playlists, 'is_favourite': is_favourite,'last_played':last_played_song}
    return render(request, 'Music/details.html', context=context)

@login_required(login_url='login')
def song_details(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    song_detail = Song.objects.filter(id=song_id).values().first()
    print(f'songs: {song}')

    # Add data to recent database
    if list(Recent.objects.filter(song=songs,user=request.user).values()):
        data = Recent.objects.filter(song=songs, user=request.user)
        data.delete()
    data = Recent(song=songs,user=request.user)
    data.save()

    #Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=7)


    playlists = Playlist.objects.filter(user=request.user).values('playlistName').distinct
    # is_favourite = Favourite.objects.filter(user=request.user).filter(song=song_id).values('is_fav')

    if request.method == "POST":
        if 'playlist' in request.POST:
            playlist_name = request.POST["playlist"]
            q = Playlist(user=request.user, song=songs, playlist_name=playlist_name)
            q.save()
            messages.success(request, "Song added to playlist!")
        # elif 'add-fav' in request.POST:
        #     is_fav = True
        #     query = Favourite(user=request.user, song=songs, is_fav=is_fav)
        #     print(f'query: {query}')
        #     query.save()
        #     messages.success(request, "Added to favorite!")
        #     return redirect('details', song_id=song_id)
        # elif 'rm-fav' in request.POST:
        #     is_fav = True
        #     query = Favourite.objects.filter(user=request.user, song=songs, is_fav=is_fav)
        #     print(f'user: {request.user}')
        #     print(f'song: {songs.id} - {songs}')
        #     print(f'query: {query}')
        #     query.delete()
        #     messages.success(request, "Removed from favorite!")
        #     return redirect('detail', song_id=song_id)

    context = {'album': song_detail, 'playlists': playlists, 'is_favourite': "is_favourite",'last_played':last_played_song}
    return render(request, 'Music/song_details.html', context=context)


@login_required
def delete_song(request, id):
    if request.method == 'POST':
        song = Song.objects.get(song_id = id)
        song.delete()
        return redirect('songs')

def userSongs(request):
    return render(request, 'Music/userSongs.html')


def playlist(request):
    playlists = Playlist.objects.filter(user=request.ser).values('playlist_name').distinct
    context = {'playlists': playlists}
    return render(request, 'Music/playlists.html', context=context)


def playlist_songs(request, playlist_name):
    songs = Song.objects.filter(playlist__playlist_name=playlist_name, playlist__user=request.user).distinct()

    if request.method == "POST":
        song_id = list(request.POST.keys())[1]
        playlist_song = Playlist.objects.filter(playlist_name=playlist_name, song__id=song_id, user=request.user)
        playlist_song.delete()
        messages.success(request, "Song removed from playlist!")

    context = {'playlist_name': playlist_name, 'songs': songs}

    return render(request, 'Music/playlistSongs.html', context=context)


def favourite(request):
    songs = Song.objects.filter(favourite__user=request.user, favourite__is_fav=True).distinct()
    print(f'songs: {songs}')
    
    if request.method == "POST":
        song_id = list(request.POST.keys())[1]
        favourite_song = Favourite.objects.filter(user=request.user, song__id=song_id, is_fav=True)
        favourite_song.delete()
        messages.success(request, "Removed from favourite!")
    context = {'songs': songs}
    return render(request, 'Music/favourites.html', context=context)

    