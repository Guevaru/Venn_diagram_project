from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt

sciGreats = {'Antoine-Laurent de Lavoisier', 'Isaac Newton',
             'Michael Faraday', 'Humphrey Davy', 'Lord Rayleigh'
             'James Clerk Maxwell', 'John Dalton',
             'Amadeus Avogadro', 'Henri Becquerel',
             'Josiah Willard Gibbs', 'Marie Currie',
             'Robert Goddard', 'Pierre Jolliot',
             'Augustin Louis Cauchy', 'Richard Edler von Mises',
             'Gregorio Ricci-Curbastro ', 'Tullio Levi-Civita',
             'Morton Gurtin', 'Robert Andrews Millikan',
             'Niels Bohr', 'Louis de Broglie', 'Albert Einstein',
             'Wilhelm Röntgen', 'Edmond Nicolas Laguerre',
             'Johann Carl Friedrich Gauss', 'Robert Boyle'
             'Louis Pasteur', 'Pierre-Simon Marquis de Laplace',
             'Giuseppe Luigi Lagrangia', 'Leonhard Euler'
             'John William Strutt Baron Rayleigh'}
nobLaur = {'Henri Becquerel', 'Marie Currie',
           'Takaaki Kajita', 'Pierre Jolliot',
           'Wolfgang Pauli', 'Paul Dirac',
           'Robert Andrews Millikan',
           'Niels Bohr', 'Louis de Broglie', 'Albert Einstein',
           'Wilhelm Röntgen', 'Max Born', 'Jack St. Claire Kilby',
           'Albert Fert', 'Erwin Schrödinger', 'Roger Penrose',
           'John William Strutt Baron Rayleigh', 'Reinhard Genzel',
           'Andrea Ghez', 'James Peebles', 'Didier Queloz',
           'Michel Mayor', 'Donna Strickland', 'Gérard Mourou'}
venn2([nobLaur, sciGreats],
      set_labels=('Nobel Laureates', 'Great Scientists'),
      set_colors=('yellow', 'red'), alpha=0.8)
venn2_circles([nobLaur, sciGreats])
plt.show()
intList = sciGreats.intersection(nobLaur)
pass
