from .forms import GamePlanForm, TaskForm, FeedbackForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import GamePlan, Feedback, Task
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required

@login_required
def main_page(request):
    game_plans = GamePlan.objects.filter(user=request.user).order_by('-created_at')

    if request.method == "POST":
        form = GamePlanForm(request.POST, request.FILES)
        if form.is_valid():
            new_plan = form.save(commit=False)
            new_plan.user = request.user  # ユーザー情報を保存
            new_plan.save()
            return redirect('plans:main_page')
    else:
        form = GamePlanForm()

    return render(request, 'plans/main_page.html', {
        'game_plans': game_plans,
        'form': form,
    })

@login_required
def game_detail(request, game_id):
    # ユーザー制限を追加
    game_plan = get_object_or_404(GamePlan, id=game_id, user=request.user)
    
    tasks_not_started = game_plan.tasks.filter(status='not_started')
    tasks_in_progress = game_plan.tasks.filter(status='in_progress')
    tasks_completed = game_plan.tasks.filter(status='completed')
    feedbacks = game_plan.feedbacks.all().order_by('-created_at')

    task_form = TaskForm()
    feedback_form = FeedbackForm()

    if request.method == "POST":
        form_type = request.POST.get("form_type")  # どのフォームが送信されたか判別
        if form_type == "task_form":
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                new_task = task_form.save(commit=False)
                new_task.game_plan = game_plan
                new_task.save()
                return redirect('plans:game_detail', game_id=game_id)
        elif form_type == "feedback_form":
            feedback_form = FeedbackForm(request.POST)
            if feedback_form.is_valid():
                new_feedback = feedback_form.save(commit=False)
                new_feedback.game_plan = game_plan
                new_feedback.user = request.user  # ログインユーザーをセット
                new_feedback.save()
                return redirect('plans:game_detail', game_id=game_id)

    # 円グラフ用のデータを追加
    task_data = {
        'not_started': tasks_not_started.count(),
        'in_progress': tasks_in_progress.count(),
        'completed': tasks_completed.count(),
    }

    return render(request, 'plans/game_detail.html', {
        'game_plan': game_plan,
        'tasks_not_started': tasks_not_started,
        'tasks_in_progress': tasks_in_progress,
        'tasks_completed': tasks_completed,
        'task_form': task_form,
        'feedback_form': feedback_form,
        'feedbacks': feedbacks,
        'task_data': task_data,  # 追加
    })




@csrf_exempt
def update_task_status(request, task_id, new_status):
    task = get_object_or_404(Task, id=task_id)
    valid_statuses = ['not_started', 'in_progress', 'completed']

    if new_status in valid_statuses:
        task.status = new_status
        task.save()

        # 進捗率とタスク数を再計算
        game_plan = task.game_plan
        total_tasks = game_plan.tasks.count()
        completed_tasks = game_plan.tasks.filter(status='completed').count()
        in_progress_tasks = game_plan.tasks.filter(status='in_progress').count()
        not_started_tasks = game_plan.tasks.filter(status='not_started').count()

        progress_percentage = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

        return JsonResponse({
            'success': True,
            'progress_percentage': progress_percentage,
            'task_data': {
                'not_started': not_started_tasks,
                'in_progress': in_progress_tasks,
                'completed': completed_tasks
            }
        })

    return JsonResponse({'success': False, 'error': 'Invalid status'}, status=400)

@login_required
def add_feedback(request, game_id):
    game_plan = get_object_or_404(GamePlan, id=game_id, user=request.user)

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user  # ログインユーザーをセット
            feedback.game_plan = game_plan
            feedback.save()
            return redirect('plans:game_detail', game_id=game_id)
