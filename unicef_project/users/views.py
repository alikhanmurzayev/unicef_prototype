from django.shortcuts import render

# Create your views here.

def profile_detail_view(request):
    return render(request, 'profile_detail.html')