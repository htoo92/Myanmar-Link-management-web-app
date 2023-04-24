from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)
    create_date = models.DateField(auto_now=True, auto_now_add=True)
    update_date = models.DateField(auto_now=True, auto_now_add=True)


    def __str__(self):
        return self.name

class officeuser(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    create_date = models.DateField(auto_now=True, auto_now_add=True)
    update_date = models.DateField(auto_now=True, auto_now_add=True)
    

    def __str__(self):
        return self.name


class Internetcustomer(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    netid = models.CharField(max_length=50)
    house_or_housenumber =  models.CharField(max_length=50)
    street = models.CharField(max_length=225)
    ward = models.CharField(_ax_length=225)

    

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


