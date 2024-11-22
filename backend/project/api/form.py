from django import forms

class ConfigForm(forms.Form):

    email = forms.EmailField(label="email",max_length=254)
    password = forms.CharField(label="password",widget=forms.PasswordInput, required=False)
    full_name = forms.CharField(label="full_name",max_length=100)


class SetFeedbackForm(forms.Form):

    comment = forms.CharField(label="comment", widget=forms.Textarea)
