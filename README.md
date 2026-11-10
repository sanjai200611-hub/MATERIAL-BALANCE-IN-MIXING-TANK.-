# Material Balance in a Mixing Tank

A Python case study by **Team Codex**, Department of Chemical Engineering (Section A).

| Name | Register Number |
|---|---|
| SANJAI M | RA2411007010037 |
| ARJUN M | RA2411007010031 |

## About the project

A mixing tank takes in several inlet streams and gives out one outlet stream. If no reaction happens inside, the total mass going in should equal the total mass coming out. This program checks that using the law of conservation of mass.

The user enters the flow rate of each inlet stream, the outlet flow rate and an acceptable error tolerance. The program then calculates:

- total inlet flow
- accumulation = total inlet - outlet
- absolute error
- percentage error

and prints one of three results: **PERFECTLY BALANCED**, **BALANCE ACCEPTABLE** or **MATERIAL IMBALANCE**.

## Objectives

- Apply the law of conservation of mass to a mixing tank
- Accept any number of inlet streams
- Calculate accumulation and error automatically
- Reject impossible inputs such as negative flow rates

## Requirements

- Python 3.8 or newer
- NumPy
- Matplotlib (only for `plot_results.py`)

Install with:

```
pip install -r requirements.txt
```

## How to run

Main program:

```
python "python team codex.py"
```

Example input and output (Case 1):

```
Enter number of inlet streams: 3
Enter inlet 1 flow rate (kg/h): 100
Enter inlet 2 flow rate (kg/h): 150
Enter inlet 3 flow rate (kg/h): 250
Enter outlet flow rate (kg/h): 495

------ RESULTS ------
Total Inlet Flow   : 500.00 kg/h
Outlet Flow        : 495.00 kg/h
Accumulation       : 5.00 kg/h
Absolute Error     : 5.00 kg/h
Percentage Error   : 1.00%

Enter acceptable error tolerance (%): 2
Status: BALANCE ACCEPTABLE
```

To regenerate the results chart used in the report:

```
python plot_results.py
```

## Files

| File | Description |
|---|---|
| `python team codex.py` | Main program (already in the repository) |
| `plot_results.py` | Makes the bar charts for the test cases |
| `requirements.txt` | Python libraries needed |
| `outputs/sample_output_case1.txt` to `case4.txt` | Program output for the four test cases |
| `outputs/results_chart.png` | Chart of the results |

## Limitations

- Only a total mass balance (single component)
- Assumes steady state
- Typing text instead of a number stops the program with a ValueError
