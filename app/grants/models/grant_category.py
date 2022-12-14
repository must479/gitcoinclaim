from django.db import models
from django.utils.translation import gettext_lazy as _

from economy.models import SuperModel


# TODO: REMOVE
class GrantCategory(SuperModel):

    category = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        help_text=_('Grant Category'),
    )

    def __str__(self):
        """Return the string representation of a Grant Category."""
        return f"{self.category}"
