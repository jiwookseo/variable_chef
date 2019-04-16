from django import forms
from .models import Word

# # 유효성 검사
# def input_word_validator(input):
#     # if 조건
#     #   raise forms.ValidationError('한글만 입력해주세요.')

class WordModelForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['kr_word']
        widgets = {
            'kr_word': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
    # word = forms.CharField(validators=[input_word_validator])

