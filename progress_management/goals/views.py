from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Goal
from .forms import GoalForm

# def is_admin(user):
#     return user.is_staff  # 管理者かどうかチェック

# @login_required
# def goal_list(request):
#     goal = Goal.objects.first()  # 目標は1つだけ管理
#     return render(request, "goals/goal_list.html", {"goal": goal})

# @user_passes_test(is_admin)  # 管理者のみ編集可能
# @login_required
# def edit_goal(request):
#     goal = Goal.objects.first()
#     if not goal:
#         goal = Goal.objects.create(title="未設定", description="ここに目標を入力してください。")

#     if request.method == "POST":
#         form = GoalForm(request.POST, instance=goal)
#         if form.is_valid():
#             form.save()
#             return redirect("goals:student_goal_list")
#     else:
#         form = GoalForm(instance=goal)

#     return render(request, "goals/edit_goal.html", {"form": form})



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Goal
from accounts.models import CustomUser
from .forms import GoalForm

# 教師であるか判定する関数
def is_admin(user):
    return user.is_authenticated and user.is_admin

# 生徒一覧ページ（教師専用）
@login_required
@user_passes_test(is_admin)
def student_list(request):
    students = CustomUser.objects.filter(is_student=True)  # 生徒のみ取得
    return render(request, "goals/student_list.html", {"students": students})

# 生徒ごとの目標一覧（教師専用）
@login_required
@user_passes_test(is_admin)
def student_goal_list(request, student_id):
    student = get_object_or_404(CustomUser, id=student_id, is_student=True)
    goals = Goal.objects.filter(student=student)
    return render(request, "goals/student_goal_list.html", {"student": student, "goals": goals})

# 目標の作成・編集（教師専用）
@login_required
@user_passes_test(is_admin)
def goal_edit(request, goal_id=None):
    if goal_id:
        goal = get_object_or_404(Goal, id=goal_id)
    else:
        goal = None

    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("goals:student_goal_list", student_id=form.cleaned_data["student"].id)
    else:
        form = GoalForm(instance=goal)

    return render(request, "goals/goal_form.html", {"form": form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Goal

# 生徒用: 自分の目標を閲覧
@login_required
def my_goals(request):
    if not request.user.is_student:  # 生徒以外はアクセス不可
        return render(request, "errors/403.html", status=403)

    goals = Goal.objects.filter(student=request.user)  # 自分の目標のみ取得
    return render(request, "goals/my_goals.html", {"goals": goals})
