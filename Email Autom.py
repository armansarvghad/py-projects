import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create a MIME multipart message
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = recipient_email
    email_message['Subject'] = subject

    # Attach the message to the email
    email_message.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.example.com', 587) as smtp_server:
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)
        smtp_server.send_message(email_message)

# Example usage
sender_email = 'your_email@example.com'
sender_password = 'your_email_password'
recipient_email = 'recipient_email@example.com'
subject = 'Hello from Python!'
message = 'This is an automated email.'

send_email(sender_email, sender_password, recipient_email, subject, message)
