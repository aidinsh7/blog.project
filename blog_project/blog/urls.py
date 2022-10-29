from django.urls import include, path

from .views import ArticleList

name='blog'

urlpatterns = [
    path('',ArticleList.as_view(),name='list' ),
    path('<int:pk>',ArticleList.as_view(),name="detail"),
]
