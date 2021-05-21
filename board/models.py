from django.db import models

# Create your models here.

class Thread(models.Model):

    title = models.CharField('タイトル', max_length=40)
    description = models.CharField('説明', max_length=100)
    created = models.DateTimeField('作成日時', auto_now_add=True)
    updated = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):

    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments', verbose_name='スレッド')
    name = models.CharField('投稿者名', default='名無し',max_length=20)
    body = models.TextField('投稿内容', max_length=200)
    created = models.DateTimeField('作成日時', auto_now_add=True)
    updated = models.DateTimeField('更新日時',auto_now=True)

    def __str__(self):
        return self.body