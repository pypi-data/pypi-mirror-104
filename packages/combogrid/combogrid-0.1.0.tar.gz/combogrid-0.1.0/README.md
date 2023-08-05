# combogrid

**combogrid** makes it easier to draw combo charts in a grid, using matplotlib

Combo charts are useful for comparing two different 'y' variables.
Grids of charts (aka 'facet grids') are useful for comparing data
between groups.

Perhaps you want to see how a single stock's price and volume changed day by day.
And you are following multiple stocks, so you want one chart per stock.

## Requirements
* python 3.71 or above
* pandas

## Install
```bash
pip install combogrid
```

## Help
```python
import combogrid
help(combogrid.plot)
```


## Use
```python
import pandas as pd
import combogrid
df = pd.read_csv("sample.csv")
df["date"] = pd.to_datetime(df["date"])
plt = combogrid.plot(df, "date", "volume", "price", "color")
plt.show()
```

## Output
![Sample image with a grid of combo charts](https://raw.githubusercontent.com/rahimnathwani/combogrid/main/sample.png)
