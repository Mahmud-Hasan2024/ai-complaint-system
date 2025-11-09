# 🧠 AI Complaint System

An intelligent and user-friendly **Complaint Management System** built with **Django**, designed to help users submit, manage, and resolve complaints efficiently.  
It includes **Admin Dashboard**, **User Authentication**, and **Role-based Access Control** (Admins and Regular Users).

---

## 🚀 Features

### 👤 User Features
- 📝 Submit and manage personal complaints  
- 📊 View complaint status (Pending, Noticed, or Resolved)  
- 🔔 Receive real-time notifications about complaint updates  
- 🗂️ View complaint history in **My Complaints** page  

### 🛠️ Admin Features
- 📋 View all submitted complaints  
- 🧾 Change complaint status instantly (Pending / Noticed / Resolved)  
- 👥 Manage users and oversee complaint statistics  
- 📊 Dashboard with key metrics:
  - Total Complaints  
  - Average Importance Score  
  - Top Users  
  - Recent Complaints  

---

## 🏗️ Tech Stack

| Category | Technology |
|-----------|-------------|
| **Backend** | Django (Python) |
| **Frontend** | HTML, TailwindCSS |
| **Database** | SQLite (default), PostgreSQL (optional) |
| **Authentication** | Django’s built-in auth system |
| **Templating** | Django Templates |
| **Role Handling** | Django Groups & Permissions |

---

## 🖼️ Pages Overview

| Page | Description |
|------|--------------|
| **Home Page** | Users can post new complaints and view others’ complaints |
| **My Complaints** | Lists all complaints by the logged-in user |
| **Notifications** | Displays messages or updates related to user complaints |
| **Dashboard (Admin)** | Shows statistics and allows managing complaint statuses |
| **Login/Register** | Secure authentication and registration system |

---

## 🔐 Role System

| Role | Permissions |
|------|--------------|
| 👤 **User** | Can post, view, and delete their own complaints |
| 🧑‍💼 **Admin** | Can manage all complaints, change statuses, and view analytics |
| 👑 **Superuser** | Full access including user/group management |

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally 👇

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/AI-Complaint-System.git
cd AI-Complaint-System
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv ai_env
source ai_env/bin/activate   # For Mac/Linux
ai_env\Scripts\activate      # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

### 5️⃣ Create a Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Start the Server

```bash
python manage.py runserver
```

Then open your browser and visit 👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🧩 Directory Structure

```bash
AI-Complaint-System/
│
├── complaints/                # Core app
│   ├── templates/complaints/  # HTML templates
│   ├── views.py               # Application logic
│   ├── models.py              # Database models
│   ├── urls.py                # App routes
│   └── ...
│
├── ai_complaint_system/       # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── static/                    # CSS, JS, images
├── manage.py
└── README.md
```

---

## 🎨 UI Highlights

✨ **Clean TailwindCSS UI**  
📱 **Responsive on all devices**  
🌈 **Beautiful dashboard cards and complaint layout**

---

## 💡 Future Improvements

-   🤖 Integrate AI-based complaint categorization
    
-   📬 Add email or SMS notifications
    
-   🕒 Implement complaint tracking timeline
    
-   🌐 Multi-language support
    

---

## 🧑‍💻 Author

**Mahamud Hasan**  
Backend Developer & DevOps Enthusiast  
📧 \[Your Email Here\]  
🔗 [GitHub Profile](https://github.com/yourusername)

---

## 🪪 License

This project is licensed under the **MIT License**.  
Feel free to use and modify it with attribution.

---

> “A good system listens to complaints — a great system learns from them.” 💬