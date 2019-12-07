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
            help_text=_('Hectare + Shift + Date + Hectare squirrel number'),
            primary_key = True)

    Hectare = models.CharField(
            help_text=_('ID tag'))

    Shift = models.CharField(
            help_text=_('AM or PM'),
            choices = TIME)

    Date = models.DateField(
            help_text=_('Date when squirrel was spotted'))

    Hectare_Squirrel_Number = model.IntegerField(
            help_text=_('Number of squirrel sightings'))

    Age = models.CharField(
            help_text=_('Adult or Juvenile'),
            choices = AGE_CHOICES)

    Primary_Fur_Color = models.CharField(
            help_text=_('gray, cinnamon or black'),
            choices = FUR_COLOR)

    Highlight_Fur_Color = models.CharFirled(
            help_text=_('Highlight color'))

    Combination_of_Color = models.CharField(
            help_text=('Combination of primary and highlight fur color'))

    Color_Notes = models.CharField(
            help_text=_('Notes on color'))

    Location = models.CharField(
            help_text=_('Ground plane or above ground'),
            choices = LOCATION)

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

    Eating = models.BooleanField(
            help_text=_('True if squirrel was eating'))
    Foraging = models.BooleanField(
            help_text=_('True if squirrel was foraging'))

    Other_Activities = models.CharField(
            help_text=_('Other activity by squirrel'),
            blank=True)

    Kuks = models.BooleanField(
            help_text=_('Is  Squirrel kuking'),
            default=False
        )


    Quaas = models.BooleanField(
            help_text=_('Is  Squirrel quaaing'),
            default=False
        )

    Moans = models.BooleanField(
            help_text=_('Is Squirrel Moaning'),
            default=False
        )

    Tail_flags = models.BooleanField(
            help_text=_('Is Squirrel flagging tail'),
            default=False
        )

    Tail_twitching = models.BooleanField(
            help_text=_('Is the Squirrel twitching tail'),
            default=False
        )

    Approaches = models.BooleanField(
        help_text=_('Is Squirrel approaching human'),
        default=False
        )

    Indifferent = models.BooleanField(
            help_text=_('Is squirrel indifferent to human'),
            default=False
        )
    Runs_from = models.BooleanField(
            help_text=_('Is Squirrel running from human'),
            default=False
        )

    AM = 'AM'
    PM = 'PM'

    ADULT = 'ADULT'
    JUVENILE = 'JUVENILE'

    Gray = 'GRAY'
    Cinnamon = 'CINAMMON'
    Black = 'BLACK'

    AGE_CHOICES = (
            (ADULT, 'ADULT'),
            (JUVENILE, 'JUVENILE'))

    TIME = (
            (AM, 'AM'),
            (PM, 'PM'))

    FUR_COLOR = (
            (Gray, 'GRAY'),
            (Cinnamon, 'CINNAMON'),
            (Black, 'BLACK'))

    GROUND_PLANE = 'GROUND PLANE'
    ABOVE_GROUND = 'ABOVE GROUND'

    LOCATION= (
            (GROUND_PLANE, 'GROUND PlANE'),
            (ABOVE_GROUND, 'ABOVE GROUND'))

    def __str__(self):
        return self.Unique_squirrel_ID


