from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib import messages

def home(request):
	return render(request,"home.html")

def check_phone(request):
	if request.method=="POST":
		phone=request.POST.get('phone')
		if len(phone)!=10 or not phone.isnumeric():
			messages.add_message(request,messages.WARNING,"Please enter a valid phone number, don't add +91 or 0 in the prefix")
			return render(request,"home.html")
		try:
			phone="91"+phone
			data=facebook_data.objects.get(mobile_no=phone)
			if user_matched.objects.filter(mobile_no=data.mobile_no).exists()==False:
				visitor_save=user_matched(mobile_no=data.mobile_no,registration=data.registration,info=data.info)
				visitor_save.save()
		except:
			if user_not_matched.objects.filter(phone=phone).exists()==False:
				visitor_save=user_not_matched(phone=phone)
				visitor_save.save()
			messages.add_message(request,messages.SUCCESS,"No breach record found for your number.")
			return render(request,"home.html")
		messages.add_message(request,messages.ERROR,"Your phone number has been exposed in the latest FB data breach.")
		return render(request,"home.html")
	return render(request,"home.html")

