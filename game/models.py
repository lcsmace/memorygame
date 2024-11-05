from django.db import models

class Game(models.Model):
    player_name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=200, null=True)
    evolution_chain = models.TextField()  # Armazena a cadeia de evolução como JSON ou texto serializado

    def __str__(self):
        return self.name