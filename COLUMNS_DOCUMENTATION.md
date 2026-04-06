# ENB2012 Dataset - Column Documentation

This document explains all the columns in the ENB2012 (Energy Efficiency Building) dataset.

## Input Features (X1 to X8)

### **X1: Relative Compactness**

- **Description**: The ratio of the building's surface area to its volume
- **Data Type**: Continuous (Float)
- **Measurement**: Ratio
- **Range**: Typically between 0.6 and 1.0
- **Importance**: Lower compactness indicates a more complex building shape, which affects heat loss/gain

### **X2: Surface Area**

- **Description**: The total surface area of the building envelope
- **Data Type**: Continuous (Float)
- **Measurement**: m² (Square meters)
- **Range**: Typically between 514 and 905
- **Importance**: Larger surface areas lead to greater heat exchange with the environment

### **X3: Wall Area**

- **Description**: The total area of all walls in the building
- **Data Type**: Continuous (Float)
- **Measurement**: m² (Square meters)
- **Range**: Typically between 245 and 416
- **Importance**: Walls are major components in building heat transfer

### **X4: Roof Area**

- **Description**: The total area of the roof(s) in the building
- **Data Type**: Continuous (Float)
- **Measurement**: m² (Square meters)
- **Range**: Typically between 110 and 189
- **Importance**: Roofs have significant thermal conductance and are exposed to solar radiation

### **X5: Overall Height**

- **Description**: The height of the building from ground to roof
- **Data Type**: Continuous (Float)
- **Measurement**: m (Meters)
- **Range**: Typically between 3.5 and 7.0
- **Importance**: Building height affects heat distribution and ventilation efficiency

### **X6: Orientation**

- **Description**: The cardinal direction the building faces
- **Data Type**: Categorical (Discrete)
- **Possible Values**:
  - 2 = North
  - 3 = South
  - 4 = East
  - 5 = West
- **Importance**: Orientation affects solar heat gain throughout the day and seasons

### **X7: Glazing Area**

- **Description**: The percentage of the wall area that is glass/windows
- **Data Type**: Continuous (Float)
- **Measurement**: % (Percentage)
- **Range**: 0%, 10%, 25%, 40% (discrete values)
- **Importance**: Windows significantly affect building thermal performance through heat loss in winter and solar heat gain in summer

### **X8: Glazing Area Distribution**

- **Description**: How the glazing (windows) is distributed across the building's facades
- **Data Type**: Categorical (Discrete)
- **Possible Values**:
  - 0 = Uniform distribution (all sides equally glazed)
  - 1 = Spread out (asymmetric distribution)
  - 2 = Concentrated on one side
  - 3 = Concentrated on two opposite sides
- **Importance**: The distribution pattern affects the building's thermal performance and daylighting

---

## Target Variables (Y1 and Y2)

### **Y1: Heating Load**

- **Description**: The amount of energy required to heat the building to maintain comfortable indoor temperature during winter
- **Data Type**: Continuous (Float)
- **Measurement**: kWh/m²year (Kilowatt-hours per square meter per year)
- **Range**: Typically between 6.0 and 43.0
- **Interpretation**: Higher values indicate greater heating energy requirement (typically occurs in colder climates or poorly insulated buildings)

### **Y2: Cooling Load**

- **Description**: The amount of energy required to cool the building to maintain comfortable indoor temperature during summer
- **Data Type**: Continuous (Float)
- **Measurement**: kWh/m²year (Kilowatt-hours per square meter per year)
- **Range**: Typically between 10.0 and 48.0
- **Interpretation**: Higher values indicate greater cooling energy requirement (typically occurs in warmer climates or poorly insulated buildings)

---

## Dataset Summary

| Aspect               | Details                                                         |
| -------------------- | --------------------------------------------------------------- |
| **Total Samples**    | 768                                                             |
| **Input Features**   | 8 (X1-X8)                                                       |
| **Target Variables** | 2 (Y1, Y2)                                                      |
| **Feature Types**    | 6 Continuous + 2 Categorical                                    |
| **Task Type**        | Regression (predicting energy loads) or Multi-output Regression |
| **Dataset Source**   | UCI Machine Learning Repository                                 |

---

## Use Cases

This dataset is commonly used for:

- **Regression Analysis**: Predicting heating and cooling loads from building characteristics
- **Energy Efficiency Studies**: Analyzing which building factors most influence energy consumption
- **Machine Learning Practice**: Classification (by discretizing targets), Regression, or Feature Selection exercises
- **Building Design Optimization**: Understanding the impact of design choices on energy efficiency

---

## Related Features

- **Related Pair**: X1 (Compactness) and X2 (Surface Area) are interdependent
- **Correlated Pair**: X3 (Wall Area) and X4 (Roof Area) are architectural components
- **Important Interaction**: X7 (Glazing Area) × X6 (Orientation) heavily influences both Y1 and Y2
