from django import forms
from tasks.models import *


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=149,
        widget=forms.TextInput(
            attrs={
                "placeholder": "введите текст для поиска",
                "class": "form-control",
            }),
    )
    category = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

