from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('post/<slug:slug>', views.Post.as_view(), name='post-detail'),
    # path('tag/<slug:slug>', views.post),
    # path('offer/', views.post),
]