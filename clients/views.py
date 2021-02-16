from django.shortcuts import render

from django .http import HttpResponse
from .models import Drivers

# Create your views here.
def clientListing(request):
	#return HttpResponse('<h1>Hello , I am learning Django!</h1>')
	clientlisting=Drivers.objects.all()
	print("Recieved  driver records",len(clientlisting))
	context={
		'driverList':clientlisting
	}
	return render(request,'clients/client.html',context)

	