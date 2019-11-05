from django import forms
from django_mako_plus import view_function
from homepage.models import Service
from django.contrib.auth.models import User


@view_function
def process_request(request):
    # create/check/handle the form
    form = ServiceForm()

     # If this is a POST request then process the Form data
    
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        # Check if the form is valid:
        if form.is_valid(): 
        # set up the context and render
            s = Service()
            s.club = form.cleaned_data.get('club') 
            s.contactName = form.cleaned_data.get('contactName') 
            s.contactPhone = form.cleaned_data.get('contactPhone') 
            s.dateCompleted = form.cleaned_data.get('dateCompleted') 
            s.description = form.cleaned_data.get('description') 
            s.hours = form.cleaned_data.get('hours') 
            s.accurate = form.cleaned_data.get('accurate') 
            s.performedByID = request.user.id
            s.save()


    context = {
        'form': form,
    }
    return request.dmp.render('newService.html', context)



class ServiceForm(forms.Form):
    CLUB_CHOICES = (
        ('G', 'General'),
        ('K', 'Key Club'),
    )
    club = forms.ChoiceField(choices=CLUB_CHOICES)
    contactName = forms.CharField()
    contactPhone = forms.CharField()
    dateCompleted = forms.DateField()
    description = forms.CharField()
    hours = forms.DecimalField()
    accurate = forms.BooleanField()

