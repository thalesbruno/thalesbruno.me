from django.db import models


class Technology(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Technologies'
    
    def __str__(self):
        return self.title


class Work(models.Model):
    RATES = (
        (0, 'Ok'),
        (1, 'Good'),
        (2, 'Nice'),
        (3, 'Awesome'),
        (4, 'Spetacular')
    )
    title = models.CharField(max_length=100, blank=False, null=False)
    thumbnail = models.ImageField()
    overview = models.TextField()
    technologies = models.ManyToManyField(Technology)
    timestamp = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    repository_url = models.CharField(max_length=200)
    site_url = models.CharField(max_length=200)
    rating = models.IntegerField(default=0, choices=RATES)

    def __str__(self):
        return self.title