from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
from django import forms
from .models import Author, Book, Review

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        
class SearchForm(forms.Form):
    query = forms.CharField()
