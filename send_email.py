import smtplib



smtp=smtplib.SMTP("smtp.gmail.com",587)
smtp.starttls()
smtp.login("email_address","pasword")


smtp.sendmail("sender_email_address","receiver_email_address",f"Subject: \n\ntext")

smtp.quit()
