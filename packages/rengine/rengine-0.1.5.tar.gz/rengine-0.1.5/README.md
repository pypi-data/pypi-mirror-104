## About this package

Collaborative Filtering is a method that is often used as a recommendation engine. Many industries have used this algorithm to recommend their products, this library can use cosine similarity or even centered cosine similarity.

### Depedencies
* Python >= 3
* numpy

### How to use
* cos_similarity(var1, var2, centered)

### Parameters
**var1** : iterable, array, np.array

> The single arrray value you want to compare

**var2** : iterable, array, np.array

> The multi arrray values, you can convert from dataframe or table on your database

**centered** : bool

> By default it will give true, if true you will use centered cosine similarity
### Example case
* We'll try to figuring out this single matrix value, on the multi array
> [4,  0,  0,  5,  1,  0,  0]
* The example dataset that we had
> [[5,  5,  4,  0,  0,  0,  0],  
    [0,  0,  0,  2,  4,  5,  0],  
    [0,  3,  0,  0,  0,  0,  3]]
### Example of code
```
from rengine.method import CollaborativeFiltering
import numpy as np
clf =  CollaborativeFiltering()
print(clf.cos_similarity(np.array([5,  4,  0,  0]),  [[1,  0,  3,  2],  [2,  1,  1,  0],  [4,  5,  0,  1]]))
```

## Example of output
```
[-0.5, 0.866, -0.24] #row 2 in multi array data has more similarity
```

## Another of output
```
[0.092, -0.559, nan] #nan means there's a number divided by zero
```