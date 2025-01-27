from django.shortcuts import render , redirect , get_object_or_404
from django.views import View
from accounts.forms import ProfileForm 
from django.urls import reverse
from advertisement.models import Advertisement
from django.contrib.auth.mixins import LoginRequiredMixin
from advertisement.forms import AdvertisementForm
# Create your views here.


class AccountSettingView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'account_setting/account_setting.html')


class UpdateProfileView(LoginRequiredMixin,View):
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
        
        
        
class MyAdsView(LoginRequiredMixin,View):
    def get(self,request):
        my_ads = Advertisement.objects.filter(user=self.request.user)
        context = {'my_ads' : my_ads}
        return render(request,'account_setting/my_ads.html' , context)
    
    
    
class UpdateAds(LoginRequiredMixin,View):
    def get(self,request,pk):
        ad = get_object_or_404(Advertisement,pk=pk)
        form = AdvertisementForm(instance=ad)
        return render(request,'account_setting/update_ads.html',{'form' : form})
    
    def post(self,request,pk):
        ad = get_object_or_404(Advertisement,pk=pk)
        form = AdvertisementForm(request.POST , request.FILES,instance=ad)
        if form.is_valid():
            form.save()
            return redirect(reverse('account_setting:my-ads'))
        
class DeleteAds(LoginRequiredMixin,View):
    def get(self,request,pk):
        ad = get_object_or_404(Advertisement,pk=pk)
        ad.delete()
        return redirect(reverse('account_setting:my-ads'))