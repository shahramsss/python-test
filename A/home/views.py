from django.shortcuts import render, redirect
from django.views import View
from .froms import UserRegistrationForm
from django.contrib.auth.models import User


class HomeView(View):
    def get(self, request):
        return render(request, "home/home.html")


class AboutView(View):
    def get(self, request):
        return render(request, "home/home.html")


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = "home/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                username=cd["username"], email=cd["email"], password=cd["password"]
            )
            return redirect("home:home")
        return render(request, self.template_name, {"form": form})
