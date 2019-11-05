from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django.contrib.auth.models import User
from django import forms

class PasswordRecovery(forms.Form):
    email = forms.EmailField(label='Email', max_length=254, required=True, help_text='Your school email address')
    class Meta:
        model = User
        fields = ('email')

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient = ""
    send_mail( subject, message, email_from, recipient_list )
    return redirect('/recoverDone/')

@view_function
def process_request(request):
    form = PasswordRecovery(request.POST)
    error = ""
    if request.method == 'POST':
        #print(form.email)
        if form.is_valid():
            form.email = form.cleaned_data['email']
            try:
                User.objects.get(email=form.email)
                subject = 'Eastlake Service Password Recovery'
                message = 'You requested to recover your password for the Eastlake Community Service Portal. Your password is ' + User.objects.get(email=form.email)
                email_from = settings.EMAIL_HOST_USER
                recipient = form.email
                send_mail( subject, message, email_from, recipient_list )
                return HttpResponseRedirect('/recoverDone/')
            except User.DoesNotExist:
                error = "This email was not found"
                return request.dmp.render('recover.html', {'form':form, 'error':error})
                
    else:
        form = PasswordRecovery()

    context = {
        'form': form,
        'error': error
    }
    return request.dmp.render('recover.html', context)