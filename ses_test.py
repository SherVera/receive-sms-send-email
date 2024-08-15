import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def lambda_handler(event, context):
    for record in event['Records']:
        sns_message = record['Sns']['Message']
        print("Message: " + sns_message)

        # Configuration of SMTP server
        smtp_server = os.environ['SMTP_SERVER']
        smtp_port = os.environ['SMTP_PORT']  # Default to 587 if not set
        smtp_user = os.environ['SMTP_USER']
        smtp_password = os.environ['SMTP_PASSWORD']

        # Configure the email
        sender_email = os.environ['SENDER_EMAIL']
        recipient_email = os.environ['RECIPIENT_EMAIL']
        subject = 'CA Notification'
        body = sns_message

        # Create the message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Start TLS
            server.login(smtp_user, smtp_password)  # Authenticate
            server.sendmail(sender_email, recipient_email,
                            msg.as_string())  # Send email
            server.quit()  # Close the connection
            return {
                'statusCode': 200,
                'body': 'Email sent successfully.'
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': f'Error sending email: {str(e)}'
            }


if __name__ == '__main__':
    event = {
        'Records': [
            {
                'Sns': {
                    'Message': 'Hello from AWS SES'
                }
            }
        ]
    }
    context = {}
    lambda_handler(event, context)
