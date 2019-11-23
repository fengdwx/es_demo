from drf_haystack.serializers import HaystackSerializer
from .search_indexes import UserIndex
from rest_framework import serializers
from .models import User


class UserIndexSerializer(HaystackSerializer):
    """
    User index result serializer
    """
    class Meta:
        index_classes = [UserIndex]
        fields = ('username', 'first_name', 'last_name', 'address', 'birthday', 'description')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'address', 'birthday', 'description')
