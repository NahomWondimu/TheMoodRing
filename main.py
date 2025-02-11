import matplotlib as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)  # 100 points between 0 and 10
y = np.sin(x)  # Sine of x values

# Create a plot
plt.plot(x, y)

# Add labels and a title
plt.title('Sine Wave Test Plot')
plt.xlabel('x values')
plt.ylabel('y values')

# Show the plot
plt.show()
