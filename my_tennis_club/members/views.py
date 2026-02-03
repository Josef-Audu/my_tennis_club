from django.shortcuts import render, get_object_or_404
from .models import Member
from django.db.models import Q

# -------------------------------
# Legacy view
# -------------------------------
def legacy(request):
    return render(request, 'myfirst.html')


# -------------------------------
# Members list view
# -------------------------------
def members(request):
    mymembers = Member.objects.all()
    return render(request, 'all_member.html', {'mymembers': mymembers})


# -------------------------------
# Member details view
# -------------------------------
def details(request, id):
    mymember = get_object_or_404(Member, id=id)
    return render(request, 'details.html', {'mymember': mymember})


# -------------------------------
# Main page view
# -------------------------------
def main(request):
    return render(request, 'main.html')


# -------------------------------
# Testing view with context
# -------------------------------
def testing(request):
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return render(request, 'template.html', context)
