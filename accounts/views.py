from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account has been created succesfully you can now Log In')
			return redirect('accounts:login')
	else:
		form = SignUpForm()
	context = {'form': form}

	return render(request, 'signup.html', context)

@login_required
def profile(request):
	return render(request, 'profile.html', {})
