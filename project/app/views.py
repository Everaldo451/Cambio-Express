from django.shortcuts import render


def home(request):
	
	return render(request, 'routes/home.html')
	
	
	
def login(request):
	
	return render(request, "routes/login.html")

# Create your views here.
