import matplotlib.pyplot as plt
import numpy as np
import msvcrt
import time

while(True):
    objects = []
    with open("objects.log") as file:
        for line in file: 
            objects.append(line)
    #object_scores = [98.7, 65.9887]
    object_scores = []
    file.close()
    with open("object_scores.log") as file:
        for line in file:
            line = line.strip()
            object_scores.append(float(line))
    print(object_scores)
    file.close()

    y_pos = np.arange(len(objects))
    plt.bar(y_pos, object_scores, align='center', alpha=0.8)
    plt.xticks(y_pos, objects)
    plt.ylabel('Scores')
    plt.title('Face Recognittion')
    plt.show()
    plt.close(1)
    if msvcrt.kbhit():
	    if ord(msvcrt.getch()) == 27: #press ESC AND close the graph
	        break

    