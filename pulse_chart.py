import matplotlib.pyplot as plt
lines = open("pulse.txt").read().splitlines()
labels = ["Commits", "Files"]
values = [int(lines[0]), int(lines[2])]
plt.bar(labels, values, color=["#2563eb", "#16a34a"])
plt.title("Pulse Overview")
plt.ylabel("Count")
plt.savefig("pulse_chart.png")
print("pulse_chart.png saved")