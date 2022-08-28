from django.db import models


# Create your models here.

class Categorie(models.Model):
    Categories_Name = models.CharField(max_length=200, default="Category Name")

    def __str__(self):
        return self.Categories_Name


class Supplier(models.Model):
    Supplier_Name = models.CharField(max_length=200, default="Supplier Name")
    Phone_num = models.IntegerField(blank=True)
    Email = models.CharField(max_length=200, unique=True)


    def __str__(self):
        return self.Supplier_Name



class Product(models.Model):

    title = models.CharField(max_length=200, default="InventoryManagement Name")
    brand = models.CharField(max_length=200, default="Brand Name")
    price = models.IntegerField(blank=True)
    weight = models.CharField(max_length=200, default='N\A')
    categories = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=1)
    supplier= models.ForeignKey(Supplier, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.title



class Stock(models.Model):
    Quantity = models.IntegerField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.product.title +" - "+ str(self.Quantity)










