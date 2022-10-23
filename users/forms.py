#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sulaiman maryam
#
# Created:     23-05-2020
# Copyright:   (c) sulaiman maryam 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from django import forms
from users.models import User, SellerProfile, BuyerProfile, ShelfFlags
from inventory.models import ShelfOne, ShelfTwo, ShelfThree, ShelfFour, ShelfFive
from django_countries.fields import CountryField
from django.contrib.auth.forms import UserCreationForm
from django_countries.widgets import CountrySelectWidget
import phonenumbers
from phonenumbers import carrier

class BuyerRegisterForm(UserCreationForm):
    is_buyer=forms.BooleanField(label_suffix='(keep this field checked)',initial=True)
    email= forms.EmailField()
    first_name= forms.CharField(required=True)
    last_name= forms.CharField(required=True)
    base_country= CountryField(blank_label='(select country)').formfield()
    mobile_number = forms.IntegerField()
    address=forms.CharField(required=True)
    address2=forms.CharField(empty_value='optional',required=False)
    city=forms.CharField(max_length=100,required=True,)


    class Meta:
        model= User
        fields= ['is_buyer','username','first_name', 'last_name' , 'email','base_country', 'city', 'mobile_number','address','address2','password1','password2']
        widgets = {'base_country':CountrySelectWidget()}





class SellerRegisterForm(UserCreationForm):
    is_seller=forms.BooleanField(label_suffix='(keep this field checked)',initial=True)
    email= forms.EmailField(required=True)
    first_name= forms.CharField(required=True)
    last_name= forms.CharField(required=True)
    store_name= forms.CharField(required=True, max_length=85)
    mobile_number= forms.IntegerField(required=True)
    address= forms.CharField(required=True)
    address2=forms.CharField(empty_value='optional',required=False)
    base_country= CountryField(blank_label='select country').formfield()
    city = forms.CharField(max_length=100, required=True)


    class Meta:
        model= User
        fields= ['is_seller','username', 'first_name', 'last_name','store_name', 'email','base_country', 'city', 'mobile_number','address','address2','password1','password2']
        widgets = {'base_country':CountrySelectWidget()}


class ShelfOneUpdateForm(forms.ModelForm):
    class Meta:
        model=ShelfOne
        fields = ['image','shelf_name', 'shelf_category']


class ShelfTwoUpdateForm(forms.ModelForm):
    class Meta:
        model=ShelfTwo
        fields = ['image','shelf_name', 'shelf_category']

class ShelfThreeUpdateForm(forms.ModelForm):
    class Meta:
        model=ShelfThree
        fields = ['image','shelf_name', 'shelf_category']

class ShelfFourUpdateForm(forms.ModelForm):
    class Meta:
        model=ShelfFour
        fields = ['image','shelf_name', 'shelf_category']


class ShelfFiveUpdateForm(forms.ModelForm):
    class Meta:
        model=ShelfFive
        fields = ['image','shelf_name', 'shelf_category']



class UserUpdateForm(forms.ModelForm):
    address2=forms.CharField(empty_value='optional',required=False)
    class Meta:
        model = User
        fields = ['store_name','image','username','email', 'city','mobile_number','address','address2']

class SellerProfileUpdateForm(forms.ModelForm):
    operating_countries=CountryField('Operating_Countries     (hold ctrl key to select multiple countries or leave empty to be set as all) ', multiple=True).formfield(required=False)
    class Meta:
        model = SellerProfile
        fields= ['store_payment_method','operating_countries','about_store']


class BuyerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = BuyerProfile
        fields = []

