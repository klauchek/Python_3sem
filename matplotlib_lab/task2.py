
import matplotlib.pyplot as plt

coord_x = []
coord_y = []
with open('data2.txt') as file:
    frames = int(sum(1 for line in file)/2)

fig, axes = plt.subplots(int(frames / 2), 2, sharex='all', sharey='all')
plt.subplots_adjust(wspace=0.3, hspace=0.4)
fig.set_figheight(9)
fig.set_figwidth(8)
plot_places1 = [0, 0, 1, 1, 2, 2]
plot_places2 = [0, 1, 0, 1, 0, 1]


file = open("data2.txt", "r")
for i, j, k in zip(range(frames), plot_places1, plot_places2):
    coord_x.append([float(s) for s in file.readline().split()])
    coord_y.append([float(s) for s in file.readline().split()])
    axes[j][k].plot(coord_x[i], coord_y[i])
    axes[j][k].set_title("Frame %d" % i)
    axes[j][k].set_xlim(left=0, right=max(coord_x[i]))
    axes[j][k].set_ylim(bottom=min(coord_y[i]) - 1.2, top=max(coord_y[i]) + 1.2)
    axes[j][k].xaxis.set_ticks_position("bottom")
    axes[j][k].yaxis.set_ticks_position("left")
    axes[j][k].grid()

plt.show()
plt.savefig("task2.png")


