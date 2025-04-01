from django.shortcuts import render

# Template View
def categoriesView(request):
  return render(request, 'categories/index.html')