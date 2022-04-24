from collections import Counter
from matplotlib import pyplot as plt

grades = [10, 20, 40, 10, 50, 50, 89, 90, 20, 60]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x - 4 for x in histogram.keys()],
        histogram.values(),
        8)

plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])

plt.show()