import smtplib
import datetime as dt
import random

my_email = "anmol.pythontest@gmail.com"
my_password = "vyitymcetjrepnqz"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="anmol.pythontest@yahoo.com",
                            msg=f"Subject: motivation \n\n{quote}")
