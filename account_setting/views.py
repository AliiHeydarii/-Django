from django.shortcuts import render
from django.views import View
from accounts.forms import ProfileForm 
# Create your views here.


class AccountSettingView(View):
    def get(self,request):
        return render(request,'account_setting/account_setting.html')


class UpdateProfileView(View):
    def get(self,request):
        form = ProfileForm()
        return render(request,'account_setting/update_profile.html' , {'form' : form })