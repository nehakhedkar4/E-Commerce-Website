from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import customer

class SignUpForm(UserCreationForm):
    email = forms.EmailInput()

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AddressForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
        exclude = ('user',)
        labels = {'name':'Name','locality':'Locality','city':'City','pincode':'Pincode','state':'State',}

    def __init__(self, *args, **kwargs):    
        super(AddressForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
