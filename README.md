# Pygame Scaling Examples

## Native Scaling
Native scaling is a technique where sprites are blit to a native surface, then
scaled to fit the size of the screen.

![](native_scaling.gif)

### Benchmarks
```
$ ./native_scaling.py 
Average FPS: 213.291753637
Average FPS: 342.199617594
Average FPS: 363.93606507
Average FPS: 318.312560733
Average FPS: 317.297608328
Average FPS: 306.18634003
Average FPS: 329.476714484
Average FPS: 328.060622111
```

## Hybrid Scaling
Hybrid scaling is a technique where some surfaces are scaled to size prior to
blitting to the screen.

![](hybrid_scaling.gif)

### Benchmarks
```
$ ./hybrid_scaling.py 
Average FPS: 252.065698454
Average FPS: 388.64804621
Average FPS: 446.700395339
Average FPS: 423.494425859
Average FPS: 403.478041847
Average FPS: 416.921969876
Average FPS: 492.048411152
Average FPS: 568.612992995
```

