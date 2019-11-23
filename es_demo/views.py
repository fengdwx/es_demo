from drf_haystack.viewsets import HaystackViewSet
from .models import User
from .serializers import UserIndexSerializer, UserSerializer
from rest_framework import viewsets


class UserSearchViewSet(HaystackViewSet):
    """
    User search
    """
    index_models = [User]
    serializer_class = UserIndexSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
