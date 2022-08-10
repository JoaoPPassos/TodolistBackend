from datetime import timedelta,datetime
from django.db import models
from django.contrib.auth.tokens import default_token_generator

# Create your models here.
import jwt
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class User(models.Model):
  username = models.CharField(max_length=40,null=False,blank=False)
  email = models.EmailField(max_length=100,null=False,blank=False,unique=True)
  password = models.CharField(max_length=100,null=False,blank=False)
  birthday = models.DateField()
  is_active = models.BooleanField(default=False)
  
  @property
  def token(self):
    token = jwt.encode({'username':self.username,'password': self.password,'exp': datetime.utcnow() + timedelta(hours=24)},settings.SECRET_KEY,algorithm='HS256')

    return token
  
  def is_authenticated():
    return True
  
  def send_user_activate(self):
    
    activate_link_url = "localhost:8000"

    confirmation_token = default_token_generator.make_token(self)
    
    activation_link = f'{activate_link_url}?user_id={self.id}&confirmation_token={confirmation_token}'
    assert isinstance(self.email,list)
    
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login('joaoffxii@gmail.com','3.14159265j')
    server.sendmail('joaoffxii@gmail.com',self.email, 'mensagem')
    server.quit()
    #return activation_link