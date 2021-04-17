import matplotlib.pyplot as plt 
from functions import medals
import math

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

plt.bar(medals.years, medals.gold, color=(255/255, 215/255, 0/255), width=medals.w)

ax.set_xticks(medals.years)
ax.set_xticklabels(medals.years, rotation='vertical')
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)

plt.ylabel("Amount of Gold Medals won by Canada")

plt.xlabel("Year")

plt.title("Canada's Gold Medal Wins in the Winter Olympics", pad="20")

plt.show()