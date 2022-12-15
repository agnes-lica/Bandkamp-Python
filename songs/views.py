from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import Song
from .serializers import SongSerializer
from albums.models import Album

class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer
    queryset = Song.objects.all()
    lookup_url_kwarg = "pk"
   
    def perform_create(self, serializer):
        album_obj = get_object_or_404(Album, pk=self.kwargs["pk"])
        serializer.save(album=album_obj)
       