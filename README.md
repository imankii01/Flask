# Flask Backend Learning Series 🚀

This repository is a structured guide to learning **Flask** for backend development. It covers fundamental concepts, best practices, and hands-on projects to build scalable web applications using Python.

## 📌 What You'll Learn

- Setting up a Flask project
- Creating RESTful APIs with Flask
- Using Blueprints for modular architecture
- Connecting Flask with databases (SQLAlchemy)
- User authentication & JWT-based security
- Handling middleware, logging, and error handling
- Deploying Flask applications

## 🏗 Folder Structure

```
/flask-backend
│── /app            # Main application
│   ├── /routes     # API endpoints
│   ├── /models     # Database models
│   ├── /services   # Business logic
│   ├── /utils      # Helper functions
│── /tests          # Unit tests
│── .env            # Environment variables
│── requirements.txt # Dependencies
│── run.py          # Entry point
```

## 🚀 Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/flask-learning-series.git
   cd flask-learning-series
   ```

2. **Set Up Virtual Environment & Install Dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # (Windows: venv\Scripts\activate)
   pip install -r requirements.txt
   ```

3. **Run the Flask Server**
   ```bash
   python run.py
   ```

## 📖 Resources

- [Flask Official Docs](https://flask.palletsprojects.com/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [JWT Authentication](https://pyjwt.readthedocs.io/en/latest/)
