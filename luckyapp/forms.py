from django import forms
from django.forms import ModelForm
from .models import Lottey_Result_2PM,Lottey_Result_5PM,Stockist_Model






# class DateForm(ModelForm):
#     class Meta:
#         model = Lottey_Result_2PM
#         fields = ('date',)
    
#         widget={'date_entered':forms.DateInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#         }

class StockistForm(ModelForm):
    class Meta:
        model = Stockist_Model
        fields = ('name', 'agency_name','contact_number_1','contact_number_2','email','street', 'district','state', 'pincode', 'existing_stocklist_status', 'stockist_type')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class':'form-control','required':'True'}),
            'agency_name': forms.TextInput(attrs={'placeholder': 'Agency name', 'class':'form-control','required':'True'}),
            'contact_number_1': forms.TextInput(attrs={'placeholder': 'Contact number(1)', 'class':'form-control','required':'True'}),
            'contact_number_2': forms.TextInput(attrs={'placeholder': 'Contact number(2)', 'class':'form-control','required':'True'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id', 'class':'form-control','required':'True'}),
            'street': forms.TextInput(attrs={'placeholder': 'street', 'class':'form-control','required':'True'}),
            'district': forms.TextInput(attrs={'placeholder': 'district', 'class':'form-control','required':'True'}),
            'state': forms.TextInput(attrs={'placeholder': 'state', 'class':'form-control','required':'True'}),
            'pincode': forms.TextInput(attrs={'placeholder': 'picode', 'class':'form-control','required':'True'}),
            'existing_stocklist_status': forms.Select(attrs={'placeholder': 'Are you existing stockist? ', 'class':'form-control','required':'True'}),
            'stockist_type': forms.Select(attrs={'placeholder': 'Select type ', 'class':'form-control','required':'True'}),
        }


