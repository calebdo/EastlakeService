from django.db import models
from datetime import datetime
from django.conf import settings

class Category(models.Model):
    last_modified = models.DateTimeField(auto_now=True) 
    name = models.TextField()

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True) 
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    status = models.TextField(db_index=True, choices=STATUS_CHOICES, default='A')
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    reorder_trigger = models.IntegerField()
    reorder_quantity = models.IntegerField()

    def image_url(self):
        return self.image_urls()[0]
        

    def image_urls(self):
        urls = []
        pimages = ProductImage.objects.filter(product=self)
        for pi in pimages:
            urls.append(pi.image_url())
        if (urls.__len__() == 0):
            urls.append(settings.STATIC_URL + "catalog/media/products/notfound.jpg")
        return urls
                
            #elif (pi.image_url() is None):
            #    return urls
            #else:
            #    return settings.STATIC_URL + "catalog/media/products/notfound.jpg"

            #else:
            #    urls.append(settings.STATIC_URL + "catalog/media/products/notfound.jpg")
            #    print(urls)
            #    return urls

#CHECK QUOTATIONS ON STUFF??

class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    filename = models.TextField() 

    def image_url(self):
        #if (self.product is None):
        #    return settings.STATIC_URL + "catalog/media/products/notfound.jpg"
        #else:
        #    return settings.STATIC_URL + "catalog/media/products/" + self.filename
        return settings.STATIC_URL + "catalog/media/products/" + self.filename