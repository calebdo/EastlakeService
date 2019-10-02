from django_mako_plus import view_function, jscontext
from catalog import models as cmod 
from datetime import datetime, timezone
import math 

ITEMS_PER_PAGE = 8

@view_function
def process_request(request, category:cmod.Category=None, page:int=1):
    #products = cmod.Product.objects.filter(status="A") ONLY ACTIVE
    products = cmod.Product.objects.all() #all
    
    if category is not None:
        products = products.filter(category=category)

    products = products[(page - 1) * ITEMS_PER_PAGE: page * ITEMS_PER_PAGE]
    
    utc_time = datetime.utcnow()
    context = {
        # sent to index.html:
        'utc_time': utc_time,
        # sent to index.html and index.js:
        jscontext('utc_epoch'): utc_time.timestamp(),
        'category': category,
        'products': products,
        'page': page,
        'numpages': math.ceil(products.count() / ITEMS_PER_PAGE),
    }

    return request.dmp.render('index.html', context)
    