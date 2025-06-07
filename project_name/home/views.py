from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, PaymentForm
from .models import PageVisit
from django.db.models import Count

def homepage(request):
    return render(request, 'home/index.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('payment')  # Redirect to payment page after registration
    else:
        form = RegistrationForm()
    
    return render(request, 'home/register.html', {'form': form})

    

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to a desired page after login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'home/login.html', {'form': form})



def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # For this example, we'll just simulate a successful payment
            return redirect('payment_confirmation')
    else:
        form = PaymentForm(initial={'amount': '49.99'})  # Set the initial amount
    
    return render(request, 'home/payment.html', {'form': form})



def payment_confirmation(request):
    return render(request, 'home/payment_confirmation.html')


    
def dashboard(request):
    return render(request, 'home/dashboard.html')        



@login_required
def emergency_alerts(request):
    return render(request, 'home/emergency_alerts.html')

@login_required
def skill_building(request):
    return render(request, 'home/skill_building.html')

@login_required
def cultural_preservation(request):
    return render(request, 'home/cultural_preservation.html')

@login_required
def discussion_forums(request):
    return render(request, 'home/discussion_forums.html')

@login_required
def resource_directory(request):
    return render(request, 'home/resource_directory.html')



def report(request):
    # Get the count of visits per page
    visits = PageVisit.objects.values('page').annotate(count=Count('id')).order_by('-count')
    
    # Get the times each page was visited
    visit_times = PageVisit.objects.values('page', 'visit_time').order_by('visit_time')
    
    return render(request, 'home/report.html', {'visits': visits, 'visit_times': visit_times})    


def user_logout(request):
    logout(request)
    return redirect('login')