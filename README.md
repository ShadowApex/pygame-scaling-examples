# Pygame Scaling Examples

## Native Scaling
Native scaling is a technique where sprites are blit to a native surface, then
scaled to fit the size of the screen.

![](native_scaling.gif)

### Benchmarks
```
$ ./native_scaling.py 
Average FPS: 229.222196069
Average FPS: 233.239866955
Average FPS: 239.072807992
Average FPS: 224.080845295
Average FPS: 234.77412611
Average FPS: 228.427977005
Average FPS: 234.813734602
Average FPS: 249.675982787
```

## Hybrid Scaling
Hybrid scaling is a technique where some surfaces are scaled to size prior to
blitting to the screen.

![](hybrid_scaling.gif)

### Benchmarks
```
$ ./hybrid_scaling.py 
Average FPS: 249.514134775
Average FPS: 384.03632468
Average FPS: 446.630069846
Average FPS: 481.477064378
Average FPS: 381.196040087
Average FPS: 426.344636521
Average FPS: 363.718988098
Average FPS: 402.93177176
```

