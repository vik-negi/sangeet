from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    # path('<int:song_id>/', views.detail, name='detail'),
    path('<int:song_id>/', views.song_details, name='song_details'),
    path('song/delete/<int:song_id>/', views.delete_song, name='song_details'),
    path('me/', views.userSongs, name='userSongs'),
    path('albums/', views.albums , name="albums"),
    path('playlist/', views.playlist, name='playlist'),
    path('playlist/<str:playlist_name>/', views.playlist_songs, name='playlist_songs'),
    path('favourite/', views.favourite, name='favourite'),
    path('songs/', views.song, name='all_songs'),
    path('recently/', views.recently, name='recent'),
    path('hindi/', views.hindiSongs, name='hindi_songs'),
    path('english/', views.englishSongs, name='english_songs'),
    path('play/<int:song_id>/', views.play_song, name='play_song'),
    path('play_song/<int:song_id>/', views.play_song_index, name='play_song_index'),
    path('play_recent_song/<int:song_id>/', views.play_recent_song, name='play_recent_song'),
    # path('home', views.homepage, name='homepage'),
]