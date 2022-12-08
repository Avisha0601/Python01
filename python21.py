import matplotlib.pyplot as plt

activities = ['study','reading','sports','eating']
slices = [3, 7, 8, 6]
colors = ['aqua', 'teal', 'beige','purple']

plt.pie(slices, labels = activities, colors=colors,
        startangle=30, shadow= False, explode = (0, 0, 0, 0),
        radius = 1.2, autopct = '%3.3f%%')

plt.legend()
plt.show()

