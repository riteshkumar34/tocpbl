#Visualization of TM

import matplotlib.pyplot as plt
import time

def visualize_tape(tape):
    plt.figure(figsize=(10, 2))
    plt.xticks(range(len(tape)), tape)
    plt.grid()
    plt.show()
    time.sleep(1)


visualize_tape(list("101____"))

