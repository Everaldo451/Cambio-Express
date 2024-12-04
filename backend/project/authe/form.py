from django import forms

class LoginForm(forms.Form):

    email = forms.EmailField(label="email",max_length=254)
    password = forms.CharField(label="password",widget=forms.PasswordInput)


class RegisterForm(forms.Form):

    email = forms.EmailField(label="email", max_length=254)
    password = forms.CharField(label="password", widget=forms.PasswordInput)


class UserRegisterExtras(forms.Form):

    full_name = forms.CharField(label="full_name", max_length=100)
   


class CompanyRegisterExtras(forms.Form):

    CNPJ = forms.CharField(label="CNPJ", max_length=14)
    name = forms.CharField(label="name", max_length=254)
    is_company = forms.CharField(label="is_company", widget=forms.RadioSelect)


class OAuthForm(forms.Form):

    code = forms.CharField(label="code", max_length=200, required=False)
    state = forms.CharField(label="state", max_length=50, required=False)
    error = forms.CharField(label="error", max_length=100, required=False)

