from django import forms
from .models import Progress, SubPage

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['title', 'description']
        
class SubPageForm(forms.ModelForm):
    class Meta:
        model = SubPage
        fields = ['title', 'design_document', 'progress_note']
