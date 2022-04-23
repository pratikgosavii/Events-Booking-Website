from django.db import models

# Create your models here.





from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File

# Create your models here.
import random
class QrCode(models.Model):
   url=models.URLField()
   image=models.ImageField(upload_to='qrcode',blank=True)

   def save(self,*args,**kwargs):
        print(self.url)
        qrcode_img=qrcode.make(self.url)
        canvas=Image.new("RGB", (600,600),"white")
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        buffer=BytesIO()
        canvas.save(buffer,"PNG")
        self.image.save(f'image{random.randint(0,9999)}'+ '.png',File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)