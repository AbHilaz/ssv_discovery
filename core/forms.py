from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class StudentProfileForm(forms.ModelForm):
    skills = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        help_text='Enter your skills separated by commas (e.g., Python, JavaScript, Machine Learning)'
    )
    experience = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        help_text='Describe your work experience'
    )
    projects = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        required=False,
        help_text='Describe your projects (optional)'
    )

    class Meta:
        model = Student
        fields = ('skills', 'experience', 'projects', 'profile_picture', 'resume')

class SearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'search-input',
            'placeholder': 'Search for talent (e.g., Python developer with ML experience)'
        })
    )
    skills = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Filter by skills (comma-separated)',
            'id': 'skills-input'
        })
    )
    location = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Filter by location',
            'id': 'location-input'
        })
    )
    experience_level = forms.ChoiceField(
        choices=[
            ('', 'Any Experience'),
            ('entry', 'Entry Level'),
            ('mid', 'Mid Level'),
            ('senior', 'Senior Level')
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'experience-level'})
    )