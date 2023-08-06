# Time Series Feature Engineering
> Time series feature generator.


## Install

`pip install timeseries_feature_engineering`

## How to use

### Add Date Parts

```python
df = pd.DataFrame({'date': ['2019-12-04', None, '2019-11-15', '2019-10-24']})
df = add_datepart(df, 'date')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Month</th>
      <th>Week</th>
      <th>Day</th>
      <th>Dayofweek</th>
      <th>Dayofyear</th>
      <th>Is_month_end</th>
      <th>Is_month_start</th>
      <th>Is_quarter_end</th>
      <th>Is_quarter_start</th>
      <th>Is_year_end</th>
      <th>Is_year_start</th>
      <th>Elapsed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2019.0</td>
      <td>12.0</td>
      <td>49.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>338.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>1575417600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2019.0</td>
      <td>11.0</td>
      <td>46.0</td>
      <td>15.0</td>
      <td>4.0</td>
      <td>319.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>1573776000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2019.0</td>
      <td>10.0</td>
      <td>43.0</td>
      <td>24.0</td>
      <td>3.0</td>
      <td>297.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>1571875200</td>
    </tr>
  </tbody>
</table>
</div>



### Add Moving Average Features

With weighted average. 
> Recency in an important factor in a time series. Values closer to the current date would hold more information.

```python
df = pd.DataFrame({
    'date': pd.date_range('2019-12-01', '2019-12-10'), 
    'sales': np.random.randint(100, 500, size=10)
})
df = add_moving_average_features(df, 'sales', windows=[3,5], weighted=True)
df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>sales</th>
      <th>sales_3p_MA</th>
      <th>sales_5p_MA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2019-12-01</td>
      <td>155</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2019-12-02</td>
      <td>437</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2019-12-03</td>
      <td>361</td>
      <td>352.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2019-12-04</td>
      <td>356</td>
      <td>371.166667</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2019-12-05</td>
      <td>490</td>
      <td>423.833333</td>
      <td>399.066667</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2019-12-06</td>
      <td>222</td>
      <td>333.666667</td>
      <td>353.133333</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2019-12-07</td>
      <td>197</td>
      <td>254.166667</td>
      <td>294.400000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2019-12-08</td>
      <td>390</td>
      <td>297.666667</td>
      <td>316.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2019-12-09</td>
      <td>159</td>
      <td>242.333333</td>
      <td>258.666667</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2019-12-10</td>
      <td>470</td>
      <td>353.000000</td>
      <td>318.133333</td>
    </tr>
  </tbody>
</table>
</div>



Without weighted average.

```python
df = pd.DataFrame({
    'date': pd.date_range('2019-12-01', '2019-12-10'), 
    'sales': np.random.randint(100, 500, size=10)
})
df = add_moving_average_features(df, 'sales', windows=[3,5], weighted=True)
df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>sales</th>
      <th>sales_3p_MA</th>
      <th>sales_5p_MA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2019-12-01</td>
      <td>167</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2019-12-02</td>
      <td>458</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2019-12-03</td>
      <td>260</td>
      <td>310.500000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2019-12-04</td>
      <td>174</td>
      <td>250.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2019-12-05</td>
      <td>392</td>
      <td>297.333333</td>
      <td>301.266667</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2019-12-06</td>
      <td>401</td>
      <td>360.166667</td>
      <td>338.200000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2019-12-07</td>
      <td>460</td>
      <td>429.000000</td>
      <td>379.200000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2019-12-08</td>
      <td>381</td>
      <td>410.666667</td>
      <td>393.733333</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2019-12-09</td>
      <td>349</td>
      <td>378.166667</td>
      <td>389.533333</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2019-12-10</td>
      <td>365</td>
      <td>362.333333</td>
      <td>379.000000</td>
    </tr>
  </tbody>
</table>
</div>



### Add Expanding Features

```python
df = pd.DataFrame({
    'date': pd.date_range('2019-12-01', '2019-12-10'), 
    'sales': np.random.randint(100, 500, size=10)
})
df = add_expanding_features(df, 'sales', period=3)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>sales</th>
      <th>sales_3p_expanding</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2019-12-01</td>
      <td>178</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2019-12-02</td>
      <td>398</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2019-12-03</td>
      <td>399</td>
      <td>325.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2019-12-04</td>
      <td>385</td>
      <td>340.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2019-12-05</td>
      <td>136</td>
      <td>299.2</td>
    </tr>
  </tbody>
</table>
</div>



### Add Trend Features

```python
df = pd.DataFrame({
    'date': pd.date_range('2019-12-01', '2019-12-10'), 
    'sales': np.random.randint(100, 500, size=10)
})
df = add_trend_features(df, 'sales', windows=[3,7])
df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>sales</th>
      <th>sales_3p_trend</th>
      <th>sales_7p_trend</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2019-12-01</td>
      <td>237</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2019-12-02</td>
      <td>388</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2019-12-03</td>
      <td>384</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2019-12-04</td>
      <td>498</td>
      <td>87.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2019-12-05</td>
      <td>275</td>
      <td>-37.666667</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2019-12-06</td>
      <td>382</td>
      <td>-0.666667</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2019-12-07</td>
      <td>132</td>
      <td>-122.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2019-12-08</td>
      <td>337</td>
      <td>20.666667</td>
      <td>14.285714</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2019-12-09</td>
      <td>496</td>
      <td>38.000000</td>
      <td>15.428571</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2019-12-10</td>
      <td>216</td>
      <td>28.000000</td>
      <td>-24.000000</td>
    </tr>
  </tbody>
</table>
</div>


