from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="USERNAME")
    password = forms.CharField(label="PASSWORD", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="USERNAME")
    password = forms.CharField(max_length=20, label="USERNAME", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        values = {
            "username": username,
            "password": password
        }
        return values
