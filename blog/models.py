from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):   # models의 Model을 상속받은 class Post
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # on_delete=models.CASCADE의 의미는 사용자가 사라지면 사용자를 참조하는 것들도 다 지워짐
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title