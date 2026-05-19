from openai import OpenAI
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = """
Generate 5 problem solving problems.

For each problem include:
- Title
- Difficulty
- Problem
- Input/Output example
- Full C++ solution
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

content = response.choices[0].message.content

email = os.getenv("EMAIL")
password = os.getenv("EMAIL_PASSWORD")

msg = MIMEMultipart()
msg["From"] = email
msg["To"] = email
msg["Subject"] = "Daily Problem Solving"
msg.attach(MIMEText(content, "plain"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)
server.sendmail(email, email, msg.as_string())
server.quit()

print("DONE")