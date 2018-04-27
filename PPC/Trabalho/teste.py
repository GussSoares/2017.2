import time

initial = time.time()
time.sleep(5)
final = time.time()
print("the now time is " + str(int(final) - int(initial)))