from django.contrib import admin

# Register your models here.
from .models import Lottey_Result_2PM,Lottey_Result_5PM,Stockist_Model


admin.site.register(Lottey_Result_2PM)
admin.site.register(Lottey_Result_5PM)
admin.site.register(Stockist_Model)