class Note(models.Model):
    name = models.CharField(max_length=200)
    family = models.TextField()
    datetime_creation = models.DateTimeField(auto_now_add=True)
