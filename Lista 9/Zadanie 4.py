import sys
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["C", "Java", "Python", "C++", "C#", "Visual Basic", "JavaScript", "PHP", "R", "Groovy"])
y = np.array([17.38, 11.96, 11.72, 7.56, 3.95, 3.84, 2.20, 1.99, 1.90, 1.84])

plt.barh(x, y, color="hotpink", height=0.8)
plt.title("Popularność języków programowania")
plt.xlabel("Popularność [%]")
plt.ylabel("Język programowania")
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
