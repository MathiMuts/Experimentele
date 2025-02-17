# Hoe werkt de datastructuur???

De ruwe data zit allemaal in één grote dictionary `data_arrays`. In deze dictionaries zijn de volgende keys:
- `opgave1`
- `opgave2_1`
- `opgave2_2`
- `opgave2_3`
- `opgave3`
- `opgave4_1`
- `opgave4_freq1`
- `opgave4_freq2`
- `opgave5_1`
- `opgave5_freq1`
- `opgave5_freq2`
- `opgave5_freq3`

Die elk overeenkomen met een deelvraag in de opgave. Onder elk van deze keys (eg: `data_arrays['opgave1']`) zit een numpy array met alle Data-objecten van deze folder.
```
data_arrays['opgave1'] = np.array(<obj1>,
<obj2>,
<obj3>,
...,
<objx>)
```
## Korte herhaling van dataobjecten
zie practicum 7.