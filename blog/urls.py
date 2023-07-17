from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='main_page'),
    path('post/<slug:slug>', views.Post.as_view(), name='post-detail'),
    path('tag/<slug:slug>', views.Tag.as_view(), name='tag-detail'),
    # path('offer/', views.post),
]
