from django.db import models

# Create your models here.
class patients(models.Model):
    firstName = models.CharField(max_length=50,null=True,blank=True)
    lastName = models.CharField(max_length=50,null=True,blank=True)
    DateOfBirth = models.DateField(null=False,blank=False)
    Sex = models.CharField(max_length=10,null=False,blank=False,choices={"male":"Male","fenale":"Female"})
    PlaceOfBirth = models.CharField(max_length=100,null=True,blank=True)
    Phone= models.CharField(max_length=10,null= True,blank=True)
    addrss= models.CharField(max_length=100,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)
    class Meta:
        db_table =  "patient"
        ordering = ['-created']

    def __str__(self):
        return f'{self.firstName}  {self.lastName}'
    
class doctors(models.Model):
    doctor_id = models.IntegerField(unique=True,null=False,blank=False)
    last_name = models.CharField(max_length=100,null=False,blank=False)
    first_name = models.CharField(max_length=100,null=False,blank=False)
    sex = models.CharField(max_length=6,null=False,blank=False,choices={'male':'Male','female':'Female'})
    dob = models.DateField(null=False,blank=False)
    pob = models.CharField(max_length=150,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table =  "doctor"
        ordering = ['-created']

    def __str__(self):
        return f'{self.last_name}  {self.first_name}'
    
class appoinment(models.Model):
    patient = models.ForeignKey(patients,on_delete=models.CASCADE)
    doctors = models.ForeignKey(doctors,on_delete=models.PROTECT)
    reason = models.TextField()
    date_appointment = models.DateTimeField(null=False,blank=False)
    status = models.CharField(max_length=20,null=False,blank=False,choices={'pending':'Pending','success':'Success'},default='pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)