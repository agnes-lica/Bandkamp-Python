from .models import Album
from .serializers import AlbumSerializer
from rest_framework import generics

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AlbumView(generics.ListCreateAPIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    lookup_url_kwarg = "pk"
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        