from django.db import models


# Create your models here.

class ThemeModel(models.Model):
    # Example: https://www.premiumtrendz.co.uk/
    theme_url = models.URLField()
    theme_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.theme_url
