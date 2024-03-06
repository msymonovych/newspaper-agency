from django import forms
from django.contrib.auth.forms import UserCreationForm

from newspaper.models import News, Redactor


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )
