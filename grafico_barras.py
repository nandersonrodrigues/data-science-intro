from matplotlib import pyplot as plt

soccer_teams = ["France", "Brazil", "German", "England"]
world_cups = [3, 5, 4, 1]

plt.bar(soccer_teams, world_cups)

plt.title("Word Cup Winners")

plt.show()