from django.urls import path
from .views import ArticleListView, ArticleDetailsView
urlpatterns = [
    path('',ArticleListView.as_view()),
    path('<pk>',ArticleDetailsView.as_view()),
]
