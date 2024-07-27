from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Marking email as required
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

        
        
# The below is also the way 

'''from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomRegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name",
                  "email", "username", "password1", "password2")'''