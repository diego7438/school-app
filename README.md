# Windward School App 🦁

A full-stack Flask application designed for Windward School students and teachers to manage schedules, announcements, and grades.

## 🚀 Features

*   **🔐 Secure Authentication:** Login and registration system with password hashing.
*   **👤 Role-Based Access:**
    *   **Students:** View daily rotation, check announcements, see profile.
    *   **Teachers:** Post announcements, view student roster, assign grades.
*   **📅 Daily Rotation Checker:** Automatically calculates the specific class rotation (Days 1-6) for any date in the 2025-26 school year, handling holidays and weekends.
*   **📢 Announcements Board:** Digital bulletin board for school news.
*   **📊 Teacher Dashboard:** Interface for teachers to manage student grades.

## 🛠️ Tech Stack

*   **Backend:** Python, Flask
*   **Database:** SQLite
*   **Frontend:** HTML, CSS, JavaScript

## ⚙️ How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/diego7438/school-app.git
    cd school-app
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Initialize the Database:**
    Since the database file is not tracked in git, you must initialize it first:
    ```bash
    python3 init_db.py
    ```

4.  **Set up the environment:**
    ```bash
    # Mac/Linux
    export FLASK_APP=my_windward_app
    export FLASK_DEBUG=1
    ```

5.  **Run the server:**
    ```bash
    python3 -m flask run
    ```

6.  **Open in Browser:**
    Go to `http://127.0.0.1:5000`

## 🔮 Future Roadmap (Winter Break Goals)

*   [ ] **🤖 AI Assistant:** Implement a Natural Language Processing (NLP) chatbot to answer questions about the schedule (e.g., "Is there school next Friday?").
*   [ ] **☁️ Deployment:** Host the application on the web so students can access it from their phones.
*   [ ] **🎨 UI Polish:** Upgrade the frontend with a CSS framework for a mobile-responsive design.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.