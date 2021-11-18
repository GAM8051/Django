"""Platzigram URLs module"""
from django.contrib import admin
from django.urls import path
from platzigram import views as local_views
from posts import views as post_views
from users import views as users_views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    
    path("HelloWord/", local_views.hello_world, name="hello_word"),
    path("sorted/", local_views.sort_integers, name="sort"),
    path("hi/<str:name>/<int:age>/", local_views.say_hi, name="hi"),

    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
