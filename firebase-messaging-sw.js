// firebase-messaging-sw.js
importScripts('https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/10.7.1/firebase-messaging.js');

const firebaseConfig = {
    apiKey: "AIzaSyBqaqW0SMq8SPHCWX9QKpShGValpYyV2bs",
    authDomain: "namasterapidtax-a92e7.firebaseapp.com",
    projectId: "namasterapidtax-a92e7",
    storageBucket: "namasterapidtax-a92e7.appspot.com",
    messagingSenderId: "1072169977465",
    appId: "1:1072169977465:web:7b63186ed7f120943b76a8",
    measurementId: "G-VTWK2QSFXM"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Retrieve an instance of Firebase Messaging
const messaging = firebase.messaging();

// Handle background messages
messaging.onBackgroundMessage((payload) => {
    console.log('Received background message ', payload);
    const notificationTitle = payload.notification.title;
    const notificationOptions = {
        body: payload.notification.body,
        icon: payload.notification.icon
    };

    self.registration.showNotification(notificationTitle, notificationOptions);
});