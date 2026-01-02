# Windward School Dashboard & AI Assistant 🦁

A full-stack web application designed for Windward School students and teachers. It features a dynamic rotation schedule calculator, a teacher dashboard for grading, and an AI-powered chatbot that answers questions about the school calendar.

## 🚀 Features

*   **Dynamic Schedule Parsing:** Automatically calculates the rotation day (1-6) based on the current date, handling weekends and holidays.
*   **AI Chatbot:** A "smart" assistant that uses Regex and timezone-aware logic to answer natural language questions like *"What is the rotation on August 25?"* or *"Is there school tomorrow?"*.
*   **User Roles:** Separate dashboards for **Students** (view schedule/grades) and **Teachers** (post announcements/edit grades).
*   **Security:**
    *   Password Hashing (Werkzeug)
    *   Session Management
    *   HTTP Security Headers (Clickjacking & XSS protection)
    *   Input Sanitization
*   **Timezone Awareness:** Server-side logic forces `America/Los_Angeles` time to ensure the schedule is accurate regardless of where the server is hosted.

## 🛠️ Tech Stack

*   **Backend:** Python, Flask
*   **Database:** PostgreSQL (Production), SQLite (Dev)
*   **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
*   **Deployment:** Render (Gunicorn WSGI)

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/my_windward_app.git
    cd my_windward_app
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Initialize the database:**
    ```bash
    flask --app my_windward_app init-db
    ```

4.  **Run the application:**
    ```bash
    flask --app my_windward_app run --debug
    ```

## 🛡️ Security Note

This application implements **OWASP** best practices, including `X-Frame-Options` to prevent clickjacking and strict input validation on the chat interface to prevent DoS attacks.

---
*Built by Diego Anderson for Honors Software Engineering.*