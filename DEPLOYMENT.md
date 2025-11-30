# 🚀 Deployment Guide — AI Complaint System

## 🌍 Live Deployment

- **Production:** https://ai-complaint-system-p1ox.onrender.com
- **GitHub:** https://github.com/Mahmud-Hasan2024/ai-complaint-system

---

## 👤 Demo Accounts

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

## 🧠 Hosting Information

### Platform

- **Render** (Free Tier)

### Production Database

- **PostgreSQL**

---

## ⚙️ Deployment Steps for Render

1. Push code to GitHub
2. Go to **Dashboard → New Web Service**
3. Connect GitHub repo
4. Choose:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn ai_complaint_system.wsgi`
5. Add environment variables:
   - `DEBUG=False`
   - `SECRET_KEY=<your-secret-key>`
   - `DATABASE_URL=<render_postgres_url>`
6. Add static file settings in Django & Render
7. Deploy 🚀

---

## 📦 Static Files (Production)

Run locally before deployment if needed:

```bash
python manage.py collectstatic
```

---

## 🔔 Notes

- Admin Dashboard accessible only for admins
- Ensure DEBUG=False in production
- Free tier may sleep after inactivity

---
