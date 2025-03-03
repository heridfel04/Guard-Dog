import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    sender_email = "kaligotla.prasanna44@gmail.com"
    receiver_email = "kingslays14@gmail.com"  # SMS via email (e.g., AT&T: number@txt.att.net)
    password = "jfkv bnbk zdgk heet"  # Create this in Gmail settings (see notes below)

    # Create a MIMEText object with UTF-8 encoding
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['Subject'] = "Guard Dog Alert 🚨"  # Add a subject line
    msg['From'] = sender_email
    msg['To'] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    
    # Send the message as a string
    server.sendmail(sender_email, receiver_email, msg.as_string())
    
    server.quit()
    print("Alert sent!")