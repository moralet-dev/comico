from django.db import models


# ----------Coded attrs starts----------

class CodedAttributeAbstract(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=4, unique=True)

    class Meta:
        abstract = True


class ProductCategory(CodedAttributeAbstract):
    parent_category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, null=True, blank=True)


class Brand(CodedAttributeAbstract):
    description = models.TextField(max_length=2000, null=True, blank=True)


class Author(CodedAttributeAbstract):
    last_name = models.CharField(max_length=200)
    pseudonym = models.CharField(max_length=200, null=True, blank=True)

    country = models.CharField(max_length=100)

    bio = models.TextField(max_length=2000, null=True, blank=True)

    date_of_brith = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)

# ----------Coded attrs ends----------


# ----------Uncoded attrs starts----------

class PrintedProductAttrs(models.Model):
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)

    cover = models.CharField(max_length=100)
    count_of_pages = models.PositiveSmallIntegerField(max_length=4)

    width = models.DecimalField(max_digits=3, decimal_places=2)
    height = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.DecimalField(max_digits=2, decimal_places=3)

# ----------Uncoded attrs ends----------


# ----------Product models starts----------

class BaseProduct(models.Model):
    name = models.CharField(max_length=200)
    categoty = models.ForeignKey('ProductCategory', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_digital = models.BooleanField(default=False)
    product_code = models.CharField(max_length=100)

    date_create = models.DateTimeField(auto_now=True)
    date_edit = models.DateTimeField(auto_now_add=True)


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', blank=True)
    product = models.ForeignKey('BaseProduct', on_delete=models.CASCADE, related_name='images')


class Comics(models.Model):
    product = models.OneToOneField('BaseProduct', on_delete=models.CASCADE)
    attributes = models.OneToOneField('PrintedProductAttrs', on_delete=models.SET_NULL, null=True, blank=True)


class TShirt(models.Model):
    product = models.OneToOneField('BaseProduct', on_delete=models.CASCADE)

    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True, blank=True)

# ----------Product models ends----------
