from django.views.generic import ListView
from cmdr. models import Employee

# Create your views here.

class loginpageview (ListView):
    model=Employee
    template_name="form.html"
