from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # removed password confirmation because this is just a test anyway
        if 'password2' in self.fields:
            del self.fields['password2']