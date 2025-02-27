from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .models import Portfolio
# from .forms import PortfolioForm

# @login_required
# def portfolio_list(request):
#     portfolios = Portfolio.objects.filter(student=request.user)
#     form = PortfolioForm()
#     return render(request, "portfolio/portfolio_list.html", {"portfolios": portfolios, "form": form})

@login_required
def add_portfolio(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect("portfolio:portfolio_list")
    return redirect("portfolio:portfolio_list")

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import PortfolioProject
from .forms import PortfolioForm

@login_required
def portfolio_list(request):
    projects = PortfolioProject.objects.filter(user=request.user)
    form = PortfolioForm()  # フォームを作成
    return render(request, 'portfolio/portfolio_list.html', {'projects': projects, 'form':form})

@login_required
def edit_portfolio(request, project_id):
    project = get_object_or_404(PortfolioProject, id=project_id, user=request.user)

    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('portfolio:portfolio_list')
    else:
        form = PortfolioForm(instance=project)

    return render(request, 'portfolio/edit_portfolio.html', {'form': form})

@login_required
def delete_portfolio(request, project_id):
    project = get_object_or_404(PortfolioProject, id=project_id, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio:portfolio_list')
    return render(request, 'portfolio/delete_portfolio.html', {'project': project})

def public_portfolio_list(request):
    projects = PortfolioProject.objects.filter(is_public=True)
    return render(request, 'portfolio/public_portfolio_list.html', {'projects': projects})
