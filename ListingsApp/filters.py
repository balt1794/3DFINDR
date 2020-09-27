import django_filters
from django_filters import CharFilter
from .models import Listing


class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = ['condition', 'city', 'state']
