from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views

def index(request):
	if request.user.is_authenticated():
		return redirect('dashboard')
	return render(request, 'lingo/index.html')

@login_required
def dashboard(request):
	return render(request, 'lingo/dashboard.html')