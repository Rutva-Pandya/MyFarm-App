from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Farm_View/farm_view.html')