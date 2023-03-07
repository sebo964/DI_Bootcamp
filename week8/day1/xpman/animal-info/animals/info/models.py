# from django.db import models

# # Create your models here.

# # class animals that takes

# # id
# # legs – an integer, the number of legs the animal has
# # weight – the average weight of an adult animal of this type
# # height – the average height of an adult animal of this type
# # speed – the maximum speed at which this animal can move
# # family – the family to which this animal belongs. (Must reference the Family model - see below).


# class Animal(models.Model):
#     id = models.IntegerField(primary_key=True)
#     legs = models.IntegerField()
#     weight = models.IntegerField()
#     height = models.IntegerField()
#     speed = models.IntegerField()
#     family = models.ForeignKey("Family", on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.id} {self.legs} {self.weight} {self.height} {self.speed} {self.family}"


# class Family(models.Model):
#     # family takes id and name
#     id = models.IntegerField(primary_key=True)
#     name = models.TextField

#     def __str__(self) -> str:
#         return f"{self.id} {self.name}"
