import matplotlib.pyplot as plt

sizes = [16, 64, 128, 256, 384, 512, 768, 1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968]

### Memory Usage ###
basic_memory_usage = [33780, 33668, 33784, 33888, 34040, 34296, 34932, 35832, 36988, 38396, 41976, 46584, 52212, 58872, 64492]
efficient_memory_usage = [33824, 33412, 33584, 33444, 33488, 33692, 33820, 33576, 33648, 33816, 33560, 33816, 33816, 33996, 33952]

plt.figure()
plt.plot(sizes, basic_memory_usage, marker='o', label='Basic')
plt.plot(sizes, efficient_memory_usage, marker='x', label='Efficient')
plt.xlabel("Problem Size (M+N)")
plt.ylabel("Memory Usage (KB)")
plt.title("Memory Usage vs Problem Size")
plt.legend()
plt.grid(True)
plt.savefig("mem.png")
####################

### Time ###
basic_time = [0.299, 3.202, 8.171, 39.891, 80.517, 133.161, 310.479, 560.541, 904.262, 1258.838, 2350.609, 4048.067, 5403.797, 7185.061, 8802.497]
efficient_time = [1.173, 9.470, 16.698, 56.085, 127.605, 234.343, 486.038, 900.299, 1431.120, 2004.242, 3676.181, 3144.777, 8095.509, 11255.246, 11010.766]

plt.figure()
plt.plot(sizes, basic_time, marker='o', label='Basic')
plt.plot(sizes, efficient_time, marker='x', label='Efficient')
plt.xlabel("Problem Size (M+N)")
plt.ylabel("Time (MS)")
plt.title("Time vs Problem Size")
plt.legend()
plt.grid(True)
plt.savefig("time.png")
####################