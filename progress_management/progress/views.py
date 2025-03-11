from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Progress
from .forms import ProgressForm

@login_required
def progress_list(request):
    progresses = Progress.objects.filter(user=request.user)
    form = ProgressForm()  # フォームを作成
    return render(request, 'progress/progress_list.html', {'progresses': progresses, 'form': form})


@login_required
def add_progress(request):
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.user = request.user  # ユーザー情報を追加
            progress.save()
            return redirect('progress:progress_list')
    else:
        form = ProgressForm()
    return render(request, 'progress/progress_list.html', {'form': form})


@login_required
def edit_progress(request, progress_id):
    progress = get_object_or_404(Progress, id=progress_id, user=request.user)

    if request.method == 'POST':
        form = ProgressForm(request.POST, instance=progress)
        if form.is_valid():
            form.save()
            return redirect('progress:progress_list')
    else:
        form = ProgressForm(instance=progress)

    return render(request, 'progress/progress_edit.html', {'form': form})

@login_required
def delete_progress(request, progress_id):
    progress = get_object_or_404(Progress, id=progress_id, user=request.user)
    if request.method == 'POST':
        progress.delete()
        return redirect('progress:progress_list')
    return render(request, 'progress/delete_progress.html', {'progress': progress})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Progress, SubPage
from .forms import ProgressForm, SubPageForm

@login_required
def subpage_list(request, game_id):
    game = get_object_or_404(Progress, id=game_id)
    subpages = SubPage.objects.filter(game=game)
    form = SubPageForm()
    return render(request, 'progress/subpage_list.html', {'game': game, 'subpages': subpages, 'form': form})

@login_required
def add_subpage(request, game_id):
    game = get_object_or_404(Progress, id=game_id)
    if request.method == 'POST':
        form = SubPageForm(request.POST, request.FILES)
        if form.is_valid():
            subpage = form.save(commit=False)
            subpage.game = game
            subpage.save()
            return redirect('progress:subpage_list', game_id=game_id)
    else:
        form = SubPageForm()
    return render(request, 'progress/subpage_list.html', {'form': form})
