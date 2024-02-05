from django import forms
from .models import Party


class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['movie_link']
        widgets = {'movie_link': forms.URLInput(attrs={'placeholder': 'movie link', 'class': 'login__input'})}
