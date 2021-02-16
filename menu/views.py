from django.shortcuts import  render,redirect

from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.
def homemenu(request):
	#return HttpResponse('<h1>Hello , I am learning Django!</h1>')
	return render(request,'menu/home.html')

	
def aboutmenu(request):
	return HttpResponse('<h1>In about Menu!</h1>')

def loginmenu(request):
	#return HttpResponse('<h1>Hello , I am learning Django!</h1>')
	
	if request.method=='POST':
		print(" I am in POST request")
		#pass the field name to get the input value
		unameEntered=request.POST['username']
		Enteredpassword=request.POST['password']
		print('username=',unameEntered)
		userObject=auth.authenticate(username=unameEntered,password=Enteredpassword)

		if userObject is not None:
			auth.login(request,userObject)
			print("user logged in")
			return redirect('myhome')

		else:
			print("Username/password invalid")
			messages.error(request,"username/password invalid")
			return redirect("mylogin")
	else:
		return render(request,'menu/login.html')

def registration(request):
	if request.method=='POST':
		print(" I am in POST request")
		username=request.POST['username']
		password1=request.POST['password1']
		password2=request.POST['password2']
		email=request.POST['Email']
		print('username=',username)
		print('password1=',password1)
		print('password2=',password2)
		print('email=',email)
		if(password1==password2):
			if User.objects.filter(username=username).exists():
				print('The username is not available/its already exists')
				messages.error(request,"username is not available/its already exists")
				return redirect('registration')
			else:
				user = User.objects.create_user(username=username,password=password1,email=email)
				user.save()
				print(" you are now registered and can login")
				return redirect('mylogin')
		else:
			print('Password do not match,please enter again')
			messages.error(request,"password do not match,please enter again")
			return redirect("registration")
		
	else:
		print("I am in GET request")
		return render(request,'menu/registration.html')

def logout(request):
	print("im in logout")
	auth.logout(request)
	return redirect('mylogin')

	

	

