from . import views
from django.urls import path

app_name = 'slick_service'
urlpatterns = [
    path('',views.home, name = 'home'),
    path('add_artist/',views.add_artist, name = 'add_artist'),
    path('add_album/',views.add_album, name = 'add_album'),
    path('album_detail/<artist_id>', views.album_detail_ajax, name='album_detail'),
    path('f_search/', views.f_search, name = 'f_search'),
    # edit data
    # path('update/<artist_id>/',views.update_item,name='update_item'),
    path('signup/', views.sign_up, name = 'signup'),
    path('user_login/', views.user_login, name = 'user_login'),
    path('logout/', views.user_logout, name = 'logout')
]
