import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Temporary placeholder
TYPE_CHOICES = ("Page", "Alias", )


class ContentExpiry(models.Model):
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES
    )
    from_expiry_date = models.DateField(_("From Expiry Date"), default=datetime.date.today)
    to_expiry_date = models.DateField(_("To Expiry Date"), default=datetime.date.today)

    class Meta:
        verbose_name = _("Content Expiry")
