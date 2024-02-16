from django.db import models
from backend.core.models import CoreModel, SystemModel

class SysProduct(SystemModel):
    name = models.CharField(max_length=196, null=False, verbose_name ='Nome')
    description = models.CharField(max_length=196, null=False, verbose_name ='Descrição')
    name = models.CharField(max_length=196, null=False, verbose_name ='Nome')