from django.shortcuts import render
from .models import Hospital,Doctor,Checkup_Details,Prescription,Medicine,Patient,Pharmacist
from django.http import HttpResponseRedirect
#from django.contrib.auth import login
#from mongoengine.django.auth import User
from mongoengine.queryset import DoesNotExist
from django.contrib import messages
from pymongo import MongoClient 
# Create your views here.


try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

db = conn.Record 

def home(request):
	return render(request, 'HealthRecord/home.html', {})

def login(request):
	if request.method == 'POST':
		id = request.POST.get("lid")
		ps = request.POST.get("lpassword")
		if id[3]=="H":
			collection = db.hospital
			c =collection.find_one({"hospital_id": id})
			if c["password"]==ps:	
				return render(request, 'HealthRecord/hprofile.html', {})
			else:
				messages.success(request, "Invalid LoginId or Password")
				return HttpResponseRedirect('/login/')
		elif id[3]=="D":
			collection = db.doctor
			c =collection.find_one({"doctor_id": id})
			if c["password"]==ps:
				return render(request, 'HealthRecord/dprofile.html', {})
			else:
				messages.success(request, "Invalid LoginId or Password")
				return HttpResponseRedirect('/login/')
			
		elif id[3]=="M":
			collection = db.pharmacist
			c =collection.find_one({"pharmacist_id": id})
			if c["password"]==ps:	
				return render(request, 'HealthRecord/phprofile.html', {})
			else:
				messages.success(request, "Invalid LoginId or Password")
				return HttpResponseRedirect('/login/')
		elif id[3]=="P":
			collection = db.patient
			c =collection.find_one({"patient_id": id})
			if c["password"]==ps:	
				return render(request, 'HealthRecord/pprofile.html', {})
			else:
				messages.success(request, "Invalid LoginId or Password")
				return HttpResponseRedirect('/login/')

	else:
		return render(request, 'HealthRecord/login.html', {})

def signup(request):
	if request.method == 'POST':
		
		type = request.POST.get("utype")
		s_id = request.POST.get("sid")
		s_ps = request.POST.get("spassword")
		

		if type=="Hospital":
			collection = db.hospital
			i = collection.count()
			i+=1
			hospital_id = "PMCH" + str(i)
			rec1 = {
				"hospital_id" :hospital_id,
				"password" : s_ps,
            	"registration_no": s_id,

			}
			rec_id1 = collection.insert_one(rec1) 
			return render(request, 'HealthRecord/hospitalform.html', {})
		elif type=="Patient":
			collection = db.patient
			i = collection.count()
			i+=1
			patient_id = "PMCP" + str(i)
			rec1 = {
				"patient_id" :patient_id,
				"password" : s_ps,
            	"aadhar_no": s_id,

			}
			rec_id1 = collection.insert_one(rec1) 
			return render(request, 'HealthRecord/patientform.html', {})
		elif type=="Pharmacist":
			collection = db.pharmacist
			i = collection.count()
			i+=1
			pharmacist_id = "PMCM" + str(i)
			rec1 = {
				"pharmacist_id" :pharmacist_id,
				"password" : s_ps,
            	"registration_no": s_id,

			}
			rec_id1 = collection.insert_one(rec1) 
			return render(request, 'HealthRecord/pharmacistform.html', {})
		elif type=="Doctor":
			collection = db.doctor
			i = collection.count()
			i+=1
			doctor_id = "PMCD" + str(i)
			rec1 = {
				"doctor_id" :doctor_id,
				"password" : s_ps,
            	"registration_no": s_id,

			}
			rec_id1 = collection.insert_one(rec1) 
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
		
		collection = db.hospital
		i = collection.count()
			
		hospital_id = "PMCH" + str(i)
		result = collection.update_many( 
        {"hospital_id":hospital_id}, 
        { 
                "$set":{ 
                        "name":name, 
            			"phone_no":phone, 
            			"helpline" : helpline,
            			"email" :email,
            			"address" : address,
            			"latitude" : lat,
            			"longitude" : longitude
                        
                        }
                  
                } 
        ) 
		
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
		
		collection = db.patient
		i = collection.count()
			
		patient_id = "PMCP" + str(i)
		result = collection.update_many( 
        {"patient_id":patient_id}, 
        { 
                "$set":{ 
                        "name":name, 
            			"phone1":phone1, 
            			"phone2":phone2,
            			"email_id" :email,
            			"permanent_addr" : paddress,
            			"local_addr" : raddress,
						"dob" : dob,
						"gender" : gender,
						"profession" : profession,
						"marital_status" : mstatus,
						"blood_grp" : bgrp,
						"spouse_name" : sname                      
                        }
                  
                } 
        ) 

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
		
		collection = db.doctor
		i = collection.count()
			
		doctor_id = "PMCD" + str(i)
		result = collection.update_many( 
        {"doctor_id":doctor_id}, 
        { 
                "$set":{ 
                        "name":name, 
            			"phone1":phone1,
            			"phone2":phone2,
            			"email" :email,
            			"address" : raddress,
                        "qualification" : qualification 
								
                        }
                  
                } 
        ) 
		
		return render(request, 'HealthRecord/login.html', {})
	else:
		return render(request, 'HealthRecord/doctorform.html', {})

