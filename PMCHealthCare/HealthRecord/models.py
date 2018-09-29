from mongoengine import *
from django.utils import timezone
import datetime
from datetime import datetime
from django.db.models import (
    DateField, DateTimeField, IntegerField, TimeField, Transform,
)
from PMCHealthCare.settings import DBNAME

connect(DBNAME)

class Doctor(Document):
	doctor_id = StringField(max_length=50)
	password = StringField(max_length=50)
	name = StringField(max_length=100)
	phone1 = StringField(max_length=15)
	phone2 = StringField(max_length=15)
	address = StringField(max_length=50)
	email = StringField(max_length=254,required=False)
	registration_no = StringField(max_length=50)
	qualification = ListField(StringField(max_length=50))
	hospitals_associated = SortedListField(StringField(max_length=50))

class Hospital(Document):
	hospital_id = StringField(max_length=50)
	password = StringField(max_length=50)
	name = StringField(max_length=100)
	phone_no = StringField(max_length=15)
	helpline = StringField(max_length=15)
	email = StringField(max_length=254,required=False)
	address = StringField(max_length=100)
	pincode = StringField(max_length=6)
	registration_no = StringField(max_length=50)
	hospital_type = StringField(max_length=50)
	doctors_associated = SortedListField(ReferenceField(Doctor))
	latitude = DecimalField(max_digits=10, decimal_places=7)
	longitude = DecimalField(max_digits=10, decimal_places=7)
	Location_Coordinates = StringField(max_length=50, blank=True, null=True)
	Subtown = StringField(max_length=50, blank=True, null=True)
	Total_Num_Beds = IntField(blank=True, null=True)
	Facilities = StringField(max_length=50, blank=True, null=True)
	District_ID = StringField(max_length=50, blank=True, null=True)
	Specialties = ListField(StringField(max_length=50, blank=True, null=True))
	Town = StringField(max_length=50, blank=True, null=True)
	Website = StringField(max_length=50, blank=True, null=True)
	Number_DoctorVillage = IntField(blank=True, null=True)
	State_ID = StringField(max_length=50 , blank=True, null=True)

class Checkup_Details(EmbeddedDocument):
	date = DateTimeField(blank=True, null=True)
	hospital_id = StringField(max_length=50)
	doctor = StringField(max_length=50)
	symptoms = ListField(StringField(max_length=50))
	provisional_diagnosis = ListField(StringField(max_length=50))
	severity = IntField()

class Prescription(EmbeddedDocument):
	prescription_id = StringField(max_length=50)
	medicines = ListField(EmbeddedDocumentField('Medicine'))
	

class Medicine(EmbeddedDocument):
	medicine_name = StringField(max_length=50)
	morning = FloatField(required=False)
	afternoon = FloatField(required=False)
	evening = FloatField(required=False)
	no_of_days = IntField()


class Patient(Document):
	patient_id = StringField(max_length=50)
	password = StringField(max_length=50)
	name = StringField(max_length=100)
	phone1 = StringField(max_length=15)
	phone2 = StringField(max_length=15)
	email_id = EmailField(max_length=254,required=False)
	aadhar_no = DecimalField( max_digits=12, decimal_places=0)
	permanent_addr = StringField(max_length=250)
	local_addr = StringField(max_length=250)
	dob = StringField(null=True, blank=True)
	gender = StringField(max_length=1)
	profession = StringField(max_length=50)
	marital_status = StringField(max_length=1)
	blood_grp = StringField(max_length=10)
	spouse_name = StringField(max_length=50,required=False)
	checkup = ListField(EmbeddedDocumentField('Checkup_Details'))
	prescription = ListField(EmbeddedDocumentField('Prescription'),blank=True,null=True)


class Pharmacist(Document):
	pharmacist_id = StringField(max_length=50)
	password = StringField(max_length=50)
	name = StringField(max_length=100)
	phone1 = StringField(max_length=15)
	phone2 = StringField(max_length=15)
	email = EmailField(max_length=254,required=False)
	address = StringField(max_length=100)
	registration_no = StringField(max_length=50)

 
#Sahyadri = Hospital(hospital_id="PMCH001",name="Sahyadri", phone_no="12345",email_id="abc@gmai.com",facilties=["MRI","X-ray"])
#Sahyadri.save()
 
 
#for e in Hospital.objects.all():
#	print(e["registration_no"],e["hospital_id"])
