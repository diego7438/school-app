# Windward School App 🦁

A full-stack Flask application designed for Windward School students and teachers to manage schedules, announcements, and grades.

## 🚀 Features

*   **🔐 Secure Authentication:** Login and registration system with password hashing.
*   **👤 Role-Based Access:**
    *   **Students:** View daily rotation, check announcements, see profile.
    *   **Teachers:** Post announcements, view student roster, assign grades.
*   **📅 Daily Rotation Checker:** Automatically calculates the specific class rotation (Days 1-6) for any date in the 2025-26 school year, handling holidays and weekends.
*   **🤖 AI Chatbot:** Smart assistant that answers questions about the schedule (e.g., "What is the rotation tomorrow?" or "Is there school on Monday?").
*   **📢 Announcements Board:** Digital bulletin board for school news.
*   **📊 Teacher Dashboard:** Interface for teachers to manage student grades.
*   **🎨 Modern UI:** Flashy landing page and auto-generated user avatars.

## 🛠️ Tech Stack

*   **Backend:** Python, Flask
*   **Database:** SQLite
*   **Frontend:** HTML, CSS, JavaScript

## 📚 Architecture Concepts

*   **Blueprints:** This project uses Flask Blueprints to organize code into modular components (e.g., `auth`, `teacher`, `chat`). This keeps the codebase clean and scalable, rather than having one massive file.
*   **Application Factory:** We use the `create_app()` function to set up the app, which allows for better testing and configuration management.
*   **Decorators:** Custom Python decorators (like `@role_required`) are used to enforce security permissions on specific routes.

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

## ☁️ Deployment (Render)

*   **Build Command:** `pip install -r requirements.txt && python3 init_db.py`
    *   *Note: This installs dependencies and resets the database.*
*   **Start Command:** `gunicorn "my_windward_app:create_app()" --bind 0.0.0.0:$PORT`

## 🔮 Future Roadmap (Winter Break Goals)

*   [x] **🤖 AI Assistant:** Implement a Natural Language Processing (NLP) chatbot to answer questions about the schedule (e.g., "Is there school next Friday?").
*   [x] **☁️ Deployment:** Hosted on Render with a production-ready web server (Gunicorn).
*   [x] **🎨 UI Polish:** Refactored frontend to use a centralized CSS stylesheet and base template for a consistent, professional, dark-mode theme.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.