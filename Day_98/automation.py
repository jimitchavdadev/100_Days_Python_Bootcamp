import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "your_email_password"  # For Gmail, use App Password if 2FA is enabled

# Email content
subject = "Daily Reminder"
body = "This is your daily reminder! Don't forget to complete your tasks."

# Function to send email
def send_email():
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Add body to email
        msg.attach(MIMEText(body, 'plain'))

        # Connect to Gmail's SMTP server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Schedule the email to be sent daily at a specific time (e.g., 8:00 AM)
schedule.every().day.at("08:00").do(send_email)

# Keep the script running to check for the scheduled time
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for 1 minute before checking again
