from django.db import models
from django.urls import reverse 

class Department(models.Model):
    name = models.CharField("Назва кафедри", max_length=200)
    head = models.CharField("Завідувач кафедри", max_length=200)
    
    coordinator_name = models.CharField("Ім'я координатора кафедри", max_length=200, blank=True)
    coordinator_contact = models.CharField("Контакт координатора кафедри", max_length=200, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('department_detail', args=[str(self.id)])



class Coordinator(models.Model):
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    description = models.TextField()
    disciplines_year1 = models.TextField("Дисципліни (1-й рік)", blank=True)
    disciplines_year2 = models.TextField("Дисципліни (2-й рік)", blank=True)
    disciplines_year3 = models.TextField("Дисципліни (3-й рік)", blank=True)
    disciplines_year4 = models.TextField("Дисципліни (4-й рік)", blank=True)

    
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="programs")

    
    coordinator = models.ForeignKey(Coordinator, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class HomePage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    contacts = models.TextField()

    def __str__(self):
        return "Контент головної сторінки"
    
class Teacher(models.Model):
    name = models.CharField("Ім'я", max_length=150)
    position = models.CharField("Посада", max_length=150)
    degree = models.CharField("Науковий ступінь", max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="teachers")

    def __str__(self):
        return self.name