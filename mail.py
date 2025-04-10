# import required modules
import smtplib
import random
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
USERNAME = "<Mail id>"
PASSWORD = "<App Password>"

messages = [
    "Hello, this is test mail",
    "Random message alert: system load is stable"
    "Hope everything is fine"
]

random_message = random.choice(messages)

subject = "Random system notification"

body = f"""\
        Hello phani,
        Message: {random_message}
        Best Regards,
        Your monitoring Team
        """

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = USERNAME
msg["To"] = "phani@kodekloud.com"

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, ["phani@kodekloud.com"], msg.as_string())
    server.quit()
    print("Email sent successfully")
except Exception as e:
    print(f"error: {e}")
