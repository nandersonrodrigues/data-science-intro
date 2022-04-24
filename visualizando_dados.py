from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2000.9,  3075.2, 10675.9, 101275.1]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title("GDP nominal")

plt.ylabel("Bilhões de $")
plt.show()