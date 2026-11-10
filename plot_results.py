"""Creates the results chart used in the project report.

The four data sets below are the same test cases that were run through
mixing_tank_balance.py. This script repeats the same calculation
(accumulation, absolute error, percentage error) and plots the answers.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# (label, inlet flows in kg/h, outlet flow in kg/h, tolerance in %)
cases = [
    ("Case 1", [100, 150, 250], 495, 2),
    ("Case 2", [200, 300], 500, 1),
    ("Case 3", [200, 300], 450, 5),
]

labels, total_in, outlet, err_pct, tol = [], [], [], [], []
for name, inlet, out, t in cases:
    total = np.sum(inlet)
    acc = total - out
    err = abs(acc) / total * 100 if total != 0 else 0
    labels.append(name)
    total_in.append(total)
    outlet.append(out)
    err_pct.append(err)
    tol.append(t)
    print(f"{name}: inlet={total} outlet={out} accumulation={acc} error={err:.2f}% tolerance={t}%")

x = np.arange(len(labels))
w = 0.35
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].bar(x - w / 2, total_in, w, label="Total inlet", color="#4c72b0")
ax[0].bar(x + w / 2, outlet, w, label="Outlet", color="#dd8452")
ax[0].set_xticks(x)
ax[0].set_xticklabels(labels)
ax[0].set_ylabel("Flow rate (kg/h)")
ax[0].set_title("Inlet and outlet flow")
ax[0].legend()

ax[1].bar(x - w / 2, err_pct, w, label="Percentage error", color="#c44e52")
ax[1].bar(x + w / 2, tol, w, label="Tolerance", color="#8c8c8c")
ax[1].set_xticks(x)
ax[1].set_xticklabels(labels)
ax[1].set_ylabel("Percent (%)")
ax[1].set_title("Error compared with tolerance")
ax[1].legend()

plt.tight_layout()
plt.savefig("outputs/results_chart.png", dpi=200)
print("Saved outputs/results_chart.png")
