from django.db import models

class Topic(models.Model):
    """The topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the model as text."""
        return self.text

class Entry(models.Model):
    """Information about progress in science"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns the model as text."""
        if self.text > self.text[:50]:
            return self.text[:50] + "..."
        elif self.text <= self.text[:50]:
            return self.text[:50]