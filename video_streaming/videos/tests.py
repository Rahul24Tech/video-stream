from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Video

class VideoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.video = Video.objects.create(user=self.user, name='Test Video', video_url='http://example.com/video.mp4')

    def test_create_video(self):
        data = {'name': 'New Video', 'video_url': 'http://example.com/newvideo.mp4'}
        response = self.client.post('/api/videos/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_videos(self):
        response = self.client.get('/api/videos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_video(self):
        data = {'name': 'Updated Video', 'video_url': 'http://example.com/updatedvideo.mp4'}
        response = self.client.put(f'/api/videos/{self.video.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_video(self):
        response = self.client.delete(f'/api/videos/{self.video.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
