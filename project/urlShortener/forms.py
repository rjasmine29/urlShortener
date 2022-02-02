from django import forms
from .models import Shortener
class ShortenerForm(forms.ModelForm):
    originalURL = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Type your URL to shorten"}))
    class Meta:
        model = Shortener

        fields = ('originalURL',)
