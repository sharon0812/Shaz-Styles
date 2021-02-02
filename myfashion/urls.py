from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import welcome
from django.conf.urls import url

from . import views


urlpatterns = [
    path('',welcome, name='home'),
    path('search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)