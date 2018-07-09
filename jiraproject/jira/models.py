from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission


class Company(models.Model):
    company_name = models.CharField(max_length=50,unique=True)
    company_address = models.CharField(max_length=50)
    company_description = models.CharField(max_length=100)
    company_code = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.company_name

class user1(AbstractUser):

   # empname = models.CharField(max_length=100, unique=True)
    ROLES = (
        ('Admin', 'Admin'),
        ('Employee', 'Employee'),
        ('Team Lead', 'Team lead'),)
    #)
    #roles = models.CharField(max_length=30, choices=ROLES)
   # password=models.CharField(default=None,max_length=30)
   # username = models.CharField(unique=True,default=None,max_length=30)





class Project(models.Model):
    COMPANY = models.ForeignKey(Company, on_delete=models.CASCADE)
    Project_name = models.CharField(max_length=100)
    start_date = models.DateField()
    deadline_date = models.DateField()
    project_code = models.CharField(max_length=20, unique=True)
    teamleader = models.ForeignKey(user1,on_delete=models.CASCADE,related_name='teamlead')
    Assigned_employee = models.ManyToManyField(user1,related_name='employee')

    def __str__(self):
         return self.Project_name

    class Meta:
        permissions = (('reg' , 'can add a user'),('project_detail' , 'can see project detail'),('make_project', 'can add project'),
                       ('view_company','can view company'),('make_company' , 'can add company' ),('view_module','can view module'),)




#class Employee(models.Model):
   # emp_id = models.CharField(max_length=30, unique=True)
   # emp_name = models.CharField(max_length=50)
    #emp_salary = models.IntegerField()
   # emp_age = models.IntegerField()
   # ROLES = (
       # ('Admin', 'Admin'),
       # ('Employee', 'Employee'),
       # ('Team Lead', 'Team lead'),
   # )
   # roles = models.CharField(max_length=30, choices=ROLES)

class Modules(models.Model):
    PROJECT=models.ForeignKey(Project, on_delete=models.CASCADE)
    Module_name=models.CharField(max_length=30)
    Assigned_to=models.ForeignKey(user1,on_delete=models.CASCADE)



   # assigned_to=models.ForeignKey(user1,on_delete=models.CASCADE,default='none')
    #Assigned_employee=models.ForeignKey(Employee,on_delete=models.CASCADE)




