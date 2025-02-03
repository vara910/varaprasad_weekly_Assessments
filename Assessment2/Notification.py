# •	14. Implement method overriding for a `Notification` class where `send()` is overridden in `EmailNotification` and `SMSNotification`.
class Notification():
    def send(self):
        return "all the notifications are always sent to devices that are logged in "
class EmailNotification(Notification):
    def send(self):
        return "notification has been sent via email"
class SmsNotification(Notification):
    def send(self):
        return "notification is sent via SMS"   
cl=EmailNotification()
print(cl.send())
cde=SmsNotification()
print(cde.send())     