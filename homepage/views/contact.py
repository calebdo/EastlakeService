from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone

@view_function
def process_request(request):
    # did user submit?
    if request.method == "POST":
        #check variables
        # assume user does it wrong
        print(request.POST['yourname'])
        print(request.POST['youremail'])
        #if user did it right
        # do the work (reset passwd, create acct, etc. then return HttpResponseRedirect('/somewhere/else/'))
    utc_time = datetime.utcnow()
    context = {
        # sent to index.html:
        'utc_time': utc_time,
       
    }
    return request.dmp.render('contact.html', context)