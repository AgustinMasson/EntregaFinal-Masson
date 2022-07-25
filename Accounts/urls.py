from django.urls import path
from Accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("Accounts/LogIn", views.login_request, name="LogIn"),
    path("Accounts/SignUp", views.signup, name="SignUp"),
    path("Accounts/LogOut", LogoutView.as_view(template_name="Accounts/logout.html"), name="LogOut"),
    path("Accounts/UpdateProfile", views.updateProfile, name="UpdateProfile"),
]