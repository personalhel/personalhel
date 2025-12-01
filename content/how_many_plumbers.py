# imports:
import numpy as np

# def constants:
n_world_pop = 8.26*10**9 # [people]
n_usa_pop = 3.25*10**8 # [people]
n_usa_Pb = 4.81*10**5 # [people]

# global  plumber density:
rho_Pb = (n_world_pop / n_usa_pop) * n_usa_Pb # [people]
print(f"estimated total amount of global plumbers: {rho_Pb:.2e}")

# our estimate for f_Pb:
r_Pb = 2.0 / np.sqrt( 2.0 * np.pi)
print(f"estimated ratio of planets with inteligent life that has plumbing: {r_Pb:.2e}")

# putting it all together:
n_stars = 10**11 # assuming 100 billion stars
f_p = 1.0
n_e = 4.0
f_l = 1.0

n_Pb_tot = n_stars * f_p * n_e * f_l * rho_Pb * r_Pb # [people] 
print(f"estimated total amout of plumbers in the galaxy: {n_Pb_tot:.1e}")
