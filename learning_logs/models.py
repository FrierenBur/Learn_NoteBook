from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# one model is one class in here
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    #* 外键：on_delete=models.CASCADE 表示如果引用的 Topic 被删除，那么关联的 Entry 也会被删除。
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """返回一个表示条目的简单字符串"""
        if len(self.text)< 50 :
            return self.text
        else:
            return f"{self.text[:50]}..."
