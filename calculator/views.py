from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe_view(request, recipe_name):
    """Отображает рецепт. Поддерживает ?servings=N для умножения порций."""
    recipe = DATA.get(recipe_name)

    if recipe is None:
        return HttpResponse('Рецепт не найден', status=404)

    servings_raw = request.GET.get('servings', 1)
    try:
        servings = int(servings_raw)
        if servings <= 0:
            servings = 1
    except (ValueError, TypeError):
        servings = 1

    scaled_recipe = {
        ingredient: amount * servings
        for ingredient, amount in recipe.items()
    }

    context = {
        'recipe': scaled_recipe
    }
    return render(request, 'calculator/index.html', context)
