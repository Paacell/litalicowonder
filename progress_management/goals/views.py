from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Goal
from .forms import GoalForm

def is_admin(user):
    return user.is_staff  # 管理者かどうかチェック

@login_required
def goal_list(request):
    goal = Goal.objects.first()  # 目標は1つだけ管理
    return render(request, "goals/goal_list.html", {"goal": goal})

@user_passes_test(is_admin)  # 管理者のみ編集可能
@login_required
def edit_goal(request):
    goal = Goal.objects.first()
    if not goal:
        goal = Goal.objects.create(title="未設定", description="ここに目標を入力してください。")

    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("goals:goal_list")
    else:
        form = GoalForm(instance=goal)

    return render(request, "goals/edit_goal.html", {"form": form})
