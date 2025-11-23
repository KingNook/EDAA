# EL PLAN: EDAA

So the plan is basically to do a sort of analysis on decay rates, with a specific focus on the effects of various smoothing algorithms on the goodness of fit (and potentially a brief note at the end on clustering of profiles; I'm not expecting much out of the clustering inspection though due to the variety of rooms that were measured).

## Pre-Processing

I would like to use the unbinned data for this project as that gives me access to roughly 1-minutely resolution. The downside to this is that the readings are not evenly on the minute, and are instead scattered at 1 minute $\pm$ some number of seconds.

Workarounds for this that I can think of include:

**Snapping readings to the nearest minute -- PLANNING TO USE THIS**
I'm hoping there's an easy way to do this with pandas by reindexing and using the nearest setting somehow.

*Update: 22/11* Can literally just use `pandas.Series.dt.round(freq='min')` to do this -- I will try both methods but I suspect this will be a lot simpler, especially since I don't think most dates are more than 10 seconds away from the nearest minute (although will have to confirm this properly in the report)

**Taking the offsets into account during smoothing**
I could apply a kernel at each minute, then the offsets would be taken into account in the weighting from the kernel. This (I think) has issues since there won't be a point at the centre of the kernel so might cause issues with values being significantly less than they should?

I also think it would be good to normalise all profiles by their maximum (initial) values, so that they can be more directly compared.

---

I will then also have to pick out the timeframes for which we see decay -- I am planning on doing this manually, although if I find a better way, I will almost certainly switch to that.

## Processing

Would want to fit exponential decay curves. Write out hypothesis that decay rate is proportional to difference between current concentration and background (in absence of external sources) and thus would be expected to be an exponential decay curve. Then possibly fit via MSE, minimise and display. Possibly also include something to do with uncertainty, eg fit a gaussian to the length scale to try to cover all values, can potentially also try GMM or similar on length scales to get an idea of groups of time scales of decay.

Could also normalise by total decrease to steady state (since steady state carbon conc might not be the same across profiles)

**smoothing?**

we could try smoothing first for the sake of it? i suspect that it is not a good idea to process the data too much before fitting curves. still, it might be worth trying it out to see how much (if any) of an effect it has on the fitted curves. As for *how* I would go about smoothing, I would like to try the gaussian stuff I saw in Daniel Chen's CMP presentation, so potentially try to apply that using `.rolling()`? It's just that I am distinctly aware that performance might be a bit of an issue.

## Analysis

Obviously dependent on final data, but either talk about groupings of decay time scales or the lack thereof -- groupings may indicate specific rooms, or whether or not the window was open, while lack of might suggest that the different rooms may play more of an impact, thus resulting in a wider spread.

# Notes on data

## columns
> "Location ID","Location Name","Location Group","Location Type","Sensor ID","Local Date/Time","UTC Date/Time","Channel","PM2.5 (μg/m³) raw","0.3um particle count","CO2 (ppm) raw","Temperature (°C) raw","Humidity (%) raw","TVOC (ppb)","TVOC index","NOX index","PM1 (μg/m³)","PM10 (μg/m³)","TVOC raw log(R)","NOX raw log(R)","measure0","measure1","measure2","measure3","measure4","measure5","measure6","measure7","measure8","measure9","measure10","measure11","measure12","measure13","measure14","measure15","measure16","measure17","measure18","measure19"

Of these, the ones of interest (to me, personally) would likely be: 

- Location Name
- Local Date/Time
- UTC Date/Time

then possibly anything we want to consider decay rates of. For now, that list is:

- CO2 (ppm) raw

Note that realistically speaking, we can make do with literally just:

- UTC Date/Time
- CO2 (ppm) raw

where we have used UTC Date/Time instead of Local Date/Time since the clocks changed at some point during the data collection so this ensures some amount of consistency across data.