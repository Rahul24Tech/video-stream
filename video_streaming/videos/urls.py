from django.urls import path
from .views import VideoListCreateView, VideoRetrieveUpdateDestroyView, RegisterView, LoginView, VideoStreamView

urlpatterns = [
    path('videos/', VideoListCreateView.as_view(), name='video-list-create'),
    path('videos/<int:id>/', VideoRetrieveUpdateDestroyView.as_view(), name='video-retrieve-update-destroy'),
    path('videos/stream/<str:video_url>/', VideoStreamView.as_view(), name='video-stream'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]