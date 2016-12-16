from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import Users ,Posts
import json


def loginpost(request):
	name=request.GET.get("myName");
	password=request.GET.get("myPass");
	print name,password
	request.session["username"]=name
	data=Users(first_name=name,password=password)
	data.save()
	print "done"
	return HttpResponseRedirect("/sulekha/home/")

	"""guidance for writing your data in JSON file""" 
	# 	diaplayData =  (serializers.serialize('json',Posts.objects.all()))
	# 	return JsonResponse({'diaplayData':diaplayData})
	# 	with  open("home.json",'a') as test_file:
	# 		 json.dump(displayData, home)



def home(request):
	name=request.session.get("username");
	return render(request, "home.html",{"uname":name})

def index(request):
	return render(request, "index.html")

def login(request):
	return render(request,"loginPage.html")

def logout(request):
	del request.session['username']
	return HttpResponseRedirect("/sulekha/home/")

def post(request):
	if request.method == "POST":

		# if form.is_valid():
			house_type= request.POST.get("type")
			rooms= request.POST.get("noofroom")
			location= request.POST.get("location")
			address= request.POST.get("add")
			city= request.POST.get("city")
			state= request.POST.get("state")
			zipcode= request.POST.get("number")
			images= request.FILES["imgaes"]
			details= request.POST.get("details")

			addData = Posts(house_type = house_type, rooms = rooms, location = location, address = address, city = city, state = state, zipcode = zipcode, images= images,details=details  )
 			uploadAddData = addData.save()
 			return HttpResponseRedirect('/sulekha/home/')

	return render(request,"post.html")

def postview(request):

		displayData =  (serializers.serialize('json',Posts.objects.all()))
		# return JsonResponse({'diaplayData':diaplayData})
		return render(request,"jsonview.html",{"displayData":displayData})


