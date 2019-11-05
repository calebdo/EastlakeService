from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django import forms

@view_function
def process_request(request):
    context = {
       
    }
    return request.dmp.render('recoverDone.html', context)