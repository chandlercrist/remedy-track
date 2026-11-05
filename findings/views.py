

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from .forms import FindingForm
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


@login_required(login_url="/admin/login/")
def finding_list(request):
    findings = Finding.objects.all().order_by("id")

    severity = request.GET.get("severity", "")
    status = request.GET.get("status", "")

    if severity in dict(Finding.SEVERITY_CHOICES):
        findings = findings.filter(severity=severity)
    else:
        severity = ""

    if status in dict(Finding.STATUS_CHOICES):
        findings = findings.filter(status=status)
    else:
        status = ""

    context = {
        "findings": findings,
        "severity_choices": Finding.SEVERITY_CHOICES,
        "status_choices": Finding.STATUS_CHOICES,
        "selected_severity": severity,
        "selected_status": status,
    }

    return render(request, "findings/finding_list.html", context)


@login_required(login_url="/admin/login/")
@permission_required("findings.add_finding", raise_exception=True)
def finding_create(request):
    if request.method == "POST":
        form = FindingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("finding_list")
    else:
        form = FindingForm()

    return render(
        request,
        "findings/finding_form.html",
        {"form": form}
    )

