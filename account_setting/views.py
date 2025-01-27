from django.shortcuts import render , redirect
from django.views import View
from accounts.forms import ProfileForm 
from django.urls import reverse
# Create your views here.


class AccountSettingView(View):
    def get(self,request):
        return render(request,'account_setting/account_setting.html')


class UpdateProfileView(View):
    def get(self,request):
        user = self.request.user
        form = ProfileForm(instance=user.profile)
        return render(request,'account_setting/update_profile.html' , {'form' : form })
    
    def post(self,request):
        user = self.request.user
        form = ProfileForm(request.POST ,request.FILES, instance=user.profile)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = user
            obj.save()
            return redirect(reverse('account_setting:account-setting'))
        else:
            return render(request,'account_setting/update_profile.html' , {'form' : form })