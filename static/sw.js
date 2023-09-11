self.addEventListener('push', function(event) {
    console.log('Push notification received:', event.data.text());

    // Handle the push notification here if needed
    // You can access the notification data in event.data
    // This example simply displays a notification with sound on the client side

    // Trigger the client to handle the push notification
    self.clients.matchAll().then(function(clients) {
        if (clients && clients.length) {
            clients[0].postMessage(event.data.text());
        }
    });

    const options = {
        body: event.data.text(),
        icon: 'icon.png', // Replace with the path to your app's icon
        badge: 'badge.png', // Replace with the path to your app's badge
        sound: 'notification.mp3' // Replace with the path to your notification sound
    };

    event.waitUntil(
        self.registration.showNotification('My App', options)
    );
});