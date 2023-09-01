from rest_framework import serializers
from .models import To_do_item

class To_do_item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = To_do_item
        fields = ['date_added', 'item', 'notes', 'lister_id']