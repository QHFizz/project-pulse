import matplotlib.pyplot as plt
labels = ["Commits", "Files"]
values = [34, 8]
file_types = ["py", "txt", "csv"]
counts = [12, 6, 3]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.bar(labels, values, color="#2563eb")
ax1.set_title("Project Activity")
ax2.pie(counts, labels=file_types, autopct="%1.1f%%", colors=["#16a34a","#3b82f6","#facc15"])
ax2.set_title("File Type Breakdown")
plt.tight_layout()
plt.savefig("pulse_dashboard.png")
print("pulse_dashboard.png created")
