import numpy as np
import matplotlib.pyplot as plt

sensitivity = 0.99

prevalence = np.linspace(0.00001, 0.5, 1000)

specificities = [0.99, 0.999, 0.9999, 0.99999] # blue, orange, green, red in order

def posterior_prob(p, sensitivity, specificities):
    return (sensitivity * p) / (sensitivity * p + (1 - specificities) * (1 - p))

plt.figure(figsize=(10, 6))

for spec in specificities:
    prob = posterior_prob(prevalence, sensitivity, spec)
    plt.plot(prevalence * 100, prob * 100, label=f"Specificity = {spec*100:.3f}%")

plt.xlabel("Prevalence in %")
plt.ylabel("P(Infect|Pos) in %")
plt.grid(True)

plt.show()
