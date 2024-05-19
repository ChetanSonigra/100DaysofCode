import smtplib,os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.my_email = os.environ.get('MY_EMAIL')
        self.my_password = os.environ.get("MY_EMAIL_PASSWD")

    def send_mail(self,recepient_mail,cheapest_flight,city):
        if recepient_mail is None:
            recepient_mail = self.my_email
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=recepient_mail,password=self.password)
            connection.sendmail(from_addr=recepient_mail,
                                to_addrs=recepient_mail,
                                msg=f'''Subject: Found Cheap Flight to {city['city']}!\n\n
                                You have good deal at {cheapest_flight['price']} on {cheapest_flight['day']} 
                                which is less than your price. {city['lowestPrice']}'''
                                )