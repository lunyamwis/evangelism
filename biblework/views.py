from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Render the home page of the bible work application.
    """
    return render(request, 'biblework/home.html')