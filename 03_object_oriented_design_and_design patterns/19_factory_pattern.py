class EmailNotification:
    def send(self):
        print("Sending Email Notification")


class SMSNotification:
    def send(self):
        print("Sending SMS Notification")


class PushNotification:
    def send(self):
        print("Sending Push Notification")


class NotificationFactory:

    @staticmethod
    def create_notification(notification_type):

        if notification_type == "email":
            return EmailNotification()

        elif notification_type == "sms":
            return SMSNotification()

        elif notification_type == "push":
            return PushNotification()

        else:
            raise ValueError("Invalid notification type")


notification1 = NotificationFactory.create_notification("email")
notification1.send()

notification2 = NotificationFactory.create_notification("sms")
notification2.send()

notification3 = NotificationFactory.create_notification("push")
notification3.send()