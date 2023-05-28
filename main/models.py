from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length = 30, null = False, blank = False)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    # writer field를 foreignKey로 수정!!
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    # blog 모델에 tags 필드 추가
    tags = models.ManyToManyField(Tag, related_name = "blogs", blank = True)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]
    
class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title+" : "+self.content[:20]
