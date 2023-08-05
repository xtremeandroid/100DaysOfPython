import smtplib
import datetime as dt
from random import choice, randint
import pandas as pd

my_email = ""
my_password = ""


def send_mail(subject, message, reciever_mail):
    global my_email, my_password
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=reciever_mail,
                            msg=f"Subject:{subject}\n\n{message}")
        connection.close()


def check_for_birthdays():
    today = dt.datetime.now()
    data = pd.read_csv("birthdays.csv")
    data_dict = data.to_dict(orient="records")
    for key in data_dict:
        if key["day"] == today.day and key["month"] == today.month:
            return [key["name"], key["email"]]
    return


if check_for_birthdays():
    user_data = check_for_birthdays()
    with open(f"letter_templates/letter_{randint(1,3)}.txt", 'r') as data_file:
        content = data_file.read()
        personalized_letter = content.replace("[NAME]", user_data[0])
        send_mail(f"Happy Birthday {user_data[0]}", personalized_letter, user_data[1])



