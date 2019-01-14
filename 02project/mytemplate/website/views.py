from django.views.generic import TemplateView

class homepage(TemplateView):
    template_name='home.html'

class aboutpage(TemplateView):
    template_name='about.html'

class contactuspage(TemplateView):
    template_name='contactus.html'
