"""
Island with single lowland cell, first herbivores only, later carnivores.
"""


__author__ = 'Hans Ekkehard Plesser, NMBU'


import textwrap
from biosim.simulation import BioSim

geogr = """\
           WWW
           WLW
           WWW"""
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

for seed in range(99, 100):
    sim = BioSim(island_map=geogr,
                 ini_pop=ini_herbs,
                 seed=seed,
                 img_dir='results',
                 img_base=f'mono_ho_{seed:05d}',
                 img_years=300)
    liste_pop = ini_herbs[0]["pop"]
    loc = ini_herbs[0]["loc"]

    sim.simulate(100)
    sim.add_population(ini_carns)
    sim.simulate(100)

    for i in sim.cells:
        try:
            print(f"Loc: {i}, N animals: {len(sim.cells[i].herbivore)}, Habitable: {sim.cells[i].habitable}, Fodder: {sim.cells[i].fodder}")
        except TypeError:
            print(i, sim.cells[i].fodder, sim.cells[i].habitable, sim.cells[i].animals)


