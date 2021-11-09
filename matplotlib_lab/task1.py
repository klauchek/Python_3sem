import matplotlib.pyplot as plt

def visualize(n, x, y, file_name):
    plt.scatter(x, y)
    plt.xlabel('x coordinate')
    plt.ylabel('y coordinate')

    plt.title(file_name + ': Number of points: %d' % n)
    plt.show()

def read_from_file(file_name):
    coord_x = []
    coord_y = []
    with open(file_name, 'r') as file:
        n = int(file.readline())
        for i in range(n):
            line = [float(i) for i in file.readline().split()]
            coord_x.append(line[0])
            coord_y.append(line[1])
    visualize(n, coord_x, coord_y, file_name)


if __name__ == "__main__":
    files = ['001.dat', '002.dat', '003.dat', '004.dat', '005.dat']
    for file_name in files:
        read_from_file('data_1tsk/' + file_name)
