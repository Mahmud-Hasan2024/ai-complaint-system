import openai
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.db.models import Avg, Count
from .models import Complaint
from .models import Notification


# Create your views here.

openai.api_key = settings.OPENAI_API_KEY

# 🔹 Helpers
def get_ai_importance_score(text):
    prompt = f"""Rate this complaint from 1 to 10 based on urgency and seriousness.
    Only return a number. Complaint: {text}"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10,
        )
        score = int(''.join([c for c in response.choices[0].message.content if c.isdigit()]))
        return max(1, min(score, 10))
    except Exception:
        return 5


def is_admin(user):
    return user.is_superuser or user.groups.filter(name="Admin").exists()

# 🔹 User Pages
@login_required
def home(request):
    if request.method == "POST":
        complaint_text = request.POST.get("complaint")
        importance = get_ai_importance_score(complaint_text)
        Complaint.objects.create(user=request.user, complaint=complaint_text, importance=importance)
        return redirect("home")

    complaints = Complaint.objects.all().order_by("-importance", "-created_at")
    return render(request, "complaints/home.html", {"complaints": complaints})


# 🔹 Authentication
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            return render(request, "complaints/register.html", {"error": "Username already exists!"})
        user = User.objects.create_user(username=username, password=password)
        group, _ = Group.objects.get_or_create(name="User")
        user.groups.add(group)
        return redirect("login")
    return render(request, "complaints/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "complaints/login.html", {"error": "Invalid credentials"})
    return render(request, "complaints/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


# 🔹 Admin Dashboard
@user_passes_test(is_admin)
def dashboard(request):
    stats = {
        "total_complaints": Complaint.objects.count(),
        "avg_importance": round(Complaint.objects.aggregate(Avg("importance"))["importance__avg"] or 0, 2),
        "top_users": Complaint.objects.values("user__username").annotate(count=Count("id")).order_by("-count")[:5],
        "recent_complaints": Complaint.objects.all().order_by("-created_at")[:5],
    }
    return render(request, "complaints/dashboard.html", {"stats": stats})

@login_required
def my_complaints(request):
    complaints = Complaint.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "complaints/my_complaints.html", {"complaints": complaints})


@login_required
def update_status(request, complaint_id):
    if not is_admin(request.user):
        return redirect("home")
    complaint = Complaint.objects.get(id=complaint_id)
    new_status = request.GET.get("status")  # changed from POST to GET
    if new_status in dict(Complaint.STATUS_CHOICES).keys():
        complaint.status = new_status
        complaint.save()

        # Create notification for the complaint owner
        Notification.objects.create(
            user=complaint.user,
            message=f"Your complaint '{complaint.complaint[:50]}' was marked as {new_status}."
        )

    return redirect("home")


@login_required
def delete_complaint(request, complaint_id):
    complaint = Complaint.objects.filter(id=complaint_id, user=request.user).first()
    if complaint:
        complaint.delete()
    return redirect("my_complaints")

@login_required
def notifications(request):
    notes = Notification.objects.filter(user=request.user).order_by("-created_at")
    # Mark all as read when opened
    notes.update(is_read=True)
    return render(request, "complaints/notifications.html", {"notes": notes})


