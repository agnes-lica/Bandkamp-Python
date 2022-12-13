from rest_framework.views import Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner

from utils.common_Views import PostCommonView
from utils.detail_common_views import GetPatchDeleteDetailView

class UserView(PostCommonView):
    view_serializer = UserSerializer


class UserDetailView(GetPatchDeleteDetailView):

    view_serializer = UserSerializer
    view_queryset = User.objects.all()
    url_param_name = "pk"