from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator


class Qualification(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
   
   
class JobSeeker(models.Model):
    qualification_id = models.ForeignKey(Qualification, on_delete=models.SET_NULL,null=True)
    position_id = models.ForeignKey(Position, on_delete=models.SET_NULL,null=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField()
    work_experience = models.PositiveIntegerField()
    current_police_check = models.BooleanField(default=False)
    children_check = models.BooleanField(default=False)
    address = models.CharField(max_length=60)
    cv = models.FileField(upload_to="cv_pdf")
    qualification_pdf = models.FileField(upload_to="qualification_pdf")
    created = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} id no {self.id}"


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.PositiveBigIntegerField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self) -> str:
        return f"{self.name} -> {self.subject}"


class Service(models.Model):
    title = models.CharField(max_length=200,unique=True)
    sub_content = models.TextField(null=True,blank=True)
    main_content = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to="homecare",null=True,blank=True)



    def __str__(self) -> str:
        return f"{self.title}"




class Point(models.Model): 
    service = models.ForeignKey(Service,on_delete=models.SET_NULL,null=True,related_name='points')
    name = models.CharField(max_length=100)



    def __str__(self) -> str:
        return f"{self.service.title} - {self.name}"




class Vacancy(models.Model):
    role_title = models.CharField(max_length=100,null=True,blank=True)
    job_title = models.CharField(max_length=100,null=True,blank=True)
    proposed_commencement_Date = models.DateField()
    attachment_position_description = models.FileField(upload_to="vacancy_attachment")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.PositiveBigIntegerField()
    additional_info = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

    


    def __str__(self) -> str:
        return f"{self.job_title} -> {self.job_title}"
        




class JobPost(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    deadline = models.DateTimeField(blank=True,null=True)
    content = RichTextField()



    def __str__(self) -> str:
        return f"{self.title}"


class TimeSheet(models.Model):
    pdf = models.FileField(upload_to="timesheet",validators=[FileExtensionValidator( ['pdf'])])

    def save(self, *args, **kwargs):
        if not self.pk:
           TimeSheet.objects.all().delete()
        super(TimeSheet, self).save(*args, **kwargs)
        
    



