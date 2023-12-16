import numpy as np
import mlx.core as mx
import time
import argparse
from tqdm import tqdm
import threading

# Argument-Parser einrichten
parser = argparse.ArgumentParser(description='Vergleiche Numpy und MXNet Geschwindigkeit.')
parser.add_argument('--iter', type=int, default=10000, help='Anzahl der Iterationen')
parser.add_argument('--size', type=int, default=100, help='Größe der zu generierenden Arrays')
parser.add_argument('--lib', choices=['numpy', 'mx', 'both'], default='both', help='Welche Bibliothek(en) zu benutzen')
parser.add_argument('--mode', choices=['sequential', 'parallel'], default='sequential', help='Ausführungsmodus: sequential oder parallel')

# Argumente parsen
args = parser.parse_args()
ITER = args.iter
array_size = args.size
library = args.lib
mode = args.mode

# Funktionen für Numpy und MXNet Berechnung mit Fortschrittsanzeige
def numpy_calculation():
    print("Start np")
    start_time_np = time.time()
    for i in tqdm(range(ITER), desc="Numpy Fortschritt"):
        arr1 = np.random.normal(size=(array_size, array_size))
        arr2 = np.random.normal(size=(array_size, array_size))
        res = np.matmul(arr1, arr2)
    end_time_np = time.time()
    print("Done np")
    return end_time_np - start_time_np

def mxnet_calculation():
    print("Start mx")
    start_time_mx = time.time()
    for i in tqdm(range(ITER), desc="MXNet Fortschritt"):
        arr1 = mx.random.normal(shape=(array_size, array_size))
        arr2 = mx.random.normal(shape=(array_size, array_size))
        res = mx.matmul(arr1, arr2)
    end_time_mx = time.time()
    print("Done mx")
    return end_time_mx - start_time_mx

# Parallele Ausführung
def run_parallel():
    thread_np = threading.Thread(target=numpy_calculation)
    thread_mx = threading.Thread(target=mxnet_calculation)

    thread_np.start()
    thread_mx.start()

    thread_np.join()
    thread_mx.join()

# Ausführung basierend auf der Auswahl
if library in ['numpy', 'both'] and mode == 'sequential':
    numpy_time = numpy_calculation()
    print(f"Numpy Zeit: {numpy_time} Sekunden")

if library in ['mx', 'both'] and mode == 'sequential':
    mxnet_time = mxnet_calculation()
    print(f"MXNet Zeit: {mxnet_time} Sekunden")

if library == 'both' and mode == 'parallel':
    run_parallel()

