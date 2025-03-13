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
        fields = ['title', 'description']

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
