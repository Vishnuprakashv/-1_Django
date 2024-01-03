
from django.urls import path
from . import views

app_name='book-app'

urlpatterns = [
# Path Home,Add & Display
    path("home/",views.home,name="home"),
    path("manage_store/",views.manage_store, name='manage'),
    path("display/",views.display),
# Path Update & Delete
    path("del-book/<int:id>",views.delete_book),
    path("update-book/<int:id>",views.update_book),
    path("do-update-book/<int:id>", views.do_update_book),
# Path Search
    path('search/', views.search),
]