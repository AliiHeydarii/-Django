from django.shortcuts import render , redirect
from django.views import View
from .forms import CustomUserCreationForm
# Create your views here.

class RegisterUserView(View):
    def get(self,request):
        form = CustomUserCreationForm()
        context = {'form' : form }
        return render(request,'accounts/register.html',context)
    
    def post(self,request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,'accounts/register.html',{'form' : form})