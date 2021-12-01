from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt
import portion as intVal

rainbow_colors = {
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Indigo",
    "Violet"
}

primary_colors = {
    "Red",
    "Green",
    "Blue",
    "Yellow"
}

venn2([rainbow_colors, primary_colors],
      set_labels=('Rainbow Colors',
                  'Primary Colors'),
      set_colors=('orange', 'purple'), alpha=0.8)
venn2_circles([rainbow_colors,
              primary_colors])
plt.show()
intList = rainbow_colors.intersection(
    primary_colors)
A = intVal.openclosed(10, 25)
B = intVal.openclosed(20, 50)
C = A.union(B)
D = B.intersection(A)
