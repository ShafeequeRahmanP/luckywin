import django_filters
from .models import *
from django_filters import DateFilter


class LotteryFilter(django_filters.FilterSet):
    class Meta:
        model = Lottey_Result_2PM
        fileds = '__all__'