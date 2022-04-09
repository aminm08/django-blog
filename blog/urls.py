from django.urls import path

from . import views

urlpatterns = [
    path('',views.ShowListView.as_view(),name='blog list'),
    path('<int:pk>/',views.ShowDetail.as_view(),name='detail_view'),
    path('addpost/',views.AddPostView.as_view(),name='add post'),
    path('<int:pk>/edit/',views.EditPost.as_view(),name='edit post'),
    path('<int:pk>/delete/',views.Deletpost.as_view(),name='delete post'),
]