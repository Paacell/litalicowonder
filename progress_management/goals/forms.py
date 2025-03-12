# from django import forms
# from .models import Goal

# class GoalForm(forms.ModelForm):
#     class Meta:
#         model = Goal
#         fields = ["title", "description"]

from django import forms
from .models import Goal
from accounts.models import CustomUser

class GoalForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(is_student=True),  # 生徒アカウントのみ選択可能
        label="生徒",
    )

    class Meta:
        model = Goal
        fields = ["student", "title", "description"]
