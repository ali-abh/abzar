from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class User(models.Model):
    class meta: 
        verbosename="کاربر"
    name = models.CharField(max_length=50,verbose_name="نام  ")
    lastname = models.CharField(max_length=50,null=True,verbose_name="نام خانوادگی ")
    userphonenumber = models.CharField(max_length=15, validators=[RegexValidator(regex=r'\d{10,14}', message='Enter a valid phone number')],verbose_name="شماره تلفن  ")
    gmail = models.EmailField(unique=True,verbose_name=" ایمیل ")       #####
    password = models.CharField(max_length=50,verbose_name="رمز  ")
    address = models.TextField(max_length=100,verbose_name=" ادرس محل سکونت ")
    age = models.PositiveIntegerField(null=True, blank=True,verbose_name=" سن ")
    def __str__(self) :
        return "{} {}".format(self.name ,self.lastname)

class Abzar(models.Model):
    class meta:    
        verbosename="ابزار"
    productname = models.CharField(max_length=100,verbose_name="نام محصول")
    remained = models.CharField(max_length=3,null=True,blank=True,verbose_name="تعداد باقی مانده ")
    price = models.DecimalField(verbose_name=" قیمت",decimal_places=3,max_digits=7)
    aboutproduct = models.TextField(max_length=350,null=True,blank=True,verbose_name="درباره ابزار ")
    brandname = models.CharField(max_length=40,null=True,blank=True,verbose_name="نام برند ")
    manufacturing_country = models.CharField(max_length=20,verbose_name=" کشور سازنده ")
    image = models.ImageField()
    def __str__(self) :
        return self.productname

class Sell(models.Model):
    address = models.CharField(max_length=350,verbose_name=" آدرس دقیق ")
    housenumber = models.IntegerField(verbose_name=" پلاک  ")
    postalcode = models.IntegerField(verbose_name="  کدپستی ")
    paymentmethod = models.CharField(max_length=1000,verbose_name=" روش پرداخت")     
    receivername = models.CharField(max_length=25,verbose_name="نام نحویل گیرنده ")
    class Meta:
        verbose_name = "فروش"
