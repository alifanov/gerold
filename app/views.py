# Create your views here.

from django.views.generic.simple import direct_to_template

def lab(req):
    return direct_to_template(req, 'lab_raphael.html', {})