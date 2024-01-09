from django.db import models

# Create your models here.
class User(models.Model):
    User_ID=models.IntegerField(primary_key=True)
    User_name=models.CharField(max_length=100)
    Email=models.EmailField()

    def __str__(self):
        return self.User_name
    
class Order(models.Model):
    User_ID=models.ForeignKey(User,on_delete=models.CASCADE)
    Order_no=models.IntegerField()
    Product_code=models.IntegerField()
    Order_loc=models.CharField(max_length=100)

    def __str__(self):
        return self.Order_loc

class Books(models.Model):
    Product_code=models.ForeignKey(Order,on_delete=models.CASCADE)
    Book_title=models.CharField(max_length=100)
    Price=models.IntegerField()

    def __str__(self):
        return self.Book_title