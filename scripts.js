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


// live clock
const clock24 = document.getElementById('clock24')

// Concatenate a zero to the left of every single digit time frame
function concatZero(timeFrame) {
  return timeFrame < 10 ? '0'.concat(timeFrame) : timeFrame
}

function realTime() {
  let date = new Date()
  let sec = date.getSeconds()
  let mon = date.getMinutes()
  let hr = date.getHours()
  clock24.textContent = `${concatZero(hr)} : ${concatZero(mon)} : ${concatZero(sec)}`
}

setInterval(realTime, 1000)