from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100, null=False, blank=False)  # Marca do carro
    model = models.CharField(max_length=100, null=False, blank=False)  # Modelo do carro
    year = models.PositiveIntegerField(null=False, blank=False)  # Ano de fabricação
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)  # Preço do carro
    image = models.ImageField(upload_to='cars/', null=True, blank=True)  # Imagem do carro
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  # Relacionamento com o usuário

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
