# sender's mail --> gmail server --> yahoo server --> received's mail

# smtp information:  Simple Mail Transfer Protocol
# Host: 
# gmail - smtp.gmail.com
# hotmail - smtp.live.com
# yahoo - smtp.mail.yahoo.com

import smtplib

my_email = 'myemail@gmail.com'
password = 'abc@1234'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs='testing@yahoo.com',
                        msg='Subject:Hello\n\nThis is body of my email.')
    # connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
print(now,year,now.month,now.day,now.hour,now.minute,now.second,now.weekday())
print(type(now),type(year))
date_of_birth = dt.datetime(year=1998,month=1,day=4)
print(date_of_birth)


# Send Monday motivational quotes
import random,smtplib
import datetime as dt

with open('100DaysofCode/Day32/quotes.txt',encoding='utf-8') as f:
    list_of_quotes = f.readlines()

quote = random.choice(list_of_quotes)
print(quote)
my_email = 'myemail@gmail.com'
password = 'abc@1234'
now = dt.datetime.now()
if now.weekday()==0:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='testing@yahoo.com',
                            msg=f'Subject:Happy Monday\n\n{quote}')


