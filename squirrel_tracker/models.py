from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class squirrel(models.Model):
    X = models.DecimalField(
            help_text = _('Longitude')
            )

    Y = models.DecimalField(
            help_text = _('Latitude'))
    Unique_squirrel_ID = models.CharField(
            help_text=_('Hectare + Shift + Date + Hectare squirrel number'))

    Hectare = models.CharField(
            help_text=_('ID tag'))

    Shift = models.CharField(
            help_text=_('AM or PM'))

    Date = models.DateField(
            help_text=_('Date when squirrel was spotted'))

    Hectare_Squirrel_Number = model.IntegerField(
            help_text=_('Number of squirrel sightings'))

    Age = models.CharField(
            help_text=_('Adult or Juvenile'))

    Primary_Fur_Color = models.CharField(
            help_text=_('gray, cinnamon or black'))

    Highlight_Fur_Color = models.CharFirled(
            help_text=_('Highlight color'))

    Combination_of_Color = models.CharField(
            help_text=('Combination of primary and highlight fur color'))

    Color_Notes = models.CharField(
            help_text=_('Notes on color'))

    Location = models.CharField(
            help_text=_('Ground plane or above ground'))

    Above_Ground_Sighter_Measurement = models.CharField(
            help_text=_('False if location is above ground'))

    Specific_Location = models.CharField(
            help_text=_('Comments on the squirrel location'))

    Running = models.BooleanField(
            help_text=_('True if squirrel was running'))

    Chasing = models.BooleanField(
            help_text=_('True if squirrel was chasing'))

    Climbing = models.BooleanField(
            help_text=_('True if squirrel was climbing'))
