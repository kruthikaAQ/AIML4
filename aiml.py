import pandas as pd
import numpy as np
series_A=pd.Series([10,20,30,40,50])
series_b=pd.Series([40,50,60,70,80])
union=pd.Series(np.union1d(series_A,series_b))
intersect=pd.Series(np.intersect1d(series_A,series_b))
notcommonseries=union[-union.isin(intersect)]
print(notcommonseries)
print('largest number in series_a is:',series_A.max())
print('smallest number in series_a is:',series_A.min())
print('the sum of series_b is:',series_b.sum())
print('the average of series_a is:',series_A.mean())
print('the median of series_b is:',series_b.median())
