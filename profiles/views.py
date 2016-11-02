from django.contrib.auth import get_user_model
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.conf import settings
from django.core.mail import send_mail

User = get_user_model()
from .forms import ProfileForm, ContactusForm
from .models import Profile


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['title'] = self.request.user.username
        return context


class AboutUs(TemplateView):
    template_name = 'about_us.html'


def contact_us(request):
    form = ContactusForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Blog contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = "%s/%s via %s"%(
                form_full_name,
                form_message,
                form_email)
        send_mail(subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False)
    context = {
        "form": form,
    }

    return render(request, 'contact_us.html', context)


@login_required
def account_redirect(request):
    return redirect('profiles:profile', username=request.user.username)


class UserListView(ListView):
    model = Profile
    template_name = 'profiles/user_list.html'


@login_required
def profile_edit(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('profiles:profile', username=request.user.username)

    context = {
        "title": 'Edit Profile',
        "form":form,
    }
    return render(request, 'profiles/profile_form.html', context)


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)
    title = request.user.username
    context = {'profile': profile, 'title': title }
    return render(request,'profiles/profile_detail.html', context )







