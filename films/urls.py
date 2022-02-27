from django.urls import path
from . import views


app_name = 'films'

urlpatterns = [
    path('', views.FilmListView.as_view(), name='all'),
    path('films/<int:pk>/detail', views.FilmDetailView.as_view(), name='film_detail'),
    path('films/create/', views.FilmCreateView.as_view(), name='film_create'),
    path('films/<int:pk>/update/', views.FilmUpdateView.as_view(), name='film_update'),
    path('films/<int:pk>/delete/', views.FilmDeleteView.as_view(), name='film_delete'),
]
