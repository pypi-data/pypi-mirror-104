# Was ist das

Ihr kauft für Kollegen Essen, kocht und esst zusammen. Wer schuldet wem nun wie
viel Geld?

Gebt pro Einkauf den Betrag, die Mitesser und den Bezahler ein und ruft `calc()`
bzw. `pprint()` auf oder `journal()` und nimmt die Ausgabe als Basis für `hledger`.

```
$ cat basic.py
$ cat main.py
#!/usr/bin/env python3
from mahlzeit import Mahlzeit

m = Mahlzeit()

m.einkauf(28.62, ('Jann', 'Flo', 'Max'), 'Flo')
m.einkauf(2.22, ('Jann', 'Flo', 'Max'), 'Jann')
m.einkauf(14.24, ('Kai', 'Jann', 'Flo', 'Max'), 'Max')
m.einkauf(2.90, ('Kai', 'Jann', 'Flo', 'Max'), 'Kai')
m.einkauf(18.73, ('Julie', 'Jann', 'Flo', 'Max'), 'Flo')
m.pprint()
m.bezahlung('Max', 'Flo', 5)
m.pprint()

python3 basic.py

$ cat ledger.py
#!/usr/bin/env python3
from mahlzeit import Mahlzeit

m = Mahlzeit()

with m(datum='2021/05/02', description='Essen 1'):
	m.einkauf(28.62, ('Jann', 'Flo', 'Max'), 'Flo')
	m.einkauf(2.22, ('Jann', 'Flo', 'Max'), 'Jann')
with m(datum='2021/05/03', description='Essen 2'):
	m.einkauf(14.24, ('Kai', 'Jann', 'Flo', 'Max'), 'Max')
	m.einkauf(2.90, ('Kai', 'Jann', 'Flo', 'Max'), 'Kai')
	m.einkauf(18.73, ('Julie', 'Jann', 'Flo', 'Max'), 'Flo')
with m(datum='2021/05/03', description='Essen 2'):
	m.bezahlung('Max', 'Flo', 5)

m.journal()

# use interactively as
$ hledger -f <(python3 main.py) balance
```

```
$ python3 basic.py
      Jann -20.00
       Max -5.00
     Julie -5.00
       Kai -2.00
       Flo 20.00
```

# Installation

Aktuell per `virtualenv`

```
virtualenv -p python3 venv
source venv/bin/activate
python3 setup.py install
python3 example.py
```

# Mehrgewichtige Esser

Ihr habt ein Paar in der Essgruppe, die manchmal Speisen gemeinsam kaufen und
deshalb gemeinsam veranlagt werden müssen?

```
#!/usr/bin/env python3
from mahlzeit import Mahlzeit, Esser as E

m = Mahlzeit()

m.einkauf(15, ('Laura', 'Nils', E('Katja_Martin', 2), 'Max'), 'Katja_Martin')
m.pprint()
```

```
$ python3 main.py
       Max -3.00
      Nils -3.00
     Laura -3.00
Katja_Martin 9.00
```

# Tests

Tests laufen mit `make test`.
