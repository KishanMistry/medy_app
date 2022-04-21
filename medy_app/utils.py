from django.conf import settings
from django.http import HttpResponse
from django.conf import settings
from django.utils.html import strip_tags
from django.core import mail


def sendEmail(html_message, subject, to):
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER    
    if mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message):
        return True
    else:
        return False