from django.urls import path

from . import views

urlpatterns = [
    path('blogpost/', views.BlogPostCreateView.as_view()),
    path('blogpost/<int:id>/', views.BlogPostView.as_view()),
    path('blogpost/<int:blog_id>/attachment_list/', views.BlogPostAttachmentListView.as_view()),
    path('blogpost/<int:blog_id>/attachment_upload/', views.BlogPostAttachmentUploadView.as_view()),
    path('attachments/<uuid:attachment_id>/', views.BlogPostAttachmentDeleteView.as_view()),
    path('blogpost/<int:id>/header/', views.BlogPostHeaderView.as_view()),
    path('blogposts/', views.BlogPostListView.as_view()),
    path('categories/', views.BlogPostCategoryListView.as_view()),
    path('tags/', views.BlogPostTagListView.as_view()),
    path('<int:id>/comment/', views.BlogPostCommentCreateView.as_view()),
    path('comment/<int:id>/', views.BlogPostCommentUpdateView.as_view()),
]
