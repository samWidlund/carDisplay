console.log("script.js är laddad!");

function checkOnlineStatus() {
    if (navigator.onLine) {
        console.log("Användaren är online");
    } else {
        console.log("Användaren är offline");
    }
}

// check when the user is online or offline
window.addEventListener('online', function() {
    console.log("Anslutning återställd");
    checkOnlineStatus();
});
window.addEventListener('offline', function() {
    console.log("Anslutning förlorad");
    checkOnlineStatus();
});

// check when the page is loaded
document.addEventListener('DOMContentLoaded', function() {
    checkOnlineStatus();
});