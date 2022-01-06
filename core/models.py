from django.db import models


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Todo(Base):
    name = models.CharField(max_length=120)
    done = models.BooleanField(default=False)
