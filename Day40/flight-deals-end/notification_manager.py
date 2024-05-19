import smtplib,os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.my_email = os.environ.get('MY_EMAIL')
        self.my_password = os.environ.get("MY_EMAIL_PASSWD")

    def send_mail(self,sender_mail,recipient_mails,cheapest_flight,city):
        if sender_mail is None:
            sender_mail = self.my_email
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=sender_mail,password=self.my_password)
            connection.sendmail(from_addr=sender_mail,
                                to_addrs=[user for user in recipient_mails],
                                msg=f'''Subject: Found Cheap Flight to {city['city']}!\n\n
                                You have good deal at {cheapest_flight['price']} on {cheapest_flight['day']} 
                                which is less than your price. {city['lowestPrice']}'''
                                )