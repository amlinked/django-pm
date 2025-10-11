from django.urls import path , include
from django.contrib.auth import views as auth_views
from accounts.views import RegisterView , edit_profile
from accounts.forms import UserLoginForm

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(authentication_form=UserLoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('profile/', edit_profile, name="profile"),
    path("register/", RegisterView.as_view(), name="register"),

    path("password_change/", auth_views.PasswordChangeView.as_view(),
         name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),

    path("password_reset/", auth_views.PasswordResetView.as_view(),
         name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
]
