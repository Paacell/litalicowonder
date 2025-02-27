# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES, label="アカウントの種類")

#     class Meta:
#         model = CustomUser
#         fields = ("username", "user_type", "password1", "password2")


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "is_student", "is_admin")
