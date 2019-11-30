import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import time

load_dotenv()

if __name__ == "__main__":
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(
        os.getenv("SENDER"),
        os.getenv("PASSWORD")
    )

    msg_part1 = MIMEText(os.getenv("SUBJECT"), 'plain')
    with open("email.html", 'r') as html_file:
        msg_part2 = MIMEText(html_file.read(), 'html')

    receivers = os.getenv("RECEIVER").split(',')
    for receiver in receivers:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = os.getenv("SUBJECT")
        msg['From'] = os.getenv("SENDER_NAME")
        msg['To'] = receiver
        msg.attach(msg_part1)
        msg.attach(msg_part2)

        server.sendmail(
            os.getenv("SENDER"),
            receiver,
            msg.as_string()
        )
        print(f"Email sent to {receiver} successfully")

    server.quit()
    print(f"\n{len(receivers)} emails sent successfully")
