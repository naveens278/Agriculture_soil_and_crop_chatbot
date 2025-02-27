from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# Crop data based on soil type
crop_data = {
    "clay": ["Rice", "Wheat", "Sugarcane"],
    "sandy": ["Peanut", "Watermelon", "Carrot"],
    "loamy": ["Cotton", "Tomato", "Barley"],
    "black": ["Soybean", "Sunflower", "Cotton"]
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_crop', methods=['GET'])
def get_crop():
    soil_type = request.args.get('soil', '').strip().lower()

    if not soil_type:
        return jsonify({"error": "No soil type provided"}), 400

    crops = crop_data.get(soil_type, ["No suitable crops found"])
    return jsonify({"soil": soil_type, "crop": ", ".join(crops)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
