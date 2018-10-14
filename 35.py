import time

count = 0
while True:
    print("HEllo")
    count += 1
    if count > 3:
        print("END OF THE LINE")
        break
    time.sleep(count)
