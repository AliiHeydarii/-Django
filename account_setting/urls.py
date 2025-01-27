from django.urls import path
from . import views

app_name = 'account_setting'

urlpatterns = [
    path('' , views.AccountSettingView.as_view() , name='account-setting'),
    path('profile/' , views.UpdateProfileView.as_view() , name='profile')
]