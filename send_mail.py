import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '6eb1d25d63cbc4'
    password = 'b8398409d97099'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_mail = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message,'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_mail
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server,port) as server:
        server.login(login, password)
        server.sendmail(sender_mail, receiver_email, msg.as_string())
