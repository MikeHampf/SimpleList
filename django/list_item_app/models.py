from django.db import models
from listers_app.models import Lister
from .validators import validate_item_and_notes

class To_do_item(models.Model):
    lister_id = models.ForeignKey(Lister, on_delete=models.CASCADE, null=False)
    date_added = models.DateField(auto_now=True)
    item = models.CharField(max_length=128, null=False, validators=[validate_item_and_notes])
    notes = models.TextField(max_length=512, null=True, validators=[validate_item_and_notes])
    done = models.BooleanField(default=False)
