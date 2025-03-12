from django import forms
from .models import Progress, SubPage

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['title', 'description']
        
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