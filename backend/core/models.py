from django.db import models
import random


def get_system_code(description):
    while True:
        new_code = random.randint(100000000000, 999999999999 )
        code, created = SystemCode.objects.get_or_create(code=new_code)
        if created:
            code.description = description
            code.save()
            return new_code


class CoreModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de alteração')    
    active = models.BooleanField(default=True, blank=False, null=False, verbose_name='Ativo')

    class Meta:
        abstract = True


class SystemModel(CoreModel):
    code = models.CharField(max_length=12, default="", verbose_name='Código', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = get_system_code(self._get_verbose_name())
        super().save(*args, **kwargs)

    def _get_verbose_name(self):
        return self._meta.verbose_name

    class Meta:
        abstract = True


class SystemCode(CoreModel):
    code = models.CharField(max_length=12, default="", verbose_name='Código', blank=True, null=True)
    description = models.CharField(max_length=50, default="", verbose_name='Classe', blank=True, null=True)
    
    def __str__(self) -> str:
        return "Código: {}   Descrição: {}".format(self.code, self.description)
    
    class Meta:
        verbose_name = 'Código'
        verbose_name_plural = 'Códigos'