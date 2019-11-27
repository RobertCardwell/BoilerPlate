from django.shortcuts import render

# dummy placeholder function, for testing 
def home(request):
    return render(request, 'index.html')
