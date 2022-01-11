import binascii
import os
import sys
import uuid
from io import BytesIO

from PIL import Image
from django.contrib.auth.hashers import make_password
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _


# Create your models here.

def send_customer_email(users, client_id, browser, domain, password):
    try:
        data = {
            'client_id': client_id,
            'browser': browser,
            'domain': domain,
            'users': users,
            'password': password
        }
        html_body = render_to_string('adminhtml/email/customer_registration.html', data)
        subject = 'Welcome in our family.'
        to = [users.email]
        mail = EmailMultiAlternatives(subject=subject, to=to)
        mail.attach_alternative(html_body, 'text/html')
        mail.send()
        return True
    except Exception as e:
        return False


class Customers(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    mobile = models.CharField(max_length=10, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128)
    profile_pic = models.ImageField(upload_to='users/profile/')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    # required fields
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['name', 'mobile']

    def __str__(self):
        return self.name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def save(self, **kwargs):
        # opening Image
        im = Image.open(self.profile_pic)
        output = BytesIO()
        # resize the modify
        im = im.resize((100, 100))
        # after modification save it to the output
        im.save(output, format='JPEG', quality=90)
        output.seek(0)
        # change imagefield value to the newly modified image value
        self.profile_pic = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % uuid.uuid4(), 'image/jpeg',
                                                sys.getsizeof(output), None)
        super(Customers, self).save()

    @receiver(post_save)
    def save_token(sender, instance=None, created=False, **kwargs):
        if created:
            try:
                CustomerToken.objects.create(customer=instance)
            except Exception as e:
                pass

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'


class CustomerToken(models.Model):
    key = models.CharField(_('Key'), max_length=40, primary_key=True)
    customer = models.OneToOneField(Customers, on_delete=models.CASCADE, related_name='customer_token',
                                    verbose_name=_('Customer'))
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    class Meta:
        verbose_name = _('Customer Token')
        verbose_name_plural = _('Customer Tokens')

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_token()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_token(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
