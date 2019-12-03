from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class squirrel(models.Model):
    X = models.DecimalField(
            help_text = _('Longitude')
            )
