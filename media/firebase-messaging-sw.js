importScripts('https://www.gstatic.com/firebasejs/9.6.10/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.6.10/firebase-messaging-compat.js');

firebase.initializeApp({
    apiKey: "AIzaSyBqaqW0SMq8SPHCWX9QKpShGValpYyV2bs",
    authDomain: "namasterapidtax-a92e7.firebaseapp.com",
    projectId: "namasterapidtax-a92e7",
    storageBucket: "namasterapidtax-a92e7.appspot.com",
    messagingSenderId: "1072169977465",
    appId: "1:1072169977465:web:7b63186ed7f120943b76a8",
    measurementId: "G-VTWK2QSFXM"
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage((payload) => {
    console.log('Received background message ', payload);
    const notificationTitle = payload.notification.title;
    const notificationOptions = {
        body: payload.notification.body,
        icon: payload.notification.icon
    };

    self.registration.showNotification(notificationTitle, notificationOptions);
});