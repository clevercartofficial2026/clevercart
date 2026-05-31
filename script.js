// 1. यह फंक्शन बैकएंड (पायथन) से जुड़कर प्रोडक्ट का 5-स्टार स्कोर लेकर आएगा
async function getTrustScoreFromServer(productName) {
    try {
        // यह लाइन हमारे सर्वर (main.py) को प्रोडक्ट का नाम भेजेगी
        const response = await fetch(`http://127.0.0.1:5000/api/analyze?product=${encodeURIComponent(productName)}`);
        
        if (!response.ok) {
            throw new Error('सर्वर से कनेक्ट करने में कोई दिक्कत आई है!');
        }

        // सर्वर से जो डेटा आएगा, उसे यहाँ रिसीव करेंगे
        const data = await response.json();
        return data.trust_score; // यहाँ से हमें 5 में से नंबर मिलेगा

    } catch (error) {
        console.error("ओह! एरर आया:", error);
        return "गड़बड़ हुई";
    }
}

// 2. यह हिस्सा स्क्रीन पर बटन दबने के बाद का काम संभालता है
document.getElementById('searchBtn')?.addEventListener('click', async () => {
    const inputField = document.getElementById('productInput');
    const resultDiv = document.getElementById('scoreResult'); // जहाँ हमें स्टार रेटिंग दिखानी है
    
    if (inputField && resultDiv) {
        const productName = inputField.value.trim();
        if (productName === "") {
            alert("कृपया पहले किसी प्रोडक्ट का नाम तो लिखिए!");
            return;
        }

        // यूजर को पता चले कि काम चल रहा है, इसलिए यह मैसेज दिखेगा
        resultDiv.innerText = "Gemini AI रिव्यूज की जांच कर रहा है, कृपया रुकें...";
        
        // अब हम ऊपर वाले फंक्शन को बोलकर स्कोर मंगवा रहे हैं
        const score = await getTrustScoreFromServer(productName);
        
        // यहाँ स्क्रीन पर ग्राहकों को 5-स्टार फॉर्मेट में स्कोर दिखेगा (जैसे ⭐ 4.5 / 5)
        resultDiv.innerText = `इस प्रोडक्ट का CleverCart Trust Score है: ⭐ ${score} / 5`;
    }
});
