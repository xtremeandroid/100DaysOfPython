import requests
from bs4 import BeautifulSoup
import smtplib

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


URL = "https://www.amazon.in/Samsung-inch-60-1-Computer-Monitor/dp/B08GC8P3YZ"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Accept-Language": "en-US,en;q=0.5"
}
response = requests.get(URL, headers=headers)
content = response.text

soup = BeautifulSoup(content, "html.parser")
price = soup.find("span", class_="a-price-whole").get_text().split(".")[0]
price = int(price.replace(",", ""))

if price < 9000:
    send_mail("Low Price Alert!", f"Price for Your Monitor is lower than Rs.9,000 Now, Go Buy It Now !! Link : {URL}", "abc@gmail.com")
    print("Sent Email")
