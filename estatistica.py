from collections import Counter
from matplotlib import pyplot as plt
from vectors import sum_of_squares
from vectors import dot
import math

num_friends = [100,49,41,50,25, 32, 40, 10, 22, 32, 46, 10, 21, 32, 40, 10, 20]
friends_counts = Counter(num_friends);

xs = range(101)
ys = [friends_counts[x] for x in xs]

plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histograma de amigos")
plt.xlabel("Número de amigos")
plt.ylabel("Número de pessoas")
plt.show()

num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)
sorted_values = sorted(num_friends)

def mean(x):
    return sum(x) / len(x)

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    print("numero amigos: ",num_friends)
    x_bar = mean(x)
    print("media: ",x_bar)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviaton(x):
    return math.sqrt(variance(x))

#não é afetada por uma pequena quantidade de valors discrepantes
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

#como duas variáveis variam em conjunto de suas médias.
#quando os elementos correspondentes de x e y estão acima ou abaixo de suas médias, 
# um número positivo entra na soma. Quanto um está acima e o outro abaixo, um número negativo entra na soma.
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

#A correlation não possui unidade e sempre permanece entre -1 e 1.
#Exemplo: um número como 0,25 representa uma correlação positiva relativamente fraca.
def correlation(x, y):
    stdev_x = standard_deviaton(x)
    stdev_y = standard_deviaton(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0

