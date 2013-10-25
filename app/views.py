from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from app.models import Language, Profile, ProfileForm

def index(request):
    if request.user.is_authenticated():
        return redirect('dashboard')
    return render(request, 'app/index.html')

class ProtectedView(TemplateView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)

class DashboardView(ProtectedView):
    template_name = 'app/dashboard.html'

class SettingsView(ProtectedView):
    template_name = 'app/settings.html'

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        return render(request, 'app/settings.html', {
            'language_form': ProfileForm(instance=profile),
        })

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('settings')
        else:
            return render(request, 'app/settings.html', {
                'language_form': form,
            })