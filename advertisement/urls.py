from django.urls import path
from . import views

urlpatterns = [
    path('' , views.IndexView.as_view() , name='index'),
    path('ad-detail/<int:pk>',views.AdDetailView.as_view(),name='ad-detail')
]