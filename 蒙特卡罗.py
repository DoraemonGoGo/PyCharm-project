import numpy as np
import datetime

n = 1 ** 6
counter = 0
length = 10000
steps = int(n / length)

startTime = datetime.datetime.now()
for i in range(steps):
    p = np.random.uniform(-1, 1, (length, 2))
    r = p[:, 0] ** 2 + p[:, 1] ** 2
    counter += np.sum(r <= 1)
    endTime = datetime.datetime.now()
    print('Running time = ', endTime - startTime)
    answer = 4.0 * counter / n
    print('Numerical solution of PI = ', answer)
