from django.urls import path
from . import views

urlpatterns = [
    path('courts/', views.members, name='courts'),
    path('courts/details/<int:id>', views.details, name='court_details'),
]