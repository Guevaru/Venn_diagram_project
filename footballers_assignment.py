from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt
import portion as intVal

great_nigerian_footballers = {
    "Kanu Nwankwo",
    "Austin Jay-Jay Okocha",
    "Sunday Oliseh",
    "Rashidi Yekini",
    "Segun Odegbami",
    "Stephen Keshi",
    "Emmanuel Amunike",
    "Finidi George",
    "Christian Chukwu",
    "Mudashiru Babatunde"
}

nigerian_players_who_have_won_afcon = {
    "Odion Ighalo",
    "Stephen Keshi",
    "Emmanuel Emenike",
    "Segun Odegbami",
    "Peter Odemwingie",
    "Christian Chuckwu",
    "Rashidi Yekini",
}

venn2([great_nigerian_footballers, nigerian_players_who_have_won_afcon],
      set_labels=('Great Nigerian Footballers',
                  'Nigerain Players Who Have Won AFCON'),
      set_colors=('blue', 'purple'), alpha=0.8)
venn2_circles([great_nigerian_footballers,
              nigerian_players_who_have_won_afcon])
plt.show()
intList = great_nigerian_footballers.intersection(
    nigerian_players_who_have_won_afcon)
A = intVal.openclosed(10, 25)
B = intVal.openclosed(20, 50)
C = A.union(B)
D = B.intersection(A)
