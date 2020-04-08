import matplotlib.pyplot as plt
import numpy

G = numpy.arange(0, 10, 0.01)
A = 0.05
P = 0.2

#PureAloha
PureAloha = G * numpy.exp(-2 * G)
#SlottedAloha
SlottedAloha = G * numpy.exp(-G)
#NonPersistent
NonPersistentSubEquation1 = G * numpy.exp(-A * G)
NonPersistentSubEquation2 = G * (1 + 2 * A) + numpy.exp(-A * G)
NonPersistent = NonPersistentSubEquation1 / NonPersistentSubEquation2
#onePersistent
onePersistentSubEquation1 = G * (1 + G + ((A * G) * (1 + G + ((A * G)/2))))
onePersistentSubEquation2 = numpy.exp(-G * (1 + 2 * A))
onePersistentSubEquation3 = G * (1 + 2 * A) - (1 - numpy.exp(-A * G)) + (1 + A * G) * numpy.exp(-G * (1 + A))
onePersistent= (onePersistentSubEquation1 * onePersistentSubEquation2) / onePersistentSubEquation3
#pPersistent
pPersistentSubEquation1 = (A + P) * G * numpy.exp(-(A + P) * G) - P * G * numpy.exp(-(2 * A + P) * G)
pPersistentSubEquation2 = (1 + A) * (1 - numpy.exp(-A * G)) + A * numpy.exp(-(A + P) * G)
pPersistent = pPersistentSubEquation1 / pPersistentSubEquation2

plt.plot(G, PureAloha, label = "PureAloha")
plt.plot(G, SlottedAloha, label = "SlottedAloha")
plt.plot(G, NonPersistent, label = "NonPersistent")
plt.plot(G, onePersistent, label = "onePersistent")
plt.plot(G, pPersistent, label = "pPersistent")


plt.title('Kleinrock-Tobagi Throughput Curves', loc='center', fontsize=12, fontweight=0, color='blue')
plt.xlabel('G = Offered Load', fontsize=12, fontweight=0, color='blue')
plt.ylabel('Throughput = Success Rate', fontsize=12, fontweight=0, color='blue')
plt.grid(alpha=.4, linestyle='--')

plt.legend()
plt.show()