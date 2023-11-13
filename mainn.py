import smtplib
import datetime as dt
import random

my_email = "xyz@gmail.com" #ur email
my_password = "xyz"        #ur app passowrd

now = dt.datetime.now()
weekday = now.weekday()
with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="xyz@yahoo.com",       # to_addrs= senders emails 
                            msg=f"Subject: motivation \n\n{quote}")
