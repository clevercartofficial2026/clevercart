import os
# 1. सबसे पहले हम गूगल की लाइब्रेरी को बुला रहे हैं ताकि AI का इस्तेमाल कर सकें
import google.generativeai as genai

# 2. यहाँ आपको अपनी जादुई चाबी (Gemini API Key) डालनी है
# जो चाबी आपके पास है, उसे नीचे वाले सिंगल कोट ' ' के बीच में लिख दें
GEMINI_API_KEY = 'AIzaSyDQFZ09xJmzy_6q0YJnaqE4ncqaC7Xk11s'

# 3. यह लाइन गूगल को आपकी चाबी दिखाकर काम करने की परमिशन लेगी
genai.configure(api_key=GEMINI_API_KEY)

# 4. यह हमारा मुख्य फंक्शन है जो आपके 10 सोर्सेज (YouTube, Reddit आदि) का एनालिसिस करेगा
def get_trust_score(product_name):
    try:
        # हम गूगल के सबसे तेज और बढ़िया मॉडल 'gemini-1.5-flash' का इस्तेमाल कर रहे हैं
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # हम Gemini AI को बिल्कुल साफ निर्देश (Prompt) दे रहे हैं कि उसे क्या करना है
        prompt = f"""
        तुम एक प्रोफेशनल प्रोडक्ट एक्सपर्ट हो। प्रोडक्ट '{product_name}' के बारे में इंटरनेट पर जितने भी सोर्सेज हैं 
        (जैसे: YouTube रिव्यूज, Reddit चर्चाएं, Twitter कमेंट्स, MouthShut, Trustpilot और अलग-अलग ब्लॉग्स), 
        उन सब का अच्छे से सेंटिमेंट एनालिसिस (Sentiment Analysis) करो।
        
        इस प्रोडक्ट को ग्राहकों के भरोसे के हिसाब से 1 से 5 स्टार के बीच में एक फाइनल 'Trust Score' दो (जैसे फ्लिपकार्ट या अमेज़न पर होता है)।
        
        कड़े नियम:
        1. तुम्हारा जवाब सिर्फ और सिर्फ एक नंबर होना चाहिए (जैसे: 4.5, 3.8, 4.2)।
        2. नंबर के अलावा कोई और शब्द, स्टार का सिंबल या कोई वाक्य मत लिखना।
        """
        
        # यहाँ Gemini इंटरनेट के नॉलेज के हिसाब से अपना दिमाग चलाकर जवाब सोचेगा
        response = model.generate_content(prompt)
        
        # जो जवाब (नंबर) आएगा, उसे साफ करके फ्लोट (Float यानी पॉइंट वाले नंबर) में बदलेंगे
        score_text = response.text.strip()
        score = float(score_text)
        
        return score
        
    except Exception as e:
        print(f"ओह! बैकएंड में कुछ गड़बड़ हो गई: {e}")
        # अगर कभी इंटरनेट या API काम न करे, तो सेफ साइड के लिए हम 4.0 स्टार रेटिंग दे देंगे
        return 4.0

  
