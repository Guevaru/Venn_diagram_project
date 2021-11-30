from matplotlib_venn import venn2,venn2_circles
from matplotlib import pyplot as plt


sciGreats ={
    'Antoine Laurent Lavoisier',
    'Isaac Newton',
    'Galileo Galilei',
    'Marie Curie',
    'Max Planck',
    'Albert Einstein',
    'Stephen Hawking',
    'Charles Darwin',
    'Nikola Tesla',
    'Thomas Edison',
    'Charles Babbage',
    'Leonardo da Vinci',
    'Niels Bohr',
}
nobelLaur={"Patric Maynard Staur Blackett","John Douglas Cockroft", "Alexander Todd", "Niels Bohr"}

newSet = sciGreats.intersection(nobelLaur)
print(newSet)
pass
venn2_circles([nobelLaur,sciGreats])
plt.show()