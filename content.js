
// Function to detect spam content on the webpage
function detectSpamOnPage() {
    // List of spam words
    var spamWords = ['spam', 'unwanted', 'advertisement','100% more','100% free','additional income','be your own boss','best price'];  // Add more spam words as needed

    // Select text elements on the webpage (paragraphs, buttons, headers, divs)
    var textElements = document.querySelectorAll('p, button, h1, h2, h3, h4, h5, h6, div');

    // Check for spam words in text elements
    var foundSpam = false;
    textElements.forEach(function(element) {
        var elementText = element.textContent.toLowerCase();  // Convert text to lowercase for case-insensitive matching
        spamWords.forEach(function(spamWord) {
            if (elementText.includes(spamWord)) {
                foundSpam = true;
                return; // Exit inner loop if any spam word is found
            }
        });
        if (foundSpam) {
            return; // Exit outer loop if any spam word is found
        }
    });

    // Display alert if spam is detected or not detected
    if (foundSpam) {
        alert("Dark pattern detected on this website!");
    } else {
        alert("No Dark pattern detected on this website.");
    }
}

// Listen for messages from the popup
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "detectSpam") {
        detectSpamOnPage();
    }
});
