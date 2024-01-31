// popup.js

// Function to send message to content script to detect spam
function detectSpam() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {action: "detectSpam"});
    });
}

// Attach event listener to the detectButton
document.addEventListener('DOMContentLoaded', function() {
    var detectButton = document.getElementById('detectButton');
    detectButton.addEventListener('click', detectSpam);
});

