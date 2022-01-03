from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)

    # EMAIL PARA INICIAR SESION EN ADMIN
    # (PARA CREAR UN SUPERUSER ESTO TIENE QUE ESTAR COMENTADO)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []