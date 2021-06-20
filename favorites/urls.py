from django.urls import path
from .views import FavoriteList,FavoriteDetail

urlpatterns = [
    path('',FavoriteList.as_view(),name='favorite_list'),
    path('<int:pk>/',FavoriteDetail.as_view(),name='favorite_detail')
]