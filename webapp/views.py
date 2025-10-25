from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def index_view(request):
    """Render the site index/home page."""
    return render(request, 'webapp/index.html')

def signup_view(request):
    """Display and process a user signup form using Django's built-in
    UserCreationForm. On success, redirect to the login page with a
    success message.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created. You can now sign in.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'webapp/signup.html', {'form': form})