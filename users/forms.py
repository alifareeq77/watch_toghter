from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    password = forms.CharField(max_length=255,
                               widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'login__input'}))
    confirm_password = forms.CharField(max_length=255,
                                       widget=forms.PasswordInput(
                                           attrs={'placeholder': 'confirm password', 'class': 'login__input'}))

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password']
        widgets = {'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'login__input'})}

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'login__input'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'login__input'}))
