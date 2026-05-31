import os
# 1. सबसे पहले हम गूगल की जादुई लाइब्रेरी को बुला रहे हैं
import google.generativeai as genai

# 2. यहाँ आपको अपनी जादुई चाबी (Gemini API Key) डालनी है
# जो चाबी आपके पास है, उसे नीचे वाले सिंगल कोट ' ' के बीच में लिख दें
GEMINI_API_KEY = 'AlzaSyDQFZ09xJmzy_6q0YJnaqE4ncqac7XK11s'

# 3. यह लाइन गूगल को आपकी चाबी दिखाकर परमिशन लेगी
genai.configure(api_key=GEMINI_API_KEY)

# 4. यह हमारा असली फंक्शन है जो आपके 10 सोर्सेज (यूट्यूब, रेडिट आदि) का एनालिसिस करेगा
def get_trust_score(product_name):
    try:
        # हम गूगल के सबसे तेज मॉडल 'gemini-1.5-flash' का इस्तेमाल कर रहे हैं
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # हम Gemini को समझा रहे हैं कि उसे इंटरनेट के 10 सोर्सेज के हिसाब से स्कोर देना है
        prompt = f"तुम एक एक्सपर्ट प्रोडक्ट एनालिस्ट हो। प्रोडक्ट '{product_name}' के बारे में इंटरनेट (YouTube, Reddit, Twitter, MouthShut, Trustpilot आदि) पर मौजूद रिव्यूज और चर्चाओं को एनालाइज करो। इस प्रोडक्ट को 1 से 10 के बीच में एक फाइनल 'Trust Score' (भरोसा स्कोर) दो। जवाब में सिर्फ और सिर्फ एक नंबर (जैसे 8.5 या 7.2) लिखना, कोई और शब्द मत लिखना।"
        
        # यहाँ Gemini अपना दिमाग चलाकर जवाब सोचेगा
        response = model.generate_content(prompt)
        
        # जो जवाब आएगा उसे नंबर में बदलकर भेजेंगे
        score = float(response.text.strip())
        return score
        
    except Exception as e:
        print(f"ओह! कुछ गड़बड़ हो गई: {e}")
        return 5.0  # गड़बड़ होने पर सेफ साइड के लिए 5.0 स्कोर दे रहे हैं
        
  
