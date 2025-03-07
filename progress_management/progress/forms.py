from django import forms
from .models import Progress

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['title', 'description']

# from django import forms
# from .models import Progress

# class ProgressForm(forms.ModelForm):
#     class Meta:
#         model = Progress
#         fields = [
#             'title', 
#             'description', 
#             'question1', 
#             'question2', 
#             'question3', 
#             'question4', 
#             'question5', 
#             'question6'
#         ]
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '進捗タイトル'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '進捗の詳細'}),
#             'question1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '現在の進捗状況は？'}),
#             'question2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '今後の予定は？'}),
#             'question3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '現在の課題や問題点は？'}),
#             'question4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '使用したツール・技術は？'}),
#             'question5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '次のステップは？'}),
#             'question6': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'その他コメント'}),
#         }
