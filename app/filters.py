import django_filters
from django.contrib.auth.models import User


class OrderFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(
        lookup_expr='startswith', label="Usuário"
        )

    class Meta:
        model = User
        fields = ['username']