🌿 Agriculture Chatbot 
📌 Project Overview
The Agriculture Chatbot is a simple web-based application that suggests suitable crops based on the soil type provided by the user. It is built using Flask for the backend and HTML, CSS, and JavaScript for the frontend.

🏗️ Project Structure

agriculture_chatbot/
│── app.py             
│── templates/
│   ├── index.html     
│── static/
│   ├── style.css      
│── requirements.txt   
│── README.md          

🔧 Installation and Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/agriculture-chatbot.git
cd agriculture-chatbot
2️⃣ Install Dependencies
Ensure you have Python 3.x installed, then install the required packages using:
pip install flask flask-cors
3️⃣ Run the Flask Server
python app.py
The server will start on http://127.0.0.1:5000/.

🎯 How to Use
Open your browser and visit http://127.0.0.1:5000/.
Enter a soil type in the input field (e.g., clay, sandy, loamy, black).
Click the "Ask" button.
The chatbot will suggest suitable crops for the entered soil type.
🖥️ Tech Stack
Backend: Flask (Python)
Frontend: HTML, CSS, JavaScript
Styling: CSS (Custom)
Communication: Fetch API (AJAX)
🚀 Features
✔️ User-friendly chat-based UI
✔️ Fast and responsive Flask API
✔️ Simple and lightweight design
✔️ Works on all modern browsers
✔️ Expandable with more soil types & crops

⚙️ Configuration
If you want to modify the crop recommendations, edit the crop_data dictionary in app.py:
crop_data = {
    "clay": ["Rice", "Wheat", "Sugarcane"],
    "sandy": ["Peanut", "Watermelon", "Carrot"],
    "loamy": ["Cotton", "Tomato", "Barley"],
    "black": ["Soybean", "Sunflower", "Cotton"]
}
Add more soil types and their respective crops as needed.

🛠️ Troubleshooting
Issue: Bot: Could not connect to server.
✅ Solution: Ensure Flask is running by executing:
python app.py
Issue: No crops displayed for a soil type.
✅ Solution: Check crop_data in app.py and ensure the soil type exists.

🏆 Contributing
Want to improve the chatbot? Feel free to contribute:

Fork the repo 📂
Create a new branch (git checkout -b feature-branch)
Make your changes 🛠️
Push and submit a PR 🚀
