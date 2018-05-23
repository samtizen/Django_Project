from django import forms

from simple_post_ui_app.models import SimplePost


class SimplePostForm(forms.Form):

    header = forms.CharField(label="Header", max_length=200, required=True)
    content =  forms.CharField(label="Content", widget=forms.Textarea)


class SimplePostModelForm(forms.ModelForm):

    class Meta:
        model = SimplePost
        fields = ["id", "header", "content"]