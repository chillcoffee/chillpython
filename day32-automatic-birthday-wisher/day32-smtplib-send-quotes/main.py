import smtplib
import datetime as dt
import random

MY_EMAIL = "chillcoffee.9419@gmail.com"
MY_PASSWORD = "uwrqcnkcrhccqqje"

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 3:
    print("Monday")
    with open("quotes.txt", encoding="utf8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)


    with open("emails.txt", encoding="utf8") as email_file:
        all_emails = email_file.readlines()
    raw_msg = f"Subject:Another Monday Motivation\n\n{quote}"

    print(raw_msg)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  #secure connection
        connection.login(MY_EMAIL, MY_PASSWORD)
        print(quote)
        for email in all_emails:
            email = email.strip("\n")

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=raw_msg.encode('utf8')
            )

