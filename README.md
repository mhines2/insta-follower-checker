# Instagram Follow Analyzer 📊

A **Flask + React** web app that helps you analyze your Instagram followers and following lists. It extracts usernames from the downloaded `followers.html` and `following.html` files, compares them, and displays who isn’t following you back.

## 🎨 Features
- 📎 Upload Instagram `followers.html` & `following.html`
- 🔍 Identify users **not following you back**
- 📊 View results in a clean **React UI**
- 🌐 Simple **Flask API** for processing data
- 🔥 Fully open-source and easy to extend!

## 📂 Project Structure
```
📁 insta-follow-analyzer/
├── backend/          # Flask API backend
│   ├── app.py        # Main Flask application
│   ├── requirements.txt  # Python dependencies
│   └── uploads/      # Folder for uploaded HTML files
├── frontend/         # React frontend
│   ├── src/          # React source files
│   ├── public/       # Public assets
│   ├── package.json  # Frontend dependencies
│   └── index.js      # React entry point
└── README.md         # Project documentation
```

## 🛠 Installation & Setup

### Backend (Flask)
1. Clone the repository:
   ```sh
   git clone https://github.com/mhines2/insta-follower-checker.git
   cd insta-follow-analyzer/backend
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run Flask server:
   ```sh
   python app.py
   ```

### Frontend (React)
1. Navigate to the frontend:
   ```sh
   cd ../frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start React development server:
   ```sh
   npm start
   ```

## 📸 Usage
1. Download your Instagram data from **Settings > Privacy > Download Your Information**.
2. Extract the ZIP file and locate `followers.html` and `following.html`.
3. Upload both files in the web app.
4. Click **Analyze** and see who isn’t following you back!

## 🚀 Future Enhancements
- 📊 Add data visualization (charts)
- 📉 Track unfollowers over time
- 🌍 Deploy to the cloud (Heroku, Vercel)

---
