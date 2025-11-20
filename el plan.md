# EL PLAN: EDAA

So the plan is basically to do a sort of analysis on decay rates, with a specific focus on the effects of various smoothing algorithms on the goodness of fit (and potentially a brief note at the end on clustering of profiles; I'm not expecting much out of the clustering inspection though due to the variety of rooms that were measured).

## Pre-Processing

I would like to use the unbinned data for this project as that gives me access to roughly 1-minutely resolution. The downside to this is that the readings are not evenly on the minute, and are instead scattered at 1 minute $\pm$ some number of seconds.

Workarounds for this that I can think of include:

**Snapping readings to the nearest minute**
I'm hoping there's an easy way to do this with pandas by reindexing and using the nearest setting somehow

**Taking the offsets into account during smoothing**
I could apply a kernel at each minute, then the offsets would be taken into account in the weighting from the kernel. This (I think) has issues since there won't be a point at the centre of the kernel so might cause issues with values being significantly less than they should?

I also think it would be good to normalise all profiles by their maximum (initial) values, so that they can be more directly compared.

## Processing

Would want to fit exponential decay curves. Write out hypothesis that decay rate is proportional to difference between current concentration and background (in absence of external sources) and thus would be expected to be an exponential decay curve. Then possibly fit via MSE, minimise and display. Possibly also include something to do with uncertainty, eg fit a gaussian to the length scale to try to cover all values, can potentially also try GMM or similar on length scales to get an idea of groups of time scales of decay.

Could also normalise by total decrease to steady state (since steady state carbon conc might not be the same across profiles)

## Analysis

Obviously dependent on final data, but either talk about groupings of decay time scales or the lack thereof -- groupings may indicate specific rooms, or whether or not the window was open, while lack of might suggest that the different rooms may play more of an impact, thus resulting in a wider spread.