from django.shortcuts import render
from rest_framework.views import APIView
from .models import To_do_item
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import To_do_item_Serializer
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from listers_app.models import Lister
from listers_app.serializers import ListerSerializer

class All_to_do_items(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        answer = {"to_do_items": []}
        for items in To_do_item.objects.filter(lister_id_id=request.user.id):
            print(items)
            answer["to_do_items"].append({"id": items.id,
                                          "entry": {
                                              "date_added": items.date_added,
                                              "item": items.item,
                                              "notes": items.notes,
                                              "complete": items.done
                                          }
                                          })
        return Response(answer)

    def post(self, request):
        item = request.data["item"]
        notes = request.data["notes"]
        lister_id = request.user.id
        new_to_do_item = To_do_item(item=item, notes=notes, lister_id_id=lister_id)
        print(request.data)
        new_to_do_item.full_clean()
        new_to_do_item.save()
        return Response(request.data, status=HTTP_201_CREATED)
    
class Single_item(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        item = To_do_item.objects.get(id=id)
        print(request.data.keys())
        print('complete' in request.data.keys())
        if "item" in request.data.keys():
            print("IF WORKED")
            item.item = request.data.get("item")
            item.save()
        if "notes" in request.data.keys():
            item.notes = request.data.get("notes")
            item.save()
        if "complete" in request.data.keys():
            item.done = request.data.get("complete")
            item.save()
        return Response(item)

    def delete(self, request, id):
        try:
            item = To_do_item.objects.get(id=id)
            item.delete()
        except:
            return Response("ITEM NOT FOUND", status=HTTP_404_NOT_FOUND)
        return Response("ITEM REMOVED", status=HTTP_204_NO_CONTENT)
