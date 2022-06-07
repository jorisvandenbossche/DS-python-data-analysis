---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.6
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

## Simplified Statistical Sectors

https://statbel.fgov.be/nl/open-data/statistische-sectoren-2019

```{code-cell} ipython3
import geopandas
```

```{code-cell} ipython3
df = geopandas.read_file("/home/joris/Downloads/sh_statbel_statistical_sectors_20190101.shp.zip")
```

```{code-cell} ipython3
df = df.dissolve("CNIS5_2019").reset_index()
```

```{code-cell} ipython3
import topojson as tp
topo = tp.Topology(df, prequantize=True)
res = topo.toposimplify(1000).to_gdf()
```

```{code-cell} ipython3
res.plot()
```

```{code-cell} ipython3
res.crs = df.crs
```

```{code-cell} ipython3
res[["CNIS5_2019", "T_MUN_NL", "geometry"]].to_file("statbel_statistical_sectors_2019.shp")
```

```{code-cell} ipython3

```
