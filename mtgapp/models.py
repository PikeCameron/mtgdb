from django.db import models

# Create your models here.

class Card_Sub_Type(models.Model):
    sub_type = models.CharField(max_length=30)

    def __str__(self) :
        output = str(self.sub_type)
        return (output)

class Card_Type(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self) :
        output = str(self.type)
        return (output)

class Set(models.Model):
    title = models.CharField(max_length=50) 

    def __str__(self) :
        output = str(self.title)
        return (output)

class Card(models.Model):
    card_name = models.CharField(max_length=45, blank=False)
    card_type = models.ManyToManyField(Card_Type, blank=False)
    card_sub_type = models.ManyToManyField(Card_Sub_Type, blank=False)
    color = models.CharField(max_length=20, blank=False)
    set = models.ManyToManyField(Set, blank=False)
    rarity = models.CharField(max_length=45, blank=False)
    foil = models.BooleanField()
    extended = models.BooleanField()
    retro = models.BooleanField()
    legendary = models.BooleanField()
    quantity = models.IntegerField(default=0, blank=False)

    def __str__(self) :
        return (self.card_name)

    def save(self):
        self.card_name = self.card_name.upper()
        super(Card, self).save() # Calls the "real" save() metho