from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('legislations/<poll_id>/vote/', views.vote, name='vote'),
    path('legislations/<poll_id>/results/', views.results, name='results'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
