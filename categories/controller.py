
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer

class CategoryListCreateDelete(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

  def delete(self, request, *args, **kwargs):
    parent_id = request.query_params.get('parent_id', None)
    
    if parent_id:
      # Get all descendants recursively
      def get_descendants(id):
        children = Category.objects.filter(parent=id)
        descendant_ids = list(children.values_list('id', flat=True))
        
        for child in children:
          descendant_ids.extend(get_descendants(child.id))
        
        return descendant_ids

      # Delete all descendants
      descendants = get_descendants(parent_id)
      Category.objects.filter(id__in=descendants).delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
