from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class Flow(models.Model):
    STATE_CHOICES = (('PA', 'Pennsylvania'),
                     ('MD', 'Maryland'),
                     ('VA', 'Virginia'),
                     ('WV', 'West Virginia'))

    site_id = models.CharField("USGS Site ID", max_length=8)
    name = models.CharField("Site Name", max_length=200)
    weather_url = models.URLField("Weather URL", blank=True, null=True)
    upper_level = models.FloatField("Upper Level", blank=True, null=True)
    lower_level = models.FloatField("Lower Level", blank=True, null=True)
    river_class = models.CharField("Class", max_length=5, blank=True, null=True)
    travel = models.CharField("Travel", max_length=100, blank=True, null=True)  # come on travis you can do better than that
    latest_height = models.FloatField("Latest Height", blank=True, null=True)
    latest_flow = models.IntegerField("Latest Flow", blank=True, null=True)
    weather_locale = models.CharField("Weather Locale", max_length=200, blank=True, null=True)  # also I should be able to automate this
    aw_url = models.URLField("American Whitewater URL", blank=True, null=True)
    height_change = models.FloatField("Change in height", blank=True, null=True)
    flow_change = models.IntegerField("Change in flow", blank=True, null=True)
    temperature = models.FloatField("Temperature", blank=True, null=True)
    state = models.CharField("State", max_length=2, choices=STATE_CHOICES)

    def __unicode__(self):
        return self.name


class UpdateLog(models.Model):
    time = models.DateTimeField(auto_now=True)
    success = models.BooleanField(default=True)
