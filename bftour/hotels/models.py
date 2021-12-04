from django.db import models

# Create your models here.
class Hotel(models.Model):

    name = models.CharField(max_length=50)
    
class Post(models.Model):
    postname = models.CharField(max_length=50)
   
    contents = models.TextField()
    
    def __str__(self):
        return self.postname

# 상품 테이블
class tb_product(models.Model):
    
    #pro_seq = models.CharField(primary_key=True, max_length=200)
    #mem_seq = models.ForeignKey
    title = models.CharField(max_length=50)
    contents = models.TextField()
    place = models.TextField()
    adress = models.CharField(max_length=255)
    #type = 체크박스
    type = models.CharField(max_length=50, default='')
    start_dt = models.DateTimeField('date published')
    end_dt = models.DateTimeField('date published')
    pro_price = models.IntegerField(default=0)
    reg_dt = models.DateTimeField(auto_now_add=True)
    reg_id = models.CharField(max_length=50, default='admin')
    thumb_file = models.ImageField(null=True, upload_to="thumb/%Y/%m/%d")
    reserve_yn = models.CharField(max_length = 1, default='N')
    del_yn = models.CharField(max_length = 1, default='N')

    def __str__(self):
        return self.title
