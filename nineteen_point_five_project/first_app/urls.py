
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('add_musician/',views.AddMusicianCreateView.as_view(),name="add_musician"),
    path('add_album/',views.AddAlbumCreateView.as_view(),name="add_album"),
    path('register/',views.register,name="register"),
    path('login/',views.UserLoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page="homepage"),name="logout"),
    path('edit_musician/<int:id>',views.EditMusicianView.as_view(),name="edit_musician"),
    path('edit_album/<int:id>',views.EditAlbumView.as_view(),name="edit_album"),
    path('delete/<int:id>',views.DeleteMusicianView.as_view(),name="delete"),
]
