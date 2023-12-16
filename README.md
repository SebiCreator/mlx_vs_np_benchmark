# Matmul Benchmark Mlx vs Numpy

## Voraussetzungen

Bevor Sie dieses Skript ausführen, stellen Sie sicher, dass die folgenden Bibliotheken installiert sind:

* numpy 
* mlx 
* tqdm

Um diese zu laden bitte die requirements.txt laden 

```console
pip install -r requirements.txt
```

## Verwendung

Das Skript kann über die Kommandozeile mit verschiedenen Optionen gesteuert werden, um die Testbedingungen anzupassen:

* **--iter**: Die Anzahl der Iterationen für die Matrixmultiplikation (Standardwert: 10000).

* **--size**: Die Größe der zu generierenden Matrizen (Standardwert: 100).

* **--lib**: Wählen Sie die zu testende Bibliothek aus. Mögliche Werte sind 'numpy', 'mx', oder 'both' (Standardwert: 'both').

* **--mode**: Wählen Sie den Ausführungsmodus aus. Mögliche Werte sind 'sequential' für sequenzielle Ausführung oder 'parallel' für parallele Ausführung (Standardwert: 'sequential').

## Beispiele

* Numpy only
```console
python3 run_benchmark.py --lib numpy
```

* Mx only
```console
python3 run_benchmark.py --lib mx
```

* Beide Libs sequenziell 
```console
python3 run_benchmark.py --lib both --mode sequential
```

* Beide Libs paralell
```console
python3 run_benchmark.py --lib both --mode parallel
```

## Funktionsweise

Das Programm führt Matrixmultiplikationen durch, indem es zufällige Matrizen mit der spezifizierten Größe generiert und diese dann multipliziert. Die Gesamtzeit, die für die Ausführung der Operationen benötigt wird, wird gemessen und am Ende ausgegeben. Bei Auswahl des parallelen Modus werden die Berechnungen für Numpy und MXNet in separaten Threads ausgeführt.



