from django.shortcuts import render

# Create your views here.

def iloveyjj(request):
    return render(request,'mypage/Love.html',{})