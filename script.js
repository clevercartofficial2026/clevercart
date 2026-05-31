// 1. जब यूजर हमारी वेबसाइट पर "Search" या "Analyze" बटन दबाएगा, तब यह काम शुरू होगा
async function getTrustScoreFromServer(productName) {
    try {
        // 2. यह लाइन हमारे पायथन बैकएंड (analyzer.py) को प्रोडक्ट का नाम भेजेगी
        // अभी हम इसे लोकल सर्वर (localhost) के लिए सेट कर रहे हैं
        const response = await fetch(`http://127.0.0.1:5000/api/analyze?product=${encodeURIComponent(productName)}`);
        
        if (!response.ok) {
            throw new Error('सर्वर से कनेक्ट करने में कोई दिक्कत आई है!');
        }

        // 3. सर्वर से जो स्कोर आएगा, उसे यहाँ रिसीव करेंगे
        const data = await response.json();
        return data.trust_score;

    } catch (error) {
        console.error("ओह! एरर आया:", error);
        return "गड़बड़ हुई";
    }
}

// 4. यह हिस्सा स्क्रीन पर बटन दबाने वाले काम को संभालता है
// (मान लेते हैं कि आपके HTML में बटन की ID 'searchBtn' और इनपुट की ID 'productInput' है)
document.getElementById('searchBtn')?.addEventListener('click', async () => {
    const inputField = document.getElementById('productInput');
    const resultDiv = document.getElementById('scoreResult'); // जहाँ स्कोर दिखाना है
    
    if (inputField && resultDiv) {
        const productName = inputField.value.trim();
        if (productName === "") {
            alert("कृपया पहले किसी प्रोडक्ट का नाम तो लिखिए!");
            return;
        }

        resultDiv.innerText = "Gemini AI जांच कर रहा है, कृपया रुकें...";
        
        // स्कोर मंगवा रहे हैं
        const score = await getTrustScoreFromServer(productName);
        
        // स्क्रीन पर स्कोर दिखा रहे हैं
        resultDiv.innerText = `इस प्रोडक्ट का Trust Score है: ${score}/10`;
    }
});

