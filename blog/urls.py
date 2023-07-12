from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('post/<slug:slug>', views.Post.as_view(), name='post-detail'),
    path('tag/<slug:slug>', views.Tag.as_view(), name='tag-detail'),
    # path('offer/', views.post),
]
