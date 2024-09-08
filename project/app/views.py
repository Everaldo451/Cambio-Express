from django.shortcuts import render, redirect
from rest_framework_simplejwt.tokens import AccessToken
from .models import User
from .form import ConfigForm


def home(request):
	
	return render(request, 'routes/home.html')
	
	
	
def login(request):
	
	return render(request, "routes/login.html")



def configs(request):

	if request.method == "POST":
		
		form = ConfigForm(request.POST)

		print(form)

		if form.is_valid() and request.COOKIES.get("access"):

			try:

				token = AccessToken(request.COOKIES.get("access"))

				user = User.objects.get(id=token.payload.get("id"))

				username = form.data.get("username")
				email = form.data.get("email")
				password = form.data.get("password")

				user.username = username if username else user.username
				user.email = email if email else user.email
				

				if password:
					user.set_password(password)

				user.save()
			
			except:pass

			print("oi")

		return redirect("/")

	return render(request, "routes/configs.html")

# Create your views here.
