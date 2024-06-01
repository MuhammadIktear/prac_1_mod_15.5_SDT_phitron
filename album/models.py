from django.db import models
import datetime
from musician.models import Musician
from django.forms.widgets import NumberInput

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=50)
    release_date = models.DateField(default=datetime.date.today)
    
    CHOICE = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    rating = models.CharField(max_length=1, choices=CHOICE, default='1')
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.album_name} by {self.musician.first_name}'
