from django.db import models

# We have used after changing setting for shop and the we have made a migration by running command (python manage.py make migration) :-This will make migration but not apply it, migratioin is about making this table below
# Then we have used (python manage.py migrate) it is used to apply migration
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category  = models.CharField(max_length=50,default="")
    subcategory  = models.CharField(max_length=50,default="")
    price =models.IntegerField(default=0)
    desc =  models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name