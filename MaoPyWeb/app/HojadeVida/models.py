from django.db import models

# Create your models here.
# Los modelos son una clase que devuelve un objeto

# Clase para el modelo Etnia
class etnia(models.Model):
    NomEtni = models.CharField(max_length = 50, verbose_name = "Grupo Étnico")

    class Meta:
        verbose_name = "Grupo Étnico"
        verbose_name_plural = "Grupos Étnicos"

    def __str__(self):
        return self.NomEtni

# Clase para el modelo Tido de Documento
class TipoDocu(models.Model):
    NomTido = models.CharField(max_length = 50, verbose_name = "Tipo de Documento")

    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipo de Documentos"

    def __str__(self):
        return self.NomTido

# Clase para el estado cívil
class EstadoCivil(models.Model):
    NomEsCi = models.CharField(max_length = 50, verbose_name = "Estado Cívil")

    class Meta:
        verbose_name = "Estado Cívil"
        verbose_name_plural = "Estados Civiles"

    def __str__(self):
        return self.NomEsCi

# Clase para el estado clasificación de los estudios
class TipoEstu(models.Model):
    NomTiEs = models.CharField(max_length = 50, verbose_name = "Tipo de Estudiante")

    class Meta:
        verbose_name = "Tipo de Estudiante"
        verbose_name_plural = "Tipo de Estudiantes"

    def __str__(self):
        return self.NomTiEs

# Clase para el estado tipos de logros
class TipoLogr(models.Model):
    NomTilo = models.CharField(max_length = 50, verbose_name = "Tipo de Logro")

    class Meta:
        verbose_name = "Tipo de Logro"
        verbose_name_plural = "Tipo de Logros"

    def __str__(self):
        return self.NomTilo