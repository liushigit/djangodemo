from django.db import models

# Create your models here.

class Institution(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.name)

class Lecture(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField('Lecture time')
    place = models.CharField(max_length=200)
    institution = models.ForeignKey(Institution)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('lecture-detail', args=[str(self.id)])
