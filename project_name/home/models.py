from django.db import models
from django.contrib.auth.models import User

class PageVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    page = models.CharField(max_length=200)
    visit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} visited {self.page} at {self.visit_time}"
