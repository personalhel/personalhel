asked by kristian wichmann on [[bluesky]]: https://bsky.app/profile/kwichmann.bsky.social/post/3m6x2uonwn22d
![[Pasted image 20251201200745.png]]

numerical calculations will be shown below.
# starting assumptions
in order to give an estimation of the amount of plumbers there are in the milky way, we will have to make some starting assumptions:
- we are not referring to the chocolate bar but our galaxy
- we define plumbing as the work relating pipes and fluid transportation in a systematic way. therefore, people coding using the [[pipe operator]], `|>`, will not be counted.
- only human plumbers are counted on earth. the alien situation, we will look at later.

# calculations
## earth estimate
"in 2020, there were around 481,472 American citizens employed in the plumbing industry"[^1]. therefore, we get: $n_{usa,Pb} = 4.81\cdot 10^5$ people.

assuming the american population is about $325$ mio. and further assuming uniform global plumber distribution in the $8.26$ billion population[^2], we get a plumber density:
$$ 
\rho_{Pb} 
=  
\left[ \frac{n_{world,pop}}{n_{usa,pop}}\right]\cdot n_{usa,Pb}
$$
inserting the numbers, we get $12.2$ million plumbers globally.

one answer would be to assume we are alone in the galaxy with no non-earth plumbers and therefore having an answer of $12.2$ million, but this is boring and goes against the [[copernican principle]], so we will continue.

## galaxy-level calculations
he [[drake equation]] is[^3]: 
$$
{N=R_{*}\cdot f_{\mathrm {p} }\cdot n_{\mathrm {e} }\cdot f_{\mathrm {l} }\cdot f_{\mathrm {i} }\cdot f_{\mathrm {c} }\cdot L}
$$
the variables are described as:
- $N$: number of civilizations in our galaxy for which communication might be possible.
- $R_*$: average rate of star formation
- $f_P$: average number of those stars with planets
- $n_e$: the average number of planets that can potentially support life per start with planets
- $f_{\mathrm {l}}$: fraction of planets that could support life that actually develop life at some point
- $f_{\mathrm {i}}$: fraction of planets with life that develop into intelligent life
- $f_{\mathrm {C}}$: fraction of civilizations that develop a technology that releases a detectable sign of their existence into space
- $L$: length of time for which such civilizations release those detectable signals

the main problem with this is that we would equate having plumbers to being able to be seen from space at a great distance. modern large-scale radio systems are a relatively new thing, and plumbing as a profession dates back to ancient times. while you could have made such signals by burning giant areas of forest or fields in ancient times, i don't think this is a very useful metric to use. we are also not interested in some cumulative total in the future, but the total of current plumbers in the galaxy. but the current estimates according to the [[wikipedia]] article[^4] for the different factors are:
- $R_*$: 1.5-3 stars / year. let's take the average of that; 2.25 stars / year
- $f_P$: around 1
- $n_e$: sounds like 3-5. we will say 4.
- $f_{\mathrm {l}}$: it seems like this is highly debated if the value is around 1, but let's use 1.
- $f_{\mathrm {i}}$: yet again, no one seems to agree, but some argue it is close to 1, so we set it to 1.
- $f_{\mathrm {C}}$: yet again again, no one seems to agree, because it could be 1 and 0.
- $L$: 420 years estimated

thankfully, we can eliminate a lot of those factors, and simplify:
$$
n_{Pb,tot} 
= 
n_{stars} 
\cdot f_P 
\cdot n_e 
\cdot f_l
\cdot \rho_{Pb}
$$
this should give an okay estimate of the total plumbers by taking number of stars with intelligent life, since we assume every instance of intelligent life will develop plumbing. however, this assumes all possible of those instances currently have intelligent life also has plumbing. therefore we need to add a factor that takes the amount of time it takes for intelligent life to develop plumbing into account. this differs from $L$ in the above calculation.

let's make $r_{Pb}$ as the ratio of current plumbing having planets to planets with intelligent life:
$$n_{Pb,tot} 
= 
n_{stars} 
\cdot f_P 
\cdot n_e 
\cdot f_l
\cdot \rho_{Pb}
\cdot r_{Pb}
$$
## estimating $r_{Pb}$
there are a couple different ways of estimating the frequency of those planets with intelligent life that currently have plumbers. 

we can start about by assuming that the distribution of plumbing creation follows a [[normal distribution]] over time, meaning most of the plumbing planet systems will be located at around the same time. by using the copernican principle again and the fact that we seem to currently have plumbing, it is likely that we are around such a peak right now. but then how many? let's define the normal distribution as having the following property (like any other well-defined distribution)[^5]:

$$
\int_{-\infty}^{\infty} f_{Pb}(t) \text{d}t = 1
$$
we know that the solution is:
$$
f_{Pb}(t) = \frac{1}{\sigma\sqrt{2\pi}}\cdot \exp\left[ -\frac{(t-\mu)^2}{2\sigma^2} \right]
$$
the peak value must be at $t=\mu$. so we get:
$$
f_{Pb} = \frac{1}{\sigma \sqrt{2\pi}}
$$
now we only need to find a way to estimate $\sigma$, and again using/abusing our powerful copernican principle, we can assume it would be close to the earth value, so saying $\sigma = 5000$ years is probably not bad compared to other estimates used in the above, since plumbing is around that age.
$$
f_{Pb} = \frac{1}{\sigma \sqrt{2\pi}} = \frac{1}{(5000 \text{ years})\sqrt{2\pi}}
$$

this value is around $8.8\cdot 10^{-5} \; \text{year}^-1$ of the frequency. but we need the instant ratio, $r_{Pb}$, so we need the lifespan of plumbing for a world. this is going to be hard to do, but since, we have already set $\sigma = 5000 \text{ years}$, let's define $t_{Pb}=2\sigma$.

therefore, we get:
$$
r_{Pb} = f_{Pb}\cdot t_{Pb} = \frac{2}{\sqrt{2\pi}} = 0.798 
$$
this is a nice dimensionless number as we want, and as it turns out by setting the time with plumbing as a constant multiple of $\sigma$ we don't even have to have a value for $\sigma$, since the information is encoded in the constant multiple instead.

# putting it all together
assuming we have around 100 billion stars in the galaxy, we can now multiply it all together:
$$
n_{Pb,tot} 
= 
n_{stars} 
\cdot f_P 
\cdot n_e 
\cdot f_l
\cdot \rho_{Pb}
\cdot r_{Pb} 
=
10^{11} \cdot
1 \cdot
4 \cdot
1 \cdot
1.22\cdot 10^7 \cdot 
0.798
= 8 \cdot 10^{18} 
$$

# conclusion
there should be around $8\cdot 10^{18}$ plumbers in the galaxy, assuming you are okay with abusing copernicus and drake enough.

# code used
```python
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
```

[^1]: source: https://www.bookcleango.com/blog/plumbing-statistics

[^2]: source: https://www.worldometers.info/world-population/

[^3]: source: https://en.wikipedia.org/wiki/Drake_equation#Equation

[^4]: source: https://en.wikipedia.org/wiki/Drake_equation#Current_estimates

[^5]: source: https://en.wikipedia.org/wiki/Normal_distribution