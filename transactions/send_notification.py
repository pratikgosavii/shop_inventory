# send_notifications.py

from pywebpush import webpush, WebPushException

subscriptions = [...]  # Retrieve subscriptions from your database

for subscription in subscriptions:
    try:
        webpush(
            subscription_info=subscription,
            data="Your notification message",
            vapid_private_key="your_private_key",
            vapid_claims={"sub": "mailto:your@email.com"}

            
        )
    except WebPushException as ex:
        print("Push notification failed for subscription:", subscription)
        print(ex)
