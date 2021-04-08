from django.db import models
# name - CharField
# price - FloatField
# description - TextField
# count - IntegerField
# is_active - BooleanField


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()
    def to_json(self):
        return {
            'id':self.id,
            'price':self.price,
            'description':self.description,
            'count':self.count,
            'is_active':self.is_active,
        }



class Category(models.Model):
    name = models.CharField(max_length=255)
    def to_json(self):
        return {
            'name':self.name
        }
