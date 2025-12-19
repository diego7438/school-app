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

2.  **Set up the environment:**
    ```bash
    # Mac/Linux
    export FLASK_APP=my_windward_app
    export FLASK_DEBUG=1
    ```

3.  **Run the server:**
    ```bash
    python3 -m flask run
    ```

4.  **Open in Browser:**
    Go to `http://127.0.0.1:5000`

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.