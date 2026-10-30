import numpy as np
print("TEAM CODEX FROM CHEMICAL DEPARTMENT SECTION - A ")
print("\nMATERIAL BALANCE IN A MIXING TANK")
print("----------------------------------")


n = int(input("Enter number of inlet streams: "))


if n <= 0:
    print("Error: Number of inlet streams must be greater than zero.")
    exit()


inlet = []

for i in range(n):
    flow = float(input(f"Enter inlet {i+1} flow rate (kg/h): "))

    if flow < 0:
        print("Error: Flow rate cannot be negative.")
        exit()

    inlet.append(flow)


inlet = np.array(inlet)


outlet = float(input("Enter outlet flow rate (kg/h): "))

if outlet < 0:
    print("Error: Outlet flow rate cannot be negative.")
    exit()


total_inlet = np.sum(inlet)


accumulation = total_inlet - outlet

absolute_error = abs(accumulation)


if total_inlet != 0:
    percentage_error = (absolute_error / total_inlet) * 100
else:
    percentage_error = 0


print("\n------ RESULTS ------")
print(f"Total Inlet Flow   : {total_inlet:.2f} kg/h")
print(f"Outlet Flow        : {outlet:.2f} kg/h")
print(f"Accumulation       : {accumulation:.2f} kg/h")
print(f"Absolute Error     : {absolute_error:.2f} kg/h")
print(f"Percentage Error   : {percentage_error:.2f}%")


tolerance = float(input("\nEnter acceptable error tolerance (%): "))

if percentage_error == 0:
    print("Status: PERFECTLY BALANCED")

elif percentage_error <= tolerance:
    print("Status: BALANCE ACCEPTABLE")

else:
    print("Status: MATERIAL IMBALANCE")

print("---------------------")
