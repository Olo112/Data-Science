from matplotlib import pyplot as plt
import data

sine = data.sin_val()
angle = data.angke(sine)

plt.plot(angle, sine, color='blue', marker='o')

plt.grid(True)
plt.show()
