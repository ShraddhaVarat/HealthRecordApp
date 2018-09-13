from django.shortcuts import render
from .models import Hospital,Doctor,Checkup_Details,Prescription,Medicine,Patient,Pharmacist
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
	return render(request, 'HealthRecord/home.html', {})

def login(request):
	if request.method == 'POST':
		id = request.POST.get("lid")
		ps = request.POST.get("lpassword")
		if id[3]=="H":
			return render(request, 'HealthRecord/hprofile.html', {})
		elif id[3]=="D":
			return render(request, 'HealthRecord/dprofile.html', {})
		elif id[3]=="M":
			return render(request, 'HealthRecord/phprofile.html', {})
		elif id[3]=="P":
			return render(request, 'HealthRecord/pprofile.html', {})

	else:
		return render(request, 'HealthRecord/login.html', {})

def signup(request):
	if request.method == 'POST':
		
		type = request.POST.get("utype")
		#print(type)
		id = request.POST.get("sid")
		#print(id)
		ps = request.POST.get("spassword")
		#print(ps)

		if type=="Hospital":
			return render(request, 'HealthRecord/hospitalform.html', {})
		elif type=="Patient":
			return render(request, 'HealthRecord/patientform.html', {})
		elif type=="Pharmacist":
			return render(request, 'HealthRecord/pharmacistform.html', {})
		elif type=="Doctor":
			return render(request, 'HealthRecord/doctorform.html', {})
	else:
		return render(request, 'HealthRecord/login.html', {})


def hospital(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		email = request.POST.get("email")
		phone = request.POST.get("phone")
		helpline = request.POST.get("helpline")
		address = request.POST.get("address")
		htype = request.POST.get("type")
		lat = request.POST.get("lat")
		longitude = request.POST.get("long")
		#print(name + email + phone + helpline + address + htype+ lat+ longitude)
		return render(request, 'HealthRecord/login.html', {})
	else:
		return render(request, 'HealthRecord/hospitalform.html', {})

def hprofile(request):
	return render(request, 'HealthRecord/hprofile.html', {})

def patient(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		email = request.POST.get("email")
		phone1 = request.POST.get("phone1")
		phone2 = request.POST.get("phone2")
		raddress = request.POST.get("raddr")
		paddress = request.POST.get("paddr")
		profession = request.POST.get("profession")
		dob = request.POST.get("dob")
		aadhar = request.POST.get("aadhar")
		gender = request.POST.get("gender")
		mstatus = request.POST.get("mstatus")
		bgrp = request.POST.get("bgrp")
		sname = request.POST.get("sname")
		#print(name + email + phone1 + phone2 + raddress+ paddress + profession+ dob)
		#print(aadhar+gender+mstatus+bgrp+sname)
		return render(request, 'HealthRecord/login.html', {})
	else:
		return render(request, 'HealthRecord/patientform.html', {})

def pprofile(request):
	return render(request, 'HealthRecord/pprofile.html', {})

def doctor(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		email = request.POST.get("email")
		phone1 = request.POST.get("phone1")
		phone2 = request.POST.get("phone2")
		raddress = request.POST.get("raddr")
		qualification = request.POST.get("qualification ")
		
		#print(name + email + phone + helpline + address + htype+ lat+ longitude)
		return render(request, 'HealthRecord/login.html', {})
	else:
		return render(request, 'HealthRecord/doctorform.html', {})

def dprofile(request):
	return render(request, 'HealthRecord/dprofile.html', {})

def pharmacist(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		email = request.POST.get("email")
		phone1 = request.POST.get("phone1")
		phone2 = request.POST.get("phone2")
		address = request.POST.get("addr")
		#qualification = request.POST.get("qualification ")
		
		#print(name + email + phone + helpline + address + htype+ lat+ longitude)
		return render(request, 'HealthRecord/login.html', {})
	else:
		return render(request, 'HealthRecord/pharmacistform.html', {})

def phprofile(request):
	return render(request, 'HealthRecord/phprofile.html', {})