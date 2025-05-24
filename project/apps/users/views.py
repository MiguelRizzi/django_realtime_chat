from django.views import View
from django.views.generic import DetailView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import CustomUserCreationForm, AvatarForm
from .models import Avatar

import json

# Authentication

class CustomLoginView(LoginView):
    template_name = "users/login.html"
    form_class = AuthenticationForm


class CustomLogoutView(LogoutView, LoginRequiredMixin):
    next_page = "chat:index"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
     

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
    

# Avatars

class AvatarDetailView(LoginRequiredMixin, DetailView):
    model = Avatar
    


class AvatarCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = AvatarForm()
        return render(request, 'users/avatar_form.html', {'form': form})

    def post(self, request):
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.create(
                user=request.user,
                image=form.cleaned_data.get('image'),
            )
            return HttpResponse(
                status=201,
                headers={
                    'HX-Trigger': json.dumps({
                        "showMessage": "The Avatar was saved successfully."
                    })
                }
            )
        else:
            return render(request, 'users/avatar_form.html', {'form': form})

class AvatarConfirmDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        avatar = get_object_or_404(Avatar, pk=pk)
        return render(request, 'users/avatar_confirm_delete.html', {'avatar': avatar})
    


class AvatarUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        avatar = get_object_or_404(Avatar, pk=pk)
        form = AvatarForm(instance=avatar)
        return render(request, 'users/avatar_form.html', {'form': form, 'avatar': avatar})

    def post(self, request, pk):
        avatar = get_object_or_404(Avatar, pk=pk)
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            avatar.image = form.cleaned_data.get('image')
            avatar.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "showMessage": "The avatar has been updated successfully."
                    })
                }
            )
        else:
            return render(request, 'users/avatar_form.html', {'form': form, 'avatar': avatar})


class AvatarDeleteView(LoginRequiredMixin, View):
    def delete(self, request, pk):
        avatar = get_object_or_404(Avatar, pk=pk)
        avatar.delete()
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "showMessage":"The avatar was successfully deleted."
                })
            }
        )