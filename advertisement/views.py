from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import Advertisement ,Category
from django.views import View
from .forms import AdvertisementForm 
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class IndexView(View):
    def get(self,request):
        search = request.GET.get('search')
        if search:
            ad_list = Advertisement.objects.filter(title__contains=search)
        else:
            ad_list = Advertisement.objects.all()
        categories = Category.objects.all()
        context = {'ad_list':ad_list , 'categories' : categories}
        return render(request,'advertisement/index.html',context)
    
    
class AdDetailView(View):
    def get(self,request,pk):
        ad = get_object_or_404(Advertisement,pk=pk)
        context = {'ad' : ad}
        return render(request,'advertisement/ad_detail.html' , context)


class AdCreateFormView(LoginRequiredMixin,View):
    def get(self,request):
        form = AdvertisementForm()
        context = {'form' : form}
        return render(request,'advertisement/ad_create.html',context)
    
    
    def post(self,request):
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = self.request.user
            obj.save()
            messages.success(request,'آگهی شما با موفقیت ثبت شد')
            return redirect('ad-create')
        else:
            context = {'form' : form}
            return render(request,'advertisement/ad_create.html',context)
        

class AdCategoryView(View):
    def get(self,request,name):
        ads = Advertisement.objects.filter(category__name__contains = name)
        categories = Category.objects.all()
        category_name = Category.objects.filter(name__contains = name).first()
        context = {
            'ads' : ads ,
            'categories' : categories,
            'category_name' : category_name
            }
        return render(request,'advertisement/filter_result.html', context)