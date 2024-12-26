from django.core.mail import send_mail, EmailMessage

def send_email_notification(to_email, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email='fadigell@gmail.com',
        recipient_list=[to_email],
        fail_silently=False,
    )

def send_html_email(to_email, html_content):
    email = EmailMessage(
        subject='Hello',
        body=html_content,
        from_email='fadigell@gmail.com',
        to=[to_email],
    )
    email.content_subtype = 'html'
    email.send()

