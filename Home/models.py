from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email= models.EmailField(max_length=100)
    Message = models.TextField(max_length=300)

    def __str__(self):
        return self.Name

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    img = models.ImageField(upload_to='pizza' )
    
    def __str__(self):
        return self.Name
    
class Burger(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    img = models.ImageField(upload_to='Burger' )

    def __str__(self):
        return self.Name
    
class Shawarma_pltr(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    img = models.ImageField(upload_to='Shwarma-pltr' )

    def __str__(self):
        return self.Name
    
class Appetizer(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    img = models.ImageField(upload_to='Appetizer' )

    def __str__(self):
        return self.Name
    
class Sandwiche(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    img = models.ImageField(upload_to='Sandwiche' )

    def __str__(self):
        return self.Name
    
class Pasta_Roll(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    img = models.ImageField(upload_to='Pasta-Rol' )

    def __str__(self):
        return self.Name
    


   
class Address(models.Model):
    ID = models.AutoField(primary_key=True)
    City_name = models.CharField(max_length=100)
    street_No= models.CharField(max_length=100)
    Zip_code= models.CharField(max_length=100 , default="")
    Phone_NO = models.CharField(max_length=100)
    

    def __str__(self):
        return str(self.ID) + "-" + self.City_name  


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email= models.EmailField(max_length=100)
    Password = models.CharField(max_length=100 , default="")
    address = models.ForeignKey(Address , on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.id) + "-" + self.Name 

class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    Duty_timing = models.CharField(max_length=100)
    address = models.ForeignKey(Address , on_delete=models.CASCADE)
    

    def __str__(self):
        return self.Name
    

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    Total_price = models.CharField(max_length=100)
    No_of_items = models.IntegerField()   

    def __str__(self):
        return str(self.id) + "-" + str(self.No_of_items) 
    
 
class Cartitem(models.Model):
    Cart_id = models.ForeignKey(Cart , on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Quantity = models.IntegerField()    

    def __str__(self):
        return str(self.Cart_id) + "-" + self.Name 
    
 
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE) 
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE) 
    Date_time = models.DateTimeField()

    def __str__(self):
        return str(self.id) + "  -  " + str(self.Date_time)
    
 