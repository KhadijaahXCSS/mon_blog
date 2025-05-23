from django import forms

class loginForm(forms.Form):
    username = forms.CharField(
        label='Nom d\'utilisateur',
        widget=forms.TextInput(attrs={
            "class": "form-control",
        }),
        max_length=100
    )
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput
                               (attrs={
            "class": "form-control",
        }))