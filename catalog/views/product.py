from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from catalog import models as cmod 
from django import forms
from datetime import datetime

utc_time = datetime.utcnow()

@view_function
def process_request(request, product:cmod.Product):
    pimages = product.image_urls()
    return request.dmp.render('product.html', {
        'product': product,
        'utc_time': utc_time,
        'pimages': pimages,
    })

#tile ajax endpoint
@view_function
def tile(request, product:cmod.Product):
    return request.dmp.render('product.tile.html', {
        'product': product,
    })