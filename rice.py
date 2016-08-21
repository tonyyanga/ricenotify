import smtplib
from email.mime.text import MIMEText
import datetime

server = smtplib.SMTP('smtp.zoho.com', 587)
server.starttls()
server.login('riceinlondon@ycyang.me', 'STABLEriceinLondon')

header1 = """Hello, Henry,

Please cook some rice for me today. I intend to get rice from you for """

header2 = """Hello, Tony,

As a reminder, please decide on your rice demand for today and notify Henry or Colin by text."""

disclaimer = """

I understand that you may have other plan for tonight or prefer to prepare rice later. It is always at your discretion whether to honor my request or not. Should you not be able to fulfill my request, please reply this email in advance so that I can be prepared, if it is convenient for you.

Thank you!"""

end = """

Have a nice day!

Best regards,

Sincerely,
Tony Yang"""

body = None

if datetime.datetime.today().weekday() >= 4:
    body = header2 + end
elif datetime.datetime.today().weekday() == 0:
    body = header1 + "DINNER TONIGHT and LUNCH TOMORROW. I will go upstairs to your flat to pick up my rice at 6:30 PM today." + disclaimer + end
elif datetime.datetime.today().weekday() == 1:
    body = header1 + "DINNER TONIGHT ONLY. I will go upstairs to your flat to pick up my rice at 6:00 PM today." + disclaimer + end
elif datetime.datetime.today().weekday() == 2:
    body = header1 + "DINNER TONIGHT ONLY. I will go upstairs to your flat to pick up my rice at 7:00 PM today." + disclaimer + end
elif datetime.datetime.today().weekday() == 3:
    body = header1 + "DINNER TONIGHT and lunch / dinner tomorrow. I will go upstairs to your flat to pick up my rice at 6:30 PM today." + disclaimer + end

msg = MIMEText(body)
msg['Subject'] = 'Automated Rice Notification on ' + datetime.date.today().strftime("%B %d, %Y")
msg['From'] = "Automated Rice Notification <riceinlondon@ycyang.me>"

if datetime.datetime.today().weekday() <= 3:
    msg['To'] = "Henry Skrehot <henryskrehot@berkeley.edu>"
    msg['Cc'] = "Colin Xiang <colinxiang518@gmail.com>, Tony Yang <tony@ycyang.me>"
    server.sendmail("riceinlondon@ycyang.me", {"henryskrehot@berkeley.edu", "colinxiang518@gmail.com", "tony@ycyang.me"}, msg.as_string())
else:
    msg['To'] = "Tony Yang <tony@ycyang.me>, Tony Yang <tonyyanga@gmail.com>"
    server.sendmail("riceinlondon@ycyang.me", "tony@ycyang.me", msg.as_string())

server.quit()
