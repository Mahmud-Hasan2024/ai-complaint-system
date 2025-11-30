# 🧠 AI Complaint System

An intelligent and user-friendly **Complaint Management System** built with **Django**, designed to help users submit, manage, and resolve complaints efficiently.  
It includes **Admin Dashboard**, **User Authentication**, and **Role-based Access Control** (Admins and Regular Users).

---

## 🌍 Live Demo & Repository

- **🔗 Live Site:** https://ai-complaint-system-p1ox.onrender.com
- **📁 GitHub Repository:** https://github.com/Mahmud-Hasan2024/ai-complaint-system

---

## 🚀 Features

### 👤 User Features

- 📝 Submit and manage personal complaints
- 📊 View complaint status (Pending, Noticed, Resolved)
- 🔔 Receive notifications
- 🗂️ View complaint history

### 🛠️ Admin Features

- 📋 View all complaints
- 🧾 Update status
- 👥 Manage users
- 📊 View dashboard metrics

---

## 🏗️ Tech Stack

| Category     | Technology                  |
| ------------ | --------------------------- |
| **Backend**  | Django (Python)             |
| **Frontend** | HTML, TailwindCSS           |
| **Database** | SQLite / PostgreSQL         |
| **Auth**     | Django Auth System          |
| **Roles**    | Django Groups & Permissions |

---

## 🖼️ Pages Overview

| Page                  | Description                      |
| --------------------- | -------------------------------- |
| **Home Page**         | Submit & view complaints         |
| **My Complaints**     | List user-specific complaints    |
| **Notifications**     | System updates                   |
| **Dashboard (Admin)** | Analytics + complaint management |
| **Login/Register**    | Secure forms                     |

---

## 🔐 Demo Credentials

### **Admin Accounts**

| Role  | Username       | Password   |
| ----- | -------------- | ---------- |
| Admin | `admin_rashid` | `password` |
| Admin | `admin_sadia`  | `password` |

### **Normal Users**

| Role | Username  | Password   |
| ---- | --------- | ---------- |
| User | `mahmud`  | `password` |
| User | `fahim`   | `password` |
| User | `sumaiya` | `password` |
| User | `arif`    | `password` |
| User | `nishat`  | `password` |

---

## 📄 Additional Documentation

- 📦 **[Deployment Guide](DEPLOYMENT.md)**
- 👨‍💻 **[About the Author](ABOUT_AUTHOR.md)**
- 🪪 **[License](LICENSE.md)**

Clicking the links will open the respective files.

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/Mahmud-Hasan2024/ai-complaint-system.git
cd ai-complaint-system
python -m venv env
source env/bin/activate   # macOS/Linux
env\Scripts\activate      # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🧩 Directory Structure

```bash
AI-Complaint-System/
│
├── complaints/
│   ├── templates/complaints/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│
├── ai_complaint_system/
│   ├── settings.py
│   ├── urls.py
│
├── static/
├── manage.py
└── README.md
```

---

## 🎨 UI Highlights

- ✨ Clean TailwindCSS UI
- 📱 Fully Responsive
- 🌈 Beautiful Admin Dashboard

---

## 💡 Future Improvements

- 🤖 AI-based complaint categorization
- 📬 Email & SMS notifications
- 🕒 Complaint timeline
- 🌐 Multi-language support

---

## 🧑‍💻 Author

**Mahamud Hasan**  
Backend Developer & DevOps Enthusiast  
📄 Learn more → **[ABOUT_AUTHOR.md](ABOUT_AUTHOR.md)**

---

## 🪪 License

This project is licensed under the **MIT License**.  
📄 Full text → **[LICENSE.md](LICENSE.md)**

---

> “A good system listens to complaints — a great system learns from them.” 💬
