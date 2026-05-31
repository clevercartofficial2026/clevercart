from flask import Flask, jsonify, request
from flask_cors import CORS

# 🌟 यहाँ हम आपकी बनाई हुई 'analyzer.py' फाइल से असली AI स्कोर लाने वाले फंक्शन को बुला रहे हैं
from analyzer import get_trust_score

app = Flask(__name__)
CORS(app)  # यह आपके index.html (फ्रंटएंड) को बैकएंड से आसानी से कनेक्ट करेगा

# 1. होम रूट (यह चेक करने के लिए कि आपका सर्वर चालू है)
@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "CleverCart AI Server is Running Perfectly!",
        "version": "1.0.0"
    })

# 2. मुख्य AI API एंडपॉइंट (Product Analysis Feature)
# 🌟 इसे हमने GET मेथड पर सेट किया है जैसा हमने आपके script.js में लिखा था
@app.route('/api/analyze', methods=['GET'])
def analyze_product():
    # जावास्क्रिप्ट (URL) से प्रोडक्ट का नाम खींचना
    product_name = request.args.get('product')
    
    if not product_name:
        return jsonify({
            "status": "error",
            "message": "कृपया प्रोडक्ट का नाम भेजें"
        }), 400
    
    print(f"यूजर इस प्रोडक्ट को सर्च कर रहा है: {product_name}")
    
    # 🌟 यहाँ आपकी 'analyzer.py' फाइल काम करेगी और Gemini AI से असली 5-स्टार स्कोर लाएगी
    star_rating = get_trust_score(product_name)
    
    return jsonify({
        "status": "success",
        "product": product_name,
        "trust_score": star_rating,  # यह हमारा असली 5-स्टार स्कोर है
        "message": "AI Analysis completed successfully."
    })

# 3. आपके 10 लाइव रिसोर्सेज (Resources API Tool)
@app.route('/api/resources', methods=['GET'])
def get_resources():
    return jsonify({
        "status": "success",
        "total_resources": 10,
        "resources": [
            {"id": 1, "name": "Product Analyzer", "type": "AI", "status": "Active"},
            {"id": 2, "name": "Risk Assessor", "type": "Security", "status": "Active"},
            {"id": 3, "name": "Fraud Detection", "type": "AI", "status": "Active"},
            {"id": 4, "name": "User Authentication", "type": "Core", "status": "Active"},
            {"id": 5, "name": "Database Connector", "type": "Data", "status": "Active"},
            {"id": 6, "name": "Log Manager", "type": "System", "status": "Active"},
            {"id": 7, "name": "Notification Engine", "type": "Utility", "status": "Active"},
            {"id": 8, "name": "Report Generator", "type": "Analytics", "status": "Active"},
            {"id": 9, "name": "API Rate Limiter", "type": "Security", "status": "Active"},
            {"id": 10, "name": "Cache Controller", "type": "Performance", "status": "Active"}
        ]
    })

if __name__ == '__main__':
    # पोर्ट 5000 सेट है ताकि GitHub Codespaces इसे आसानी से पकड़ सके
    app.run(host='0.0.0.0', port=5000, debug=True)
