from .models import Game  # Gameモデルをインポート

def progress_links(request):
    return {
        'progress_games': Game.objects.all()
    }
