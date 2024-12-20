# Email Related
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def user_activation_email(user_email, subject, message, success_url, domain):
    sender = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    context = {
        "message": message,
        "username": "test",
        # Need to fetch the domain from ENV : FrontEnd Link
        "domain": domain,
        "success_url": success_url,
    }
    html_message = render_to_string("account_activation_email.html", context)
    plain_message = strip_tags(html_message)
    email = EmailMultiAlternatives(subject, plain_message, sender, recipient_list)
    email.attach_alternative(html_message, "text/html")
    email.send()


def success_email(
    request,
    subject,
    message,
    success_url="/",
    # Need to UPDATE
    domain="",
):
    sender = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email]
    context = {
        "username": request.user.username,
        "message": message,
        "success_url": success_url,
        "domain": domain,
    }
    html_message = render_to_string("email_template.html", context)
    plain_message = strip_tags(html_message)
    email = EmailMultiAlternatives(subject, plain_message, sender, recipient_list)
    email.attach_alternative(html_message, "text/html")
    email.send()


def failure_email(
    request,
    subject,
    message,
    success_url="/",
    # Need to UPDATE
    domain="",
):
    sender = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email]
    context = {
        "username": request.user.username,
        "message": message,
        "success_url": success_url,
        "domain": domain,
    }
    html_message = render_to_string("email_template.html", context)
    plain_message = strip_tags(html_message)
    email = EmailMultiAlternatives(subject, plain_message, sender, recipient_list)
    email.attach_alternative(html_message, "text/html")
    email.send()
