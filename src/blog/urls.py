from django.urls import path
from . import views


urlpatterns = [
    path('',views.PostList.as_view(), name='post_list'),
    path('draft',views.PostDraftList.as_view(), name='post_draft_list'),
    path('archived',views.PostArchivedList.as_view(), name='post_archived_list'),
    path('post/new/', views.CreatePost.as_view(), name='post_new'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', views.PostDelete.as_view(), name='post_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/archive/', views.post_archive, name='post_archive'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('user/new/', views.CreateUser.as_view(), name='new_user'),
]