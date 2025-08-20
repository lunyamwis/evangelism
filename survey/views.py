from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Render the home page of the survey application.
    """
    return render(request, 'survey/home.html')