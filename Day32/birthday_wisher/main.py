##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)


import random,smtplib,pandas as pd
import datetime as dt

letters = ['letter_1','letter_2','letter_3']

data_df = pd.read_csv('Day32/birthday_wisher/birthdays.csv')
data_dict = data_df.to_dict(orient='records')

now = dt.datetime.now()
mon,day = now.month,now.day

my_email = 'myemail@gmail.com'
password = 'abc@123'


for x in data_dict:
    sample = random.choice(letters)

    if (x['day'],x['month']) == (day,mon):
        with open(f'Day32/birthday_wisher/letter_templates/{sample}.txt') as f:
            data = f.read()
            letter = data.replace('[NAME]',x['name'])
    
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.send_message(from_addr=my_email,to_addrs=x['email'],msg=f'Subject: Birthday Wishes!\n\n{letter}')



