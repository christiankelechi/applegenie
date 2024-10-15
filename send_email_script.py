# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
import os
# def send_email(to_email, subject, body):
#     # SMTP server configuration
#     smtp_server = "c76592.sgvps.net"
#     smtp_port = 465
#     username = "support@finderskeepers.ai"
#     password = "}ur^81*1kll%"  # Replace with your actual email password

#     # Create the email content
#     msg = MIMEMultipart()
#     msg['From'] = username
#     msg['To'] = to_email
#     msg['Subject'] = subject

#     # Attach the body to the email
#     msg.attach(MIMEText(body, 'html'))  # Use 'plain' for plain text

#     try:
#         # Set up the SMTP server and send the email
#         with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
#             server.login(username, password)
#             server.sendmail(username, to_email, msg.as_string())
#             print("Email sent successfully!")
#     except Exception as e:
#         print(f"Failed to send email: {str(e)}")

# # Example usage
# recipient_email = "kezechristian@gmail.com"  # Replace with the recipient's email address
# email_subject = "Your Verification Code"
# email_body = "<strong>Your verification code is: 123456</strong>"  # Replace with your actual content

# send_email(recipient_email, email_subject, email_body)
import smtplib
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os

def send_email(to_email, subject, template_path, images_dir=None):
    # SMTP server configuration
    smtp_server = "c76592.sgvps.net"
    smtp_port = 465
    username = "support@finderskeepers.ai"
    password = "your_password"  # Replace with your actual email password

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Read the HTML template
    with open(template_path, 'r') as file:
        body = file.read()

    # Attach the body to the email
    msg.attach(MIMEText(body, 'html'))

    # Attach images if the directory is provided
    if images_dir:
        # Get all image files from the specified directory
        for filename in os.listdir(images_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):  # Add more formats if needed
                image_path = os.path.join(images_dir, filename)
                with open(image_path, 'rb') as img_file:
                    img = MIMEImage(img_file.read())
                    img.add_header('Content-ID', f'<{filename}>')  # Use the filename as the Content-ID
                    msg.attach(img)

    try:
        # Set up the SMTP server and send the email
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(username, password)
            server.sendmail(username, to_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Example usage
recipient_email = "kezechristian@gmail.com"  # Replace with the recipient's email address
email_subject = "Welcome to Finders Keepers"
current_directory = Path.cwd()

# Create the path to the template file
template_path = current_directory / "templates" / "email_templates" / "welcome" / "new_email.html"
images_dir = current_directory / "templates" / "email_templates" / "welcome"  # Replace with the path to your images directory

send_email(recipient_email, email_subject, template_path, images_dir)
