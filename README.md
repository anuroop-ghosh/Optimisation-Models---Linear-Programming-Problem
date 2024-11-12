## Smart Rug Manufacturer - Linear Optimization Model

This Python code implements a linear optimization model to solve the following problem.

**Problem**

*Smart Rug Manufacturers has available1800 square meters of wool and 800 square meters of nylon
for the manufacture of two grades of carpeting: high-grade, which sells for £850 per roll, and low-
grade, which sells for £650 per roll.
35 square meters of wool and 15 square meters of nylon are used in a roll of high-grade carpet.
15 square meters of wool and 45 square meters of nylon are used in a roll of low-grade carpet.
25 work-hours are required to manufacture each roll of the high-grade carpet, and 20 work-hours
are required for each roll of the low-grade carpet, at an average cost of £7 per work-hour. A
maximum of 1000 work-hours are available.
The cost of wool is £4 per square meter and the cost of nylon is £3 per square meter.
What is the maximum income that can be achieved by manufacturing the carpets?
Hint :_Income=revenue from sale-(production cost for material+labor)*

**Mathematical Visualisation of the problem**
LP Model:
maximise  490x + 315y
    
subject to constraints:
        x,y ≥ 0
		35x + 15y ≤ 1800
        15x + 45y ≤ 800
		25x + 20y ≤ 1000  
        
<img width="236" alt="image" src="https://github.com/user-attachments/assets/e23f98d7-08f9-4e81-8fb8-6096ebf2d91c">

**Data Read from the excel file**

| Feature | High-Grade | Low-Grade | Available | Cost | |---|---|---|---|---| | Wool | 35 | 15 | 1800 | 4 | | Nylon | 15 | 45 | 800 | 3 | | Work Hours | 25 | 20 | 1000 | 7 | | Selling Price | 850 | 650 | | |


**Key Feature:**

* **Data-Driven Flexibility:** The model is designed to be adaptable to user-defined data. You can modify the values in the accompanying Excel file (`Optimisation Model - Smart Rug Manufacturer Problem.xlsx`) to tailor the optimization process to your specific scenario.

**How to Use This Code:**

1. **Install Required Libraries:**

   Ensure you have the following libraries installed in your Python environment:

   ```bash
   pip install pyomo pandas
   ```

2. **Prepare the Excel File:**

   * Locate or create the Excel file named `Optimisation Model - Smart Rug Manufacturer Problem.xlsx`.
   * Organize the data as described in the original prompt:
     - Material availability (wool, nylon)
     - Work hours required
     - Selling prices for each rug type
     - Costs of materials (wool, nylon, and labor)
   * Update any values as needed to reflect your desired scenario.

3. **Run the Python Script:**

   Execute the Python script containing this code. The program will read the data from the Excel file, compute the optimal solution based on the provided parameters, and print the results.

**Model Components:**

1. **Data Import:**
   * Reads data from the specified Excel file.
   * Extracts relevant information for the optimization model.

2. **Model Definition:**
   * Creates a Pyomo concrete model.
   * Defines decision variables representing the production quantities.

3. **Objective Function:**
   * Maximizes the total profit, considering selling prices and production costs.

4. **Constraints:**
   * Ensures that resource usage (material and labor) does not exceed availability.

5. **Solving and Printing Results:**
   * Uses the GLPK solver to find the optimal solution.
   * Prints the total profit and optimal production quantities for each rug type.

**Additional Considerations:**

* **Data Validation:** Consider adding error handling mechanisms to check for invalid data in the Excel file.
* **Sensitivity Analysis:** Explore how changes in input parameters affect the optimal solution. This can be achieved by modifying the Excel data and rerunning the script.
* **Visualization:** Create visualizations (e.g., using Matplotlib or Plotly) to enhance the presentation of the results.
* **User Interface:** For a more user-friendly experience, consider developing a user interface (using Tkinter or PyQt) to provide an interactive way to input data and display results.

**Benefits:**

* **Optimal Production Planning:** This model can assist in determining the production quantities that maximize profit within the given resource constraints.
* **Data-Driven Decisions:** The ability to modify the Excel data allows for scenario planning and analyzing the impact of changes on the optimal solution.
* **Improved Efficiency:** By leveraging optimization techniques, you can potentially optimize smart rug production processes, leading to increased efficiency and profitability.

This code provides a valuable tool for smart rug manufacturers seeking to optimize production strategies. By adapting the provided data and exploring further enhancements, you can gain valuable insights and maximize your business outcomes.
