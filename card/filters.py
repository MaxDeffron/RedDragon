import django_filters

from .models import Product


class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['manufacturer']

class SearchClientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Поиск')
    class Meta:
        model = Product
        fields = ['name']

#fields = ['processor', 'videomemory', 'power', 'price', 'manufacturer']