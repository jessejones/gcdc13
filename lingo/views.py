from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

def index(request):
    if request.user.is_authenticated():
        return redirect('dashboard')
    return render(request, 'lingo/index.html')

class ProtectedView(TemplateView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)

class DashboardView(ProtectedView):
    template_name = 'lingo/dashboard.html'

class SettingsView(ProtectedView):
    template_name = 'lingo/settings.html'