import threading
import time

from signals_app.models import TestModel

print("Main Thread ID:", threading.get_ident())

start_time = time.time()

obj = TestModel.objects.create(name="Vardhan")

end_time = time.time()

print("Time Taken:", end_time - start_time)
print("Object Created")