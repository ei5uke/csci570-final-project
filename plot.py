import matplotlib.pyplot as plt

sizes = [16, 64, 128, 256, 384, 512, 768, 1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968]

### Memory Usage ###
basic_memory_usage = [40416, 40096, 40128, 40224, 40560, 41568, 41936, 42560, 43920, 45424, 48656, 52992, 58624, 65808, 71632]
efficient_memory_usage = [40496, 41088, 40896, 41456, 40864, 40032, 41184, 40784, 40768, 40416, 41248, 40160, 40256, 40688, 41040]

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
basic_time = [0.380, 1.226, 4.184, 25.790, 52.203, 80.957, 183.311, 291.934, 442.894, 611.405, 1087.381, 1695.491, 2441.489, 3359.632, 4192.616]
efficient_time = [0.248, 1.962, 4.718, 22.183, 50.958, 107.978, 204.926, 356.180, 517.937, 760.617, 1360.526, 2008.715, 2931.417, 3974.431, 4973.406]

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