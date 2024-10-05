#Sending Alert to the Government

import smtplib
from email.mime.text import MIMEText

def send_alert():
    sender_email = "  our_email@example.com"
    receiver_email = "government_email@example.com"
    subject = "Air Quality Alert: Immediate Action Required"
    body = "The air quality in our area has reached hazardous levels. Immediate action is required."
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login("  our_email@example.com", "  our_password")
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Alert email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
if prediction == 1:
    send_alert()
