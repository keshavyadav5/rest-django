from django.urls import path
from . import views


urlpatterns = [
  path('blogs/', views.Blogsview.as_view(), name='blogs'),
  path('blogs/<int:pk>/', views.BlogDetailsView.as_view(), name='blgoDetails'),
  path('comments/', views.CommentView.as_view(), name='comments'),
  path('comments/<int:pk>/', views.CommentDetailsView.as_view(), name='commentDetails')
]