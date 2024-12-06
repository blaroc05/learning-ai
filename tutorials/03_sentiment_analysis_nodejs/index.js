// Import the Natural library for sentiment analysis
const natural = require('natural');
const analyzer = new natural.SentimentAnalyzer('English', natural.PorterStemmer, 'afinn');

// Function to analyze the sentiment of a given text
function analyzeSentiment(text) {
    const words = text.split(" ");
    const sentimentScore = analyzer.getSentiment(words);

    if (sentimentScore > 0) {
        console.log(`The text has a positive tone (Sentiment Score: ${sentimentScore})`);
    } else if (sentimentScore < 0) {
        console.log(`The text has a negative tone (Sentiment Score: ${sentimentScore})`);
    } else {
        console.log(`The text has a neutral tone (Sentiment Score: ${sentimentScore})`);
    }
}

// Example text to analyze
const text = "I absolutely love this product! It works perfectly and I am very happy with it.";

// Perform sentiment analysis
analyzeSentiment(text);


const text1 = "This is the worst experience I’ve ever had.";
const text2 = "The weather is okay today, not too good, not too bad.";

analyzeSentiment(text1);  // Negative tone
analyzeSentiment(text2);  // Neutral tone
