from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    pass

    def es_colaborador(self):
        return self.groups.filter(name='colaborador').exists()