from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Render the home page of the medical missionary application.
    """
    return render(request, 'medicalmissionary/home.html')