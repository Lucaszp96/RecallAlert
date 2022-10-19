from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __repr__(self):
        return self.title


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    sn = models.CharField(max_length=20)
    defects = models.CharField(max_length=100)
    hazards = models.CharField(max_length=100)
    consumers = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    traders = models.CharField(max_length=100)
    sold_venues = models.CharField(max_length=100)
    avaiable_sale_date = models.CharField(max_length=100)
    content = models.CharField(max_length=200)

    created_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["-created_date"]

    def __repr__(self):
        return f"{self.product_name} - {self.sn} - {self.created_date}"


class Message(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    product_sn = models.CharField(max_length=20)
    product_name = models.CharField(max_length=20)
    product_detail = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __repr__(self):
        return f"{self.name} - {self.phone} - {self.created_date}"
