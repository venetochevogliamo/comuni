# Comuni Veneto 🏙️

Lista dei comuni della Regione Veneto. Il file JSON [`comuni-veneto.json`](https://github.com/venetochevogliamo/comuni/blob/master/comuni-veneto.json) segue il seguente schema:

```
{
        "nome": "Cittadella",
        "codice": "028032",
        "zona": {
            "codice": "2",
            "nome": "Nord-est"
        },
        "regione": {
            "codice": "05",
            "nome": "Veneto"
        },
        "provincia": {
            "codice": "028",
            "nome": "Padova"
        },
        "sigla": "PD",
        "codiceCatastale": "C743",
        "cap": [
            "35013"
        ],
        "popolazione": 19956
    }
```

# Development

È richiesto:

- Python 3

Scaricare il file con tutti i comuni con il seguente comando:

```
wget 'https://raw.githubusercontent.com/matteocontrini/comuni-json/master/comuni.json' -O comuni.json
```

A questo punto lanciare: `python3 clean.py`.
