from django import forms

class LoginForm(forms.Form):

    email = forms.EmailField(label="email",max_length=254)
    password = forms.CharField(label="password",widget=forms.PasswordInput)


class RegisterForm(forms.Form):

    email = forms.EmailField(label="email", max_length=254)
    password = forms.CharField(label="password", widget=forms.PasswordInput)


class RegisterFormForUser(RegisterForm):

    full_name = forms.CharField(label="full_name", max_length=100)
   


class RegisterFormForCompany(RegisterForm):

    CNPJ = forms.CharField(label="CNPJ", max_length=14)
    name = forms.CharField(label="name", max_length=254)
    is_company = forms.CharField(label="is_company", widget=forms.RadioSelect)

