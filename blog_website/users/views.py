from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    # If the request is POST method then create a form with values
    # else create empty form
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        # Save user and print the flashed message if form is valid
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            # Return to home page
            return redirect('blog-home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})