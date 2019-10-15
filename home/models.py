from django.db import models


class Tag(models.Model):
    COLORS = [
        (0, 'primary'),
        (1, 'secondary'),
        (2, 'success'),
        (3, 'danger'),
        (4, 'warning'),
        (5, 'info'),
        (6, 'light'),
        (7, 'dark')
    ]
    title = models.CharField(max_length=20)
    badge = models.CharField(max_length=20, choices=COLORS)
    
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
    tags = models.ManyToManyField(Tag)
    timestamp = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    repository_url = models.CharField(max_length=200)
    site_url = models.CharField(max_length=200)
    rating = models.IntegerField(default=0, choices=RATES)

    def __str__(self):
        return self.title