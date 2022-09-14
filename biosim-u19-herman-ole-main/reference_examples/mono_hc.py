"""
Island with single lowland cell, first herbivores only, later carnivores.
"""

# noinspection SpellCheckingInspection
__author__ = 'Hans Ekkehard Plesser, NMBU'


import textwrap
from biosim.simulation import BioSim

geogr = """\
           WWWWW
           WLLLW
           WLLLW
           WWWWW
           WWWWW"""
geogr = textwrap.dedent(geogr)

ini_herbs = [{'loc': (2, 2),
              'pop': [{'species': 'Herbivore',
                       'age': 5,
                       'weight': 20}
                      for _ in range(50)]}]
ini_carns = [{'loc': (2, 2),
              'pop': [{'species': 'Carnivore',
                       'age': 5,
                       'weight': 20}
                      for _ in range(20)]}]

for seed in range(10, 11):
    sim = BioSim(geogr, ini_herbs, seed=seed, img_base=f'mono_hc_{seed:05d}', img_years=300, vis_years=2)

    sim.simulate(20)
    sim.add_population(ini_carns)
    sim.simulate(20)


