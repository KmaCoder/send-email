import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    msg = MIMEMultipart('alternative')
    msg['Subject'] = os.getenv("SUBJECT")
    msg['From'] = os.getenv("SENDER")
    msg['To'] = os.getenv("RECEIVER")

    part1 = MIMEText(msg['Subject'], 'plain')
    with open("email.html", 'r') as html_file:
        part2 = MIMEText(html_file.read(), 'html')

    msg.attach(part1)
    msg.attach(part2)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(
        os.getenv("SENDER"),
        os.getenv("PASSWORD")
    )
    server.sendmail(
        os.getenv("SENDER"),
        os.getenv("RECEIVER").split(','),
        msg.as_string()
    )
    server.quit()
    print(f"Email sent to {os.getenv('RECEIVER')} successfully")
