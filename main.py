import smtplib
import datetime as dt
import pandas as pd
import random
# Rad Dataframe and Birthday Data
birthday_details = pd.read_csv("birthday.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (
    index, data_row) in birthday_details.iterrows()}

# Choose a Random Quote
with open("quotes.txt") as quotes:
    quote_list = quotes.readlines()
    quote = random.choice(quote_list)

# Set Up Email Connection
my_email = "saransh.shankar@gmail.com"
password = "ppnhfilfnhvkqfom"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)

# Date Time Module
now = dt.datetime.now()
today_tuple = (now.month, now.day)
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    person_name = birthday_person["name"]
    print(birthday_person)
    connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                        msg=f"Subject:Happy Birthday!!!\n\n{quote}\nHappy Birthday {person_name}\nLove you so much!")
    connection.close()

