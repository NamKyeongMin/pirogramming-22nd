from django.db import models
from apps.users.models import User

class Post(models.Model):
  title = models.CharField('제목', max_length= 20)
  content = models.CharField('내용', max_length=20)
  region = models.CharField('지역', max_length=20)
  user = models.ForeignKey(User, verbose_name='작성자', on_delete=models.CASCADE) 
  price = models.IntegerField('가격', default=1000)
  created_date = models.DateTimeField('작성일', blank=True, auto_created=True, auto_now_add=True)
  updated_date = models.DateTimeField('수정일', blank=True, auto_created=True, auto_now=True)
  photo = models.ImageField('사진', upload_to='posts/%y%m%d', blank=True)

  def __str__(self):
    return self.user.name