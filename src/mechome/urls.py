from django.contrib import admin
from django.urls import path,include
from ratings import views as rating_views
from dashboard import views as dashboard_views

urlpatterns = [
    path('dashboard/', dashboard_views.home_view),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('movies/', include('movies.urls')),
    path('', include('movies.urls')),
    path('rate/movie/', rating_views.rate_movie_view),
    path('resources/', include('resources.urls')),
]
