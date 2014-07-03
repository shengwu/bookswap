from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *

def home(request):
    return render_to_response('home.html', locals(),
            context_instance=RequestContext(request))
