from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import ModelFormMixin

from app.models import Profile, LanguagesForm, ActiveLanguageForm

def index(request):
    if request.user.is_authenticated():
        return redirect('dashboard')
    return render(request, 'app/index.html')

class ProtectedView(TemplateView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)

class DashboardView(ModelFormMixin, ProtectedView):
    model = Profile
    template_name = 'app/dashboard.html'

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        languages = profile.languages.all()

        if not languages:
            return render(request, self.template_name, {
                'first_language_form': ActiveLanguageForm(instance=profile),
            })

        return render(request, self.template_name, {
            'active_language_form': ActiveLanguageForm(instance=profile, added=languages),
        })

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        form = ActiveLanguageForm(request.POST, instance=profile)

        if not profile.languages.all() and not form.is_valid():
            return render(request, self.template_name, {
                'first_language_form': form,
            })
        elif not form.is_valid():
            return render(request, self.template_name, {
                'active_language_form': form,
            })
        else:
            form.save()
            return redirect('dashboard')


class SettingsView(ProtectedView):
    template_name = 'app/settings.html'

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        return render(request, 'app/settings.html', {
            'language_form': LanguagesForm(instance=profile),
        })

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        form = LanguagesForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('settings')
        else:
            return render(request, 'app/settings.html', {
                'language_form': form,
            })