from django import forms
from .models import GamePlan, Task, Feedback

class GamePlanForm(forms.ModelForm):
    class Meta:
        model = GamePlan
        fields = ['title', 'description1', 'description2', 'description3', 'description4', 'description5', 'image']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'フィードバックを入力してください'}),
        }
