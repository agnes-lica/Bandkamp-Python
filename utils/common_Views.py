from rest_framework.views import APIView, Request, Response, status

class PostCommonView(APIView):
  def post(self, request: Request)-> Response:
    
    serializer = self.view_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    serializer.save()
    
    return Response(serializer.data, status.HTTP_201_CREATED)
  
class GetCommonView(APIView):
  def get(self, request: Request)-> Response:
    
    queryset=self.view_queryset.all()
    serializer=self.view_serializer(queryset, many=True)
    
    return Response(serializer.data, status.HTTP_200_OK)
    