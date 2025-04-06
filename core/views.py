from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Q, F
import spacy
from .forms import UserRegistrationForm, StudentProfileForm, SearchForm
from .models import Student, RecruiterSearch, Analytics

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = None

def home(request):
    return render(request, 'core/home.html')

def discover(request):
    form = SearchForm(request.GET)
    # Exclude students with admin accounts (is_staff or is_superuser)
    students = Student.objects.exclude(user__is_staff=True).exclude(user__is_superuser=True)

    if form.is_valid():
        query = form.cleaned_data.get('query', '')
        skills = form.cleaned_data.get('skills', '')
        location = form.cleaned_data.get('location', '')
        experience_level = form.cleaned_data.get('experience_level', '')

        if query and nlp:
            # Process the natural language query
            doc = nlp(query.lower())
            # Extract relevant keywords
            keywords = [token.text for token in doc if not token.is_stop and not token.is_punct]

            # Search in skills and experience
            q_objects = Q()
            for keyword in keywords:
                q_objects |= (
                    Q(skills__icontains=keyword) |
                    Q(experience__icontains=keyword) |
                    Q(projects__icontains=keyword)
                )
            students = students.filter(q_objects)

            # Log the search
            RecruiterSearch.objects.create(
                search_query=query,
                filters_used={
                    'skills': skills,
                    'location': location,
                    'experience_level': experience_level
                }
            )

            # Update analytics
            for keyword in keywords:
                # Try to get the existing analytics object
                try:
                    analytics = Analytics.objects.get(skill_name=keyword)
                    # If it exists, update the search count
                    analytics.search_count = F('search_count') + 1
                    analytics.save()
                except Analytics.DoesNotExist:
                    # If it doesn't exist, create a new one with search_count=1
                    Analytics.objects.create(skill_name=keyword, search_count=1)

        if skills:
            skill_list = [s.strip() for s in skills.split(',') if s.strip()]
            if skill_list:
                # Create a Q object for OR filtering of skills
                skill_query = Q()
                for skill in skill_list:
                    skill_query |= Q(skills__icontains=skill)
                students = students.filter(skill_query)

        if location:
            location_list = [loc.strip() for loc in location.split(',') if loc.strip()]
            if location_list:
                # Create a Q object for OR filtering of locations
                location_query = Q()
                for loc in location_list:
                    location_query |= Q(experience__icontains=loc)
                students = students.filter(location_query)

        if experience_level:
            students = students.filter(experience__icontains=experience_level)

    context = {
        'form': form,
        'students': students,
        'total_results': students.count()
    }
    return render(request, 'core/discover.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Please complete your profile.')
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def profile(request):
    # Get or create the student profile for the current user
    student, _ = Student.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = StudentProfileForm(instance=student)

    return render(request, 'core/profile.html', {'form': form})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        student = get_object_or_404(Student, user=request.user)
        user = request.user
        student.delete()
        user.delete()
        messages.success(request, 'Your profile has been deleted.')
        return redirect('home')
    return render(request, 'core/delete_profile.html')
