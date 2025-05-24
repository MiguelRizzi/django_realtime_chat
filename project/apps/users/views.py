from django.views import View
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


# _____________________ AUTH VIEWS _____________________
class CustomLoginView(LoginView):
    template_name = "users/login.html"
    form_class = AuthenticationForm


class CustomLogoutView(LogoutView, LoginRequiredMixin):
    template_name = "base.html"

    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        return redirect ('users:login')   
     

class CustomSignupView(View):
    template_name = "users/signup.html"

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        return render(request, self.template_name, {"form": form})
    

