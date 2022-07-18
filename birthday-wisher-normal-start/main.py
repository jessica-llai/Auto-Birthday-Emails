
import datetime as dt
import random
import pandas
import smtplib

my_username = "laiy20010413@gmail.com"
my_password = "aonpgiigsfjkhjqv"


today=(dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]  #find the right key
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        new_letter = content.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com", 25) as smtp:
        smtp.starttls()
        smtp.login(user=my_username, password=my_password)
        smtp.ehlo()

        smtp.ehlo()
        smtp.sendmail(from_addr=my_username,
                      to_addrs="laiy20010413@yahoo.com",
                      msg=f"Subject: Happy Birthday!\n\n{new_letter}")
        smtp.quit()

