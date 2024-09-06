from django.shortcuts import render, redirect


def home(request):
	
	return render(request, 'routes/home.html')
	
	
	
def login(request):
	
	return render(request, "routes/login.html")



def configs(request):

	if request.method == "POST":

		return redirect("/")

	return render(request, "routes/configs.html")

# Create your views here.
