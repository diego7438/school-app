# Windward School Companion App 🦁

A comprehensive web application designed to help Windward School students and faculty manage daily schedules, announcements, and academic tracking.

## 🌐 Live Access

The application is deployed and accessible via the web:

**🔗 [Windward Companion App](https://school-app-wza8.onrender.com)**

*Note: The application is hosted on Render's free tier. It may take a minute to wake up if it hasn't been accessed recently.*

## � Features

*   **Dynamic Rotation Schedule:** Automatically calculates the daily rotation (Days 1-6) based on the current date, handling holidays and special schedules.
*   **Role-Based Access:**
    *   **Students:** View schedules, chat with the AI bot, and check grades.
    *   **Teachers:** Post announcements, manage student grades, and view rosters.
*   **AI Schedule Assistant:** A chatbot that answers natural language questions about the schedule (e.g., "What is the rotation for next Tuesday?").
*   **Announcements System:** Digital bulletin board for teacher-posted updates.
*   **Secure Authentication:** User registration and login with hashed passwords.

## 🛠️ Tech Stack

*   **Backend:** Python, Flask
*   **Database:**
    *   **Development:** SQLite (Local)
    *   **Production:** PostgreSQL (Render)
*   **Frontend:** HTML5, CSS3, JavaScript
*   **Deployment:** Render Cloud Hosting

## 📂 Project Structure

*   `my_windward_app/`: Main application source code.
    *   `templates/`: HTML files for the frontend.
    *   `static/`: CSS and JavaScript files.
    *   `auth.py`: Handles user registration and login logic.
    *   `db.py`: Database connection and management (SQLite/PostgreSQL).
*   `init_db.py`: Script to initialize the database tables.
*   `requirements.txt`: List of Python dependencies.

## ⚙️ Local Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd my_windward_app
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Initialize the database:**
    ```bash
    python3 init_db.py
    ```

4.  **Run the application:**
    ```bash
    flask --app my_windward_app run --debug
    ```

## 📝 License
Created by Diego Anderson for Honors Software Engineering.