from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import Signal, receiver
from django_rest_passwordreset.signals import reset_password_token_created
from .models import ConfirmEmailToken, User


new_user_registered = Signal()

new_order = Signal()


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, **kwargs):
 

    message = EmailMultiAlternatives(
 
        f"Password Reset Token for {reset_password_token.user}",
   
        reset_password_token.key,
 
        settings.EMAIL_HOST_USER,
  
        [reset_password_token.user.email]
    )
    message.send()


@receiver(new_user_registered)
def new_user_registered_signal(user_id, **kwargs):
  
    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user_id)

    message = EmailMultiAlternatives(

        f"Password Reset Token for {token.user.email}",

        token.key,

        settings.EMAIL_HOST_USER,

        [token.user.email]
    )
    message.send()


@receiver(new_order)
def new_order_signal(user_id, **kwargs):

    user = User.objects.get(id=user_id)

    message = EmailMultiAlternatives(

        f"Обновление статуса заказа",
 
        'Заказ сформирован',
 
        settings.EMAIL_HOST_USER,

        [user.email]
    )
    message.send()