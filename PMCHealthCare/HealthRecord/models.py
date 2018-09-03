from mongoengine import *
from django.utils import timezone
import datetime
from datetime import datetime
from django.db.models import (
    DateField, DateTimeField, IntegerField, TimeField, Transform,
)
from PMCHealthCare.settings import DBNAME

connect(DBNAME)

class Hospital(Document):
	hospital_id = StringField(max_length=50)
	name = StringField(max_length=100)
	phone_no = StringField(max_length=15)
	email_id = StringField(max_length=254,required=False)
	address = StringField(max_length=100)
	registration_no = StringField(max_length=50)
	facilties = ListField(StringField(max_length=50))
	doctors_associated = SortedListField(StringField(max_length=50))

class Doctor(Document):
	doctor_id = StringField(max_length=50)
	name = StringField(max_length=100)
	phone_no = StringField(max_length=15)
	email_id = StringField(max_length=254,required=False)
	registration_no = StringField(max_length=50)
	qualtification = ListField(StringField(max_length=50))
	hospitals_associated = SortedListField(StringField(max_length=50))

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
	dosage = StringField(max_length=10)
	morning = FloatField(required=False)
	afternoon = FloatField(required=False)
	evening = FloatField(required=False)
	no_of_days = IntField()


class Patient(Document):
	patient_id = StringField(max_length=50)
	name = StringField(max_length=100)
	phone_no = StringField(max_length=15)
	email_id = EmailField(max_length=254,required=False)
	aadhar_no = DecimalField( max_digits=12, decimal_places=0)
	permanent_addr = StringField(max_length=250)
	local_addr = StringField(max_length=250)
	dob = DateField(null=True, blank=True)
	gender = StringField(max_length=1)
	profession = StringField(max_length=50)
	marital_status = StringField(max_length=1)
	blood_grp = StringField(max_length=10)
	spouse_name = StringField(max_length=50,required=False)
	checkup = EmbeddedDocumentField('Checkup_Details')
	prescription = EmbeddedDocumentField('Prescription')


class Pharmacist(Document):
	pharmacist_id = StringField(max_length=50)
	name = StringField(max_length=100)
	phone_no = StringField(max_length=15)
	email_id = EmailField(max_length=254,required=False)
	address = StringField(max_length=100)
	registration_no = StringField(max_length=50)

 
Sahyadri = Hospital(hospital_id="PMCH001",name="Sahyadri", phone_no="12345",email_id="abc@gmai.com",facilties=["MRI","X-ray"])
Sahyadri.save()
 
 
#for e in Employee.objects.all():
    #print (e["id"], e["name"], e["age"])"""


