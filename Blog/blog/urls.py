from django.urls import path
from .views import HomePageViews, PageDetailViews, PostCreateViews, PostUpdateViews, PostDeleteViews


urlpatterns = [

    path('post/<int:pk>/delete/', PostDeleteViews.as_view(), name='post_delete'),

    path('post/<int:pk>/edit/', PostUpdateViews.as_view(), name='post_edit'),

    path('post/new/', PostCreateViews.as_view(), name='post_new'),

    path('post/<int:pk>/', PageDetailViews.as_view(), name='post_detail'),

    path('', HomePageViews.as_view(), name='home'),
    
]