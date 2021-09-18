print("runing")

for i in range(4000000):
    max = int(i ** 0.5 + 1)
    if i%2 != 0:
        for x in range(2, max):
            if i%x == 0:
                break
            if x == max:
                pass #nb premier