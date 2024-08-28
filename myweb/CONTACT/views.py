from django.http import HttpResponse
from django.template import loader

def CONTACT(request):
  template = loader.get_template('CONTACT.html')
  return HttpResponse(template.render())