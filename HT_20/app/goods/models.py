from django.db import models


class Base(models.Model):
    title = \
        models.CharField(max_length=60, unique=True)
    price = \
        models.PositiveIntegerField(default=0)
    count = \
        models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Guitar(Base):
    description = \
        models.TextField(default='description')
    # material_body = \
    #     models.CharField(max_length=50)
    # material_fretboard = \
    #     models.CharField(max_length=50)
    # guitar_pickups = \
    #     models.CharField(max_length=50, null=True, blank=True)
    # lads = \
    #     models.PositiveSmallIntegerField(default=18)
    # color = \
    #     models.CharField(max_length=50, default='натуральный')
    products = \
        models.ForeignKey('CategoryOfGuitar', on_delete=models.CASCADE)


# class SoundAmplifier(Base):
#     power =\
#         models.CharField(max_length=10),
#     size_dynamic =\
#         models.PositiveSmallIntegerField()
#     weight =\
#         models.PositiveSmallIntegerField()


class CategoryOfGuitar(models.Model):
    name = \
        models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Basket(models.Model):
    user_id = \
        models.PositiveIntegerField()
    product_id = \
        models.PositiveIntegerField()
