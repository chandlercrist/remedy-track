
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Finding


@login_required(login_url="/admin/login/")
def dashboard(request):
    context = {
        "open_count": Finding.objects.filter(status="Open").count(),
        "progress_count": Finding.objects.filter(status="In Progress").count(),
        "resolved_count": Finding.objects.filter(status="Resolved").count(),
        "recent_findings": Finding.objects.order_by("-id")[:5],
    }

    return render(request, "findings/dashboard.html", context)

