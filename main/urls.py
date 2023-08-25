from django.urls import path, include
from . import views
# import api


urlpatterns = [
    path('', views.home, name='home'),
    path('<str:name>/', views.short_view, name='short'),
    path('language/<int:pk>/', views.language_view, name='language'),
    path('category/<int:pk>/', views.category_view, name='category'),
]
