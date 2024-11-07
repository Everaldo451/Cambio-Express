from django import forms

class ConfigForm(forms.Form):

    email = forms.EmailField(label="email",max_length=254)
    password = forms.CharField(label="password",widget=forms.PasswordInput, required=False)
    username = forms.CharField(label="username",max_length=100)


class SetFeedbackForm(forms.Form):

    stars = forms.CharField(label="stars", max_length=1, required=True)
    comment = forms.CharField(label="comment", widget=forms.Textarea)
