from django.urls import path
from . import views

urlpatterns = [
    path('train-availability/<str:source>/<str:destination>/', views.TrainAvailability.as_view()),
    path('book-seat/<int:train_id>/', views.BookSeat.as_view()),
]
