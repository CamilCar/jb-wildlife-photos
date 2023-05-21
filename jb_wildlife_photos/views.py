from django.shortcuts import render

# Renders a 404 page


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)