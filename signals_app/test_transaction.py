from django.db import transaction
from signals_app.models import TestModel

try:
    with transaction.atomic():
        TestModel.objects.create(name="Transaction Test")
except Exception as e:
    print("Exception:", e)

count = TestModel.objects.filter(name="Transaction Test").count()
print("Records Found:", count)