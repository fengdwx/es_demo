from haystack import indexes
from .models import User
import datetime


class UserIndex(indexes.SearchIndex, indexes.Indexable):
    """
    User索引类
    """

    # text represents the field being queried, and the user searches for the values of these fields.
    text = indexes.CharField(document=True, use_template=True)

    first_name = indexes.CharField(model_attr='first_name')
    username = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')
    address = indexes.CharField(model_attr='address')
    description = indexes.CharField(model_attr='address')
    birthday = indexes.DateField(model_attr='birthday')

    def get_model(self):
        """Return to the indexed model class"""
        return User

    def index_queryset(self, using=None):
        """Returns the data query set to be indexed"""
        # return self.get_model().objects.filter(username__contains=self.request.GET.get('text'))
        return self.get_model().objects.filter(birthday__lte=datetime.date.today())
