from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.forms import RegisterForm, LoginForm

class CustomRegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
       user = form.save()
       user.save()
       return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        response = super().form_valid(form)

        user = self.request.user
        access_token = self.get_access_token(user)

        return HttpResponseRedirect(self.success_url)
    
    def get_access_token(self, user):
        refresh = RefreshToken.for_user(user)
        return refresh.access_token
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")
