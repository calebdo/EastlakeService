from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required for password recovery. Input your school email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

@view_function
def process_request(request):
    if request.method == 'POST':
        f = SignUpForm(request.POST)
        if f.is_valid():
            f.save()
            username = f.cleaned_data.get('username')
            raw_password = f.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/newService/')
 
    else:
        f = SignUpForm()
     
    context = {
        'form': f
    }
    return request.dmp.render('create.html', context)
