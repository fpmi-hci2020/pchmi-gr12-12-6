from .models import Tickets
from django.forms import ModelForm

class TicketsForm(ModelForm):
    class Meta:
        model = Tickets
        fields = ["From", "Where", "Date", "Carrier", "Price"]
