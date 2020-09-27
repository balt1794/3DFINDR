from django import forms
from .models import Listing, Customer


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'condition', 'product_type', 'sale_type', 'price', 'main_photo', 'photo_1',
                  'photo_2', 'photo_3', 'photo_4', 'city', 'state', 'zipcode', 'contact_email', 'list_date']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone']
