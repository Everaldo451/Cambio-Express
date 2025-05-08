from django import forms
from api.models import CODE_CHOICES

class PostAccountForm(forms.Form):
    code = forms.ChoiceField(label="code", choices=CODE_CHOICES)


