# pokedex/models.py

from django.db import models

class Pokemon(models.Model):
    name_english = models.CharField(max_length=255, default='')
    name_japanese = models.CharField(max_length=255, default='')
    name_chinese = models.CharField(max_length=255, default='')
    name_french = models.CharField(max_length=255, default='')
    type_1 = models.CharField(max_length=50, default='')
    type_2 = models.CharField(max_length=50, blank=True, null=True, default='')
    hp = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    sp_attack = models.IntegerField(default=0)
    sp_defense = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    species = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    height = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    egg_group_1 = models.CharField(max_length=50, default='')
    egg_group_2 = models.CharField(max_length=50, blank=True, null=True, default='')
    ability_1_name = models.CharField(max_length=100, default='')
    ability_1_hidden = models.BooleanField(default=False)
    ability_2_name = models.CharField(max_length=100, blank=True, null=True, default='')
    ability_2_hidden = models.BooleanField(default=False)
    gender_ratio = models.CharField(max_length=50, default='')
    sprite = models.URLField(default='')
    thumbnail = models.URLField(default='')
    hires_image = models.URLField(default='')

    def __str__(self):
        return self.name_english
