from django import forms
# from .models import Portfolio

# class PortfolioForm(forms.ModelForm):
#     class Meta:
#         model = Portfolio
#         fields = ["title", "description", "image"]

from django import forms
from .models import PortfolioProject

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = PortfolioProject
        fields = ['title', 'description', 'image', 'is_public']
