from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Video
from .serializers import VideoSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import cv2
import threading
from django.http import StreamingHttpResponse
from django.views.decorators.http import require_GET
from django.utils.decorators import method_decorator

class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VideoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Video, id=self.kwargs['id'], user=self.request.user)

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
class VideoStreamView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @method_decorator(require_GET)
    def get(self, request, *args, **kwargs):
        video_url = self.kwargs.get('video_url')
        return StreamingHttpResponse(self.generate(video_url), content_type='multipart/x-mixed-replace; boundary=frame')

    def generate(self, video_url):
        cap = cv2.VideoCapture(video_url)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            _, jpeg = cv2.imencode('.jpg', frame)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        cap.release()
