import smtplib
import ssl
import uuid
from email.mime.text import MIMEText

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    # is_verified = models.BooleanField(default=False)


# class EmailVerification(models.Model):
#     code = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     expiration = models.DateTimeField()
#
#     def __str__(self):
#         return f'Email Verification for {self.user.email}'
#
#     def send_verification_email(self):
#         link = reverse('users:email_verification', kwargs={'email': self.user.email, 'code': self.code})
#         verification_link = f'{settings.DOMAIN_NAME}{link}'
#         subject = f'Verification email for {self.user.username}'
#         message = 'To verify email for {}, visit {}'.format(
#             self.user.username,
#             verification_link
#         )
#         send_mail(
#             subject=subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[self.user.email],
#             fail_silently=False,
#         )
#
#     def is_expired(self):
#         return True if now() >= self.expiration else False