def phprofile(request):
	return render(request, 'HealthRecord/phprofile.html', {})

def pharmacist(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		email = request.POST.get("email")
		phone1 = request.POST.get("phone1")
		phone2 = request.POST.get("phone2")
		address = request.POST.get("addr")
		
		collection = db.pharmacist
		i = collection.count()
			
		pharmacist_id = "PMCM" + str(i)
		result = collection.update_many( 
        {"pharmacist_id":pharmacist_id}, 
        { 
                "$set":{ 
                        "name":name, 
            			"phone1":phone1,
            			"phone2":phone2,
            			"email" :email,
            			"address" : address								
                        }
                  
                } 
        ) 
		
		return render(request, 'HealthRecord/login.html', {})
	else:
		return render(request, 'HealthRecord/pharmacistform.html', {})

def dprofile(request):
	if 'prescription1' in request.POST:
		pid = request.POST.get("pid")
		print(pid)
		i = request.POST.get("counter")
		i= int(i)
		collection = db.patient
		collection1 = db.prescription
		collection2 = db.medicine
		#res is a list of medicine
		res = []
		for j in range(0,i):
			name1 = "name" + str(j)
			morning1 = "morning" + str(j)
			afternoon1 = "afternoon" + str(j)
			evening1 = "evening" + str(j)
			days1 = "days" + str(j)
			name = request.POST.get(name1)
			morning = request.POST.get(morning1)
			afternoon = request.POST.get(afternoon1)
			evening = request.POST.get(evening1)
			days = request.POST.get(days1)
	
			#r = rec + str(j) 
			r = { 
            "medicine_name":name, 
            "morning":morning, 
            "afternoon":afternoon,
            "evening" : evening,
            "no_of_days" : days
            } 
			#val = collection2.insert_one(r)
			res.append(r)
		
		
		cursor = collection.find({"patient_id":pid})
		no=0
		#res2 is a list of prescription
		res2 = []
		for record in cursor: 
			#if record["patient_id"]==pid:
				#if not None(record["prescription"]):
					for m in record["prescription"]:
						no+=1
						res2.append(m)
					break;

		print(no)
		p_id = pid + "PR" + str(no)
		#result is the latest prescription
		result = {
		    "prescription_id": p_id ,
		    "medicine" :res
		}
		print(result)
		collection1.insert_one(result)

		#list of prescription
		res2.append(result)
		res3 = collection.update_many( 
        {"patient_id":pid}, 
        { 
                "$set":{ 
                        "prescription":res2
                        }
                } 
        ) 

		
		return render(request, 'HealthRecord/dprofile.html', {})

	elif 'search' in request.POST:
		id = request.POST.get("search_patient")
		collection = db.patient
		c =collection.find_one({"patient_id": id })
		if c:
			return render(request, 'HealthRecord/dprofile.html', {'pdetails':c})
	else:
		#plist = Patient.objects.all()
		return render(request, 'HealthRecord/dprofile.html', {})

