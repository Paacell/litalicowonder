# from django import forms
# from .models import Progress

# class ProgressForm(forms.ModelForm):
#     class Meta:
#         model = Progress
#         fields = ['title', 'description']

from django import forms
from .models import Progress

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        # タイトルや概要、質問項目をフォームに含める
        fields = [
            'title',         # 進捗の見出し（例：「バグ修正完了」など）
            'description',   # 進捗の詳細説明
            'question1',     # 質問1：現在の進捗状況は？
            'question2',     # 質問2：今後の予定は？
            'question3',     # 質問3：現在の課題や問題点は？
            'question4',     # 質問4：使用したツール・技術は？
            'question5',     # 質問5：次のステップは？
            'question6',     # 質問6：その他、コメント
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '進捗タイトル'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '進捗の詳細'}),
            'question1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '例）作業の現状'}),
            'question2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '例）今後の予定'}),
            'question3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '例）現在の課題'}),
            'question4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '例）使用した技術'}),
            'question5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '例）次のステップ'}),
            'question6': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'その他コメント'}),
        }
