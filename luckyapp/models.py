from django.db import models

# # Create your models here.
# class Stockistship(models.Model):
#     name = models.CharField(max_length=20)
#     agency_name = models.CharField(max_length=20)
#     contact_number1 = models.CharField(max_length = 10)
#     contact_number2 = models.CharField(max_length = 10)
#     email = models.EmailField()
#     street = models.TextField()
#     state = models.TextField()
#     def __str__(self):
#         return self.name
STATUS_CHOICES = (
    ('Y', 'YES'),
    ('N', 'NO'),
)

STOCKIST_TYPE = (
    ('S', 'STOCKIST'),
    ('SS', 'SUB-STOCKIST'),
    ('SE', 'SELLER'),

)


class Lottey_Result_2PM(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    first_price = models.CharField(max_length = 10)
    second_price = models.CharField(max_length = 70)
    third_price = models.CharField(max_length = 70)
    fourth_price = models.CharField(max_length = 70)
    fifth_price = models.CharField(max_length = 70)
    sixth_price = models.TextField(max_length = 600)




class Lottey_Result_5PM(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    first_price = models.CharField(max_length = 10)
    second_price = models.CharField(max_length = 70)
    third_price = models.CharField(max_length = 70)
    fourth_price = models.CharField(max_length = 70)
    fifth_price = models.CharField(max_length = 70)
    sixth_price = models.TextField(max_length = 600)


class Stockist_Model(models.Model):
    name = models.CharField(max_length = 10)
    agency_name = models.CharField(max_length = 20)
    contact_number_1 = models.CharField(max_length = 10)
    contact_number_2 = models.CharField(max_length = 10)
    email = models.EmailField()
    street = models.CharField(max_length = 50)
    state = models.CharField(max_length = 20)
    district = models.CharField(max_length = 20)
    pincode = models.CharField(max_length = 6)
    existing_stocklist_status = models.CharField(choices = STATUS_CHOICES, max_length = 1)
    stockist_type = models.CharField(max_length = 2, choices = STOCKIST_TYPE)
    def __str__(self):
        return self.name

        
class Date_Search(models.Model):
    date_entered = models.DateField()

    
    


    
