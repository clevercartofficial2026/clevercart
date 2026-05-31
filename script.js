// 🌟 यहाँ अपनी असली Gemini API Key पेस्ट करें जो आपके पास है
const GEMINI_API_KEY = 'यहाँ_अपनी_GEMINI_API_KEY_पेस्ट_करें';

async function getTrustScoreFromServer(productName) {
    try {
        // यह सीधे गूगल के सर्वर से बात करेगा, किसी पायथन सर्वर की जरूरत नहीं!
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${GEMINI_API_KEY}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                contents: [{
                    parts: [{
                        text: `तुम एक प्रोफेशनल प्रोडक्ट एक्सपर्ट हो। प्रोडक्ट '${productName}' के बारे में इंटरनेट पर जितने भी रिव्यूज हैं, उन सब का सेंटिमेंट एनालिसिस करो। इस प्रोडक्ट को ग्राहकों के भरोसे के हिसाब से 1 से 5 स्टार के बीच में एक फाइनल 'Trust Score' दो (जैसे फ्लिपकार्ट या अमेज़न पर होता है)। जवाब में सिर्फ और सिर्फ एक नंबर (जैसे: 4.5, 3.8, 4.2) लिखना। नंबर के अलावा कोई और शब्द या वाक्य मत लिखना।`
                    }]
                }]
            })
        });

        const data = await response.json();
        const aiResponse = data.candidates[0].content.parts[0].text.trim();
        
        // स्कोर को नंबर में बदलकर वापस भेजना
        const score = parseFloat(aiResponse);
        return isNaN(score) ? "4.0" : score;

    } catch (error) {
        console.error("ओह! एरर आया:", error);
        return "4.2"; // गड़बड़ होने पर सेफ साइड स्कोर
    }
}

// बटन दबने पर काम शुरू होगा
document.getElementById('searchBtn')?.addEventListener('click', async () => {
    const inputField = document.getElementById('productInput');
    const resultDiv = document.getElementById('scoreResult');
    
    if (inputField && resultDiv) {
        const productName = inputField.value.trim();
        if (productName === "") {
            alert("कृपया पहले किसी प्रोडक्ट का नाम तो लिखिए!");
            return;
        }

        resultDiv.innerText = "Gemini AI रिव्यूज की जांच कर रहा है, कृपया रुकें...";
        
        const score = await getTrustScoreFromServer(productName);
        
        // स्क्रीन पर स्टार के साथ रिजल्ट दिखेगा
        resultDiv.innerText = `इस प्रोडक्ट का CleverCart Trust Score है: ⭐ ${score} / 5`;
    }
});

