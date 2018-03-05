from django.db import models
from django.core.urlresolvers import reverse

class Course(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('course_detail', arg=(self.id, ))

    def __str__(self):
        return self.name

