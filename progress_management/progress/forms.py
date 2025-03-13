from django import forms
from .models import Progress, SubPage

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['title', 'description1', 'description2']
        
from django import forms
from .models import Game, SubPage

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'overview', 'description1', 'description2', 'description3', 'description4', 'description5',]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description1':forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'description2':forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'description3':forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'description4':forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'description5':forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'overview':forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class SubPageForm(forms.ModelForm):
    class Meta:
        model = SubPage
        fields = ['progress_title', 'progress_detail']
        
# from django import forms
# from .models import GamePlan

# class GamePlanForm(forms.ModelForm):
#     class Meta:
#         model = GamePlan
#         fields = ['concept', 'mechanics', 'art_style', 'development_schedule']
