# Python can be used to send various types of notifications, including:
# 1.Desktop Notifications – Using libraries like plyer, win10toast, notify2, notifypy to show native system alerts.

# 2.Email Notifications – Using Python’s built-in smtplib to send emails via SMTP.

# 3.SMS Notifications – Using third-party APIs (e.g., Twilio, Sinch) to send text messages.

# 4.Web Push Notifications – Integrated into web apps via push notification services and Python backends.

# 5.In-app Notifications – Frameworks like Shiny for Python allow showing notifications inside the app UI.

import time 
from plyer import notification 

while True:
    print("Please sip some water!")
    notification.notify(title="please drink some water",message = "You need to drink some water", )
    time.sleep(3)