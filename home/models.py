from django.db import models

from admin_singleton.models import SingletonModel



# Create your models here.
class Mark(models.Model):
   name = models.CharField(max_length=30)

   def __str__(self):
       return self.name

class Color(models.Model):
   name = models.CharField(max_length=30)

   def __str__(self):
       return self.name
   
class Drive(models.Model):
   name = models.CharField(max_length=30)

   def __str__(self):
       return self.name

class Model(models.Model):
   name = models.CharField(max_length=30)

   def __str__(self):
       return self.name

class Car(models.Model):
   mark = models.ForeignKey(Mark, on_delete=models.PROTECT)
   model = models.ForeignKey(Model, on_delete=models.PROTECT)
   color = models.ForeignKey(Color, on_delete=models.PROTECT)
   drive = models.ForeignKey(Drive, on_delete=models.PROTECT)
   year = models.IntegerField()
   price = models.IntegerField()
   
class Settings(SingletonModel):
   title = models.CharField(max_length=30)
   phone_number = models.CharField(max_length=30)

   def __str__(self):
      return 'Налаштування домашньої сторінки'
   
class Feedback(models.Model):
   user_name = models.CharField(max_length=30)
   feedback_text = models.CharField(max_length=1000)

   def __str__(self):
      return self.user_name
   
class RiflesPage(models.Model):
   picture = models.ImageField(upload_to="rifles_page", null=True)
   price = models.CharField(max_length=10)
   model = models.CharField(max_length=30)
   name = models.CharField(max_length=30)

   def __str__(self):
      return self.name