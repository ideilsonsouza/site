from django.db import models
from backend.core.models import CoreModel, SystemModel


class SysClient(SystemModel):
    name = models.CharField(max_length=196, null=False, verbose_name ='Nome')
    doc = models.CharField(max_length=30, null=False, unique=True, verbose_name ='Documento')
    phone = models.CharField(max_length=30, null=True, blank=True, unique=True,  verbose_name ='Nome')

    def __str__(self) -> str:
        return "{} - {}".format(self.doc, self.name)

    class Meta(SystemModel.Meta):
        ordering=['name']
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"