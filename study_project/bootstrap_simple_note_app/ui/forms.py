from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

from bootstrap_simple_note_app.models import SimpleNote


class CustomAuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={
            "placeholder": "Логин",
            "class": "form-control"
        })
    )
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "placeholder": "Пароль",
            "class": "form-control"
        })
    )


class CustomSignUpForm(UserCreationForm):
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control is-invalid"})
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})
    """
    pass


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class SimpleNoteForm(forms.ModelForm):

    #header = forms.CharField(label="Header", max_length=200, required=True)
    #content =  forms.CharField(label="Content", widget=forms.Textarea)

    class Meta:
        model = SimpleNote
        fields = ("header", "content", "location")
        labels = {
            "header": _("Заголовок"),
            "content": _("Содержание"),
            "location": _("Местность")
        }
        widgets = {
            "header": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
        }
