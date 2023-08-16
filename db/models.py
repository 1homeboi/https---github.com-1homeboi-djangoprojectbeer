from django.db import models
from manage import init_django

init_django()

class Location(models.Model):
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200) 
    def __str__(self):
        return self.city
    
class Store(models.Model):
    store_title = models.CharField(max_length=200)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.store_title
    
class Packaging(models.Model):
    packaging_title = models.CharField(max_length=200)
    capacity = models.IntegerField()
    def __str__(self):
        return self.packaging_title
    
class Storage(models.Model):
    storage_title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.storage_title
    
class Company(models.Model):
    company_title = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    def __str__(self):
        return self.company_title
    
class Beer(models.Model):
    beer_title = models.CharField(max_length=200)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    sku_title = models.CharField(max_length=200)
    price = models.IntegerField()
    expiry_date = models.DateField()
    volume = models.IntegerField()
    storage_id = models.ForeignKey(Storage, on_delete=models.CASCADE, null=True)
    Packaging_id = models.ForeignKey(Packaging, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.beer_title
    
class Sales(models.Model):
    quantity = models.IntegerField()
    sales_date = models.DateField()
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    beer_id = models.ForeignKey(Beer, on_delete=models.CASCADE, null=True)
    total_amount = models.IntegerField()
    def __str__(self):
        return f"Продажи #{self.pk} ({self.quantity} штук) на {self.sales_date}"
    
class SalesBeer(models.Model):
    beer_id = models.ForeignKey(Beer, on_delete=models.CASCADE, null=True)
    sales_id = models.ForeignKey(Sales, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.beer_id
    
class Inventory(models.Model):
    beer_id = models.ForeignKey(Beer, on_delete=models.CASCADE, null=True)
    storage_id = models.ForeignKey(Storage, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    def __str__(self):
        return f"Инвентарь #{self.pk} ({self.quantity}) в {self.storage_id}"