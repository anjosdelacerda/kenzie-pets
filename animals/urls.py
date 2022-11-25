from django.urls import path

from . import views

urlpatterns = [
    path('animals/', views.AnimalViews.as_view()),
    path('animals/<int:animal_id>/', views.AnimalDetailViews.as_view()),
]
