import pandas as pd
import datetime as dt
import random
import smtplib
import sensitive_data

sender_email = sensitive_data.sender_mail
password = sensitive_data.password


birthday_data = pd.read_csv("birthdays.csv")
birthdays_months = [month for month in birthday_data.month]
birthdays_days = [day for day in birthday_data.day]

birthdays_list = []
for _ in range(len(birthdays_months)):
    birthday_tuple = (birthdays_months[_], birthdays_days[_])
    birthdays_list.append(birthday_tuple)

today_day = dt.datetime.today().day
today_month = dt.datetime.today().month
today_tuple = (today_month, today_day)

if today_tuple in birthdays_list:
    tuple_index = birthdays_list.index(today_tuple)
    name = birthday_data.loc[tuple_index]["name"]
    email = birthday_data.loc[tuple_index]["email"]
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter:
        birthday_letter = letter.read()
        named_letter = birthday_letter.replace("[NAME]", name)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday, {name}\n\n{named_letter}"
        )
else:
    print("Nobody celebrates birthday today!")



