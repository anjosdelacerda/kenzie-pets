from math import log

from django.db import models

# Create your models here.

class Gender(models.TextChoices):
    MALE = "Macho"
    FEMALE = "Fêmea"
    UNKNOW = "Não informado"


class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15, choices=Gender.choices, default=Gender.UNKNOW)

    group = models.ForeignKey(
        'groups.Group', 
        on_delete=models.CASCADE,
        related_name='animals',
        null=True,
        )

    traits = models.ManyToManyField(
        'traits.Trait', related_name='traits',
        )
    
    def convert_dog_age_to_human_years(self):
        human_age = 16 * log(self.age) + 31
        return human_age

    def __repr__(self) -> str:
        return f"<Animal {self.id} - {self.name}>"

