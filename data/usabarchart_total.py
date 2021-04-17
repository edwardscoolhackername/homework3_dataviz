import matplotlib.pyplot as plt 
from functions import medals
import math

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

plt.bar(medals.years, medals.usabronze, color=(255/255, 140/255, 0/255), width=medals.w)
plt.bar(medals.years, medals.usasilver, color=(192/255, 192/255, 192/255), width=medals.w, bottom=medals.usabronze)
plt.bar(medals.years, medals.usagold, color=(255/255, 215/255, 0/255), width=medals.w, bottom=[sum(x) for x in zip(medals.usasilver,medals.usabronze)])

ax.set_xticks(medals.years)
ax.set_xticklabels(medals.years, rotation='vertical')
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)

plt.ylabel("Amount of Medals won by USA")

plt.xlabel("Year")

plt.title("USA's Total Medal Wins in the Winter Olympics", pad="20")

plt.show()