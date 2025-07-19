// js/firebase-config.js
if (typeof firebase === 'undefined') {
  console.error('Firebase SDK no cargado.');
  throw new Error('Firebase SDK no cargado.');
}

const firebaseConfig = {
apiKey: "AIzaSyCO9FUQRFHnv-BZV8ZbUWyIbZbuuZO8g5Y",
  authDomain: "chat-av-a3131.firebaseapp.com",
  projectId: "chat-av-a3131",
  storageBucket: "chat-av-a3131.firebasestorage.app",
  messagingSenderId: "457752271473",
  appId: "1:457752271473:web:4fa8783bfccc01f29b99d0",
  measurementId: "G-DQ35SCENDJ"
};

firebase.initializeApp(firebaseConfig);
window.auth = firebase.auth();
window.db = firebase.firestore();
window.database = firebase.database();