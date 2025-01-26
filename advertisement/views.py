from django.shortcuts import render
from .models import Advertisement
from django.views import View
# Create your views here.

class IndexView(View):
    def get(self,request):
        ad_list = Advertisement.objects.all()
        context = {'ad_list':ad_list}
        return render(request,'advertisement/index.html',context)