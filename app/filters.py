import django_filters
from .models import Participacao
from django.contrib.auth.models import User
# from app.models import Participacao


class OrderFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(
        field_name='ministro__username',
        lookup_expr='istartswith'
        )

    class Meta:
        model = Participacao
        fields = ['username', 'missa']