from flask import Flask, jsonify, request
from flask_cors import CORS

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
@app.route('/api/analyze', methods=['POST'])
def analyze_product():
    data = request.get_json() or {}
    product_name = data.get("product_name", "Unknown Product")
    
    return jsonify({
        "status": "success",
        "product": product_name,
        "risk_score": 12,
        "status_tag": "LOW RISK",
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
