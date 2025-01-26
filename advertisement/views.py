from django.shortcuts import render,get_object_or_404
from .models import Advertisement
from django.views import View
# Create your views here.

class IndexView(View):
    def get(self,request):
        ad_list = Advertisement.objects.all()
        context = {'ad_list':ad_list}
        return render(request,'advertisement/index.html',context)
    
    
class AdDetailView(View):
    def get(self,request,pk):
        ad = get_object_or_404(Advertisement,pk=pk)
        context = {'ad' : ad}
        return render(request,'advertisement/ad_detail.html' , context)
