# from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# from .models import Progress
# from .forms import ProgressForm

# @login_required
# def progress_list(request):
#     progresses = Progress.objects.filter(user=request.user)
#     form = ProgressForm()  # フォームを作成
#     return render(request, 'progress/progress_list.html', {'progresses': progresses, 'form': form})


# @login_required
# def add_progress(request):
#     if request.method == 'POST':
#         form = ProgressForm(request.POST)
#         if form.is_valid():
#             progress = form.save(commit=False)
#             progress.user = request.user  # ユーザー情報を追加
#             progress.save()
#             return redirect('progress:progress_list')
#     else:
#         form = ProgressForm()
#     return render(request, 'progress/progress_list.html', {'form': form})


# @login_required
# def edit_progress(request, progress_id):
#     progress = get_object_or_404(Progress, id=progress_id, user=request.user)

#     if request.method == 'POST':
#         form = ProgressForm(request.POST, instance=progress)
#         if form.is_valid():
#             form.save()
#             return redirect('progress:progress_list')
#     else:
#         form = ProgressForm(instance=progress)

#     return render(request, 'progress/progress_edit.html', {'form': form})

# @login_required
# def delete_progress(request, progress_id):
#     progress = get_object_or_404(Progress, id=progress_id, user=request.user)
#     if request.method == 'POST':
#         progress.delete()
#         return redirect('progress:progress_list')
#     return render(request, 'progress/delete_progress.html', {'progress': progress})

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Game, Progress
from .forms import ProgressForm

@login_required
def game_progress_view(request, game_id):
    """
    指定したゲームの進捗一覧を表示するビュー
    """
    game = get_object_or_404(Game, pk=game_id)
    progresses = game.progresses.order_by('-updated_at')  # Gameモデルにrelated_name='progresses'が定義されている前提
    form = ProgressForm()
    context = {
        'game': game,
        'progresses': progresses,
        'form': form,
    }
    return render(request, 'progress/game_progress.html', context)

@login_required
def add_progress(request, game_id):
    """
    進捗追加の処理。POST送信の場合、フォームのバリデーション後にProgressを作成。
    AJAXリクエストの場合はJSONレスポンス、通常リクエストの場合はリダイレクト。
    """
    if request.method == 'POST':
        game = get_object_or_404(Game, pk=game_id)
        form = ProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.game = game  # 関連するゲームを設定
            progress.save()
            # AJAXの場合はJSONレスポンス
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': '進捗が追加されました。'})
            return redirect('progress:game_progress', game_id=game.id)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseBadRequest("不正なリクエストです。")

@login_required
def edit_progress(request, progress_id):
    """
    進捗編集用のビュー。GETでフォームを表示し、POSTで更新処理を行う。
    """
    progress = get_object_or_404(Progress, pk=progress_id)
    if request.method == 'POST':
        form = ProgressForm(request.POST, instance=progress)
        if form.is_valid():
            form.save()
            return redirect('progress:game_progress', game_id=progress.game.id)
    else:
        form = ProgressForm(instance=progress)
    context = {
        'form': form,
        'progress': progress,
    }
    return render(request, 'progress/edit_progress.html', context)

@login_required
def delete_progress(request, progress_id):
    """
    進捗削除用のビュー。削除後、該当ゲームの進捗一覧ページにリダイレクト。
    """
    progress = get_object_or_404(Progress, pk=progress_id)
    game_id = progress.game.id
    progress.delete()
    return redirect('progress:game_progress', game_id=game_id)
