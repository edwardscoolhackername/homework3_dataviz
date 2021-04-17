import matplotlib.pyplot as plt 
from functions import medals

values = [315, 203, 107]
labels = ["315", "203", "107"]
colors = [(255/255, 215/255, 0/255), (192/255, 192/255, 192/255), (255/255, 140/255, 0/255)]

plt.pie(values, labels=labels, colors=colors)

plt.title("Canada's Total Medal Wins in the Winter Olympics", pad="20")
plt.show()