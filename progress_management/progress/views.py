from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Game, SubPage
from .forms import GameForm, SubPageForm

@login_required
def game_list(request):
    games = Game.objects.filter(user=request.user)  # 🔥 現在のユーザーに限定
    form = GameForm()

    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.user = request.user  # 🔥 ユーザー情報を紐づける
            game.save()
            return redirect('progress:progress_list')

    return render(request, 'progress/progress_list.html', {'games': games, 'form': form})

@login_required
def subpage_list(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    subpages = SubPage.objects.filter(game=game)
    form = SubPageForm()
    if request.method == 'POST':
        form = SubPageForm(request.POST)
        if form.is_valid():
            subpage = form.save(commit=False)
            subpage.game = game
            subpage.save()
            return redirect('progress:subpage_list', game_id=game_id)
    return render(request, 'progress/subpage_list.html', {'game': game, 'subpages': subpages, 'form': form})

# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Plan, GamePlan
# from .forms import GamePlanForm

# def game_detail(request, game_id):
#     game = get_object_or_404(Plan, id=game_id)
    
#     # 既存の計画があれば取得、なければ新規作成
#     game_plan, created = GamePlan.objects.get_or_create(game=game)

#     if request.method == 'POST':
#         form = GamePlanForm(request.POST, instance=game_plan)
#         if form.is_valid():
#             form.save()
#             return redirect('game_detail', game_id=game.id)
#     else:
#         form = GamePlanForm(instance=game_plan)

#     return render(request, 'game_detail.html', {'game': game, 'form': form})
