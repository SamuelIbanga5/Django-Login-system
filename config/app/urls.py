from django.urls import path
from .views import (
    homePage, 
    registerPage, 
    loginPage,  
    logoutUser
    )

urlpatterns = [
    path('', homePage, name='home'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    # path('resetPassword/', PasswordReset.as_view(), name="reset-password"),
    # path('password-reset-done/', PasswordResetDone.as_view(), name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmationView.as_view(), name='password-reset-confirm'),
    # path('password-reset-complete/', PasswordResetComplete.as_view(), name='password-reset-complete'),
]