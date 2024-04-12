from django.db import models

class Contact(models.Model):
  STATUS= (
    ('Lido', 'Lido'),
    ('Não Lido', 'Não Lido'),
  )
  name = models.CharField(max_length=255, blank=False)
  email = models.CharField(max_length=255, blank=False)
  subject = models.CharField(max_length=255, blank=False)
  message = models.TextField(blank=False)
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=10, choices=STATUS, default='Não Lido')

  def __str__(self):
    return self.name