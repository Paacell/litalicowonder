from .models import Game  # Gameモデルをインポート

def progress_links(request):
    if request.user.is_authenticated:
        return {
            'progress_games': Game.objects.filter(user=request.user)  # 現在のユーザーに限定
        }
    return {
        'progress_games': []  # 未ログイン時は空リスト
    }
