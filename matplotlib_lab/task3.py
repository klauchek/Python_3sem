import matplotlib.pyplot as plt
import collections
import csv

preps = collections.defaultdict(list)
groups = collections.defaultdict(list)

with open('students.csv', mode='r') as infile:
    reader = csv.reader(infile, delimiter=';')
    rows = [i for i in reader]

for row in rows:
    preps[row[0]].append(int(row[2]))
    groups[row[1]].append(int(row[2]))

for key in preps:
    prep_marks = [0] * 8
    for i in range(3, 11):
        prep_marks[i - 3] = preps[key].count(i)
    preps[key] = prep_marks

for key in groups:
    group_marks = [0] * 8
    for i in range(3, 11):
        group_marks[i - 3] = groups[key].count(i)
    groups[key] = group_marks

width = 0.35
fig, ax = plt.subplots(2, 1)
prep_labels = list(preps.keys())
group_labels = list(groups.keys())

for i in range(3, 11):
    upper_preps = [preps[key][i - 3] for key in preps]
    lower_preps = [sum(preps[key][j - 3] for j in range(3, i)) for key in preps]
    upper_groups = [groups[key][i - 3] for key in groups]
    lower_groups = [sum(groups[key][j - 3] for j in range(3, i)) for key in groups]
    ax[0].bar(list(preps.keys()), upper_preps, width, bottom=lower_preps, label='%d' % i)
    ax[1].bar(list(groups.keys()), upper_groups, width, bottom=lower_groups, label='%d' % i)

plt.subplots_adjust(wspace=0.3, hspace=0.4)
ax[0].legend(loc='upper right',  bbox_to_anchor=(1.1, 1.1), fontsize=8)
ax[1].legend(loc='upper right',  bbox_to_anchor=(1.1, 1.1), fontsize=8)
ax[0].set_ylabel('Number of marks')
ax[1].set_ylabel('Number of marks')
ax[0].set_title('Marks per prep')
ax[1].set_title('Marks per group')

plt.savefig("marks.png")
plt.show()
