# Major Preprocessing Steps in Machine Learning

Preprocessing is a critical step in the machine learning pipeline that involves transforming raw data into a format suitable for model training. Below are the major preprocessing steps applied to datasets:

---

## 1. Data Cleaning

### 1.1 Removing Duplicates

- Identify and remove duplicate rows from the dataset
- Helps prevent bias and redundancy in training data
- Use: `pandas.DataFrame.drop_duplicates()`

### 1.2 Handling Invalid Values

- Remove or correct data entries that are clearly incorrect
- Validate data types and formats
- Remove rows with inconsistent or corrupted data

### 1.3 Removing Irrelevant Features

- Identify and drop columns that do not contribute to predictions
- Remove redundant features that carry the same information
- Example: Drop ID columns, timestamps that won't help prediction

---

## 2. Handling Missing Values

### 2.1 Identifying Missing Data

- Detect NaN, NULL, or missing values using `.isnull()` or `.isna()`
- Analyze the percentage of missing values per feature

### 2.2 Strategies for Missing Values

- **Deletion**: Remove rows or columns with missing data
  - Useful when missing data is < 5-10% of total
  - Use: `pandas.DataFrame.dropna()`
- **Imputation**: Fill missing values with estimated data
  - **Mean/Median**: Numerical features (less sensitive to outliers)
  - **Mode**: Categorical features (most frequent value)
  - **Forward/Backward Fill**: Time-series data
  - **Interpolation**: For sequential data
  - Use: `pandas.DataFrame.fillna()` or `sklearn.impute.SimpleImputer`

---

## 3. Handling Outliers

### 3.1 Detecting Outliers

- **Statistical methods**: Z-score, IQR (Interquartile Range)
- **Visualization**: Box plots, scatter plots
- **Domain knowledge**: Identify unrealistic values

### 3.2 Treating Outliers

- **Removal**: Delete rows with extreme outliers
- **Transformation**: Apply log, square root transformations
- **Capping**: Set upper and lower bounds for values
- **Separate modeling**: Create separate model for outliers

---

## 4. Feature Encoding

### 4.1 Categorical to Numerical Encoding

- **Label Encoding**: Convert categories to integers (0, 1, 2, ...)

  - Use for ordinal features where order matters
  - Use: `sklearn.preprocessing.LabelEncoder`

- **One-Hot Encoding**: Create binary columns for each category

  - Use for nominal features without order
  - Use: `pandas.get_dummies()` or `sklearn.preprocessing.OneHotEncoder`

- **Ordinal Encoding**: Map categories to custom numerical values
  - Use: `sklearn.preprocessing.OrdinalEncoder`

### 4.2 Text Data Encoding

- **Tokenization**: Split text into words
- **Vectorization**: Convert text to numerical vectors
  - TF-IDF (Term Frequency-Inverse Document Frequency)
  - Word2Vec embeddings
  - Use: `sklearn.feature_extraction.text.TfidfVectorizer`

---

## 5. Feature Scaling/Normalization

### 5.1 Standardization (Z-score Normalization)

- Transform features to have mean = 0 and standard deviation = 1
- Formula: $z = \frac{x - \mu}{\sigma}$
- Suitable for algorithms sensitive to feature magnitude (KNN, SVM, Neural Networks)
- Use: `sklearn.preprocessing.StandardScaler`

### 5.2 Min-Max Scaling (Normalization)

- Scale features to a range [0, 1] or [-1, 1]
- Formula: $x_{scaled} = \frac{x - x_{min}}{x_{max} - x_{min}}$
- Preserves the distribution of original data
- Use: `sklearn.preprocessing.MinMaxScaler`

### 5.3 Robust Scaling

- Scale using median and interquartile range
- Less sensitive to outliers than standard scaling
- Use: `sklearn.preprocessing.RobustScaler`

### 5.4 Log Scaling

- Apply logarithmic transformation to right-skewed data
- Helps normalize distributions and reduce the impact of large values

---

## 6. Feature Engineering

### 6.1 Feature Creation

- Create new features from existing ones
- Examples: Age groups, interaction terms, polynomial features
- Enhance model performance and interpretability

### 6.2 Feature Selection

- Identify most important features
- **Methods**: Correlation analysis, feature importance, recursive elimination
- Reduce dimensionality and improve model efficiency
- Use: `sklearn.feature_selection.SelectKBest`, `RFE`

### 6.3 Dimensionality Reduction

- Reduce number of features while retaining information
- **Methods**: PCA (Principal Component Analysis), t-SNE
- Reduce computational cost and avoid curse of dimensionality
- Use: `sklearn.decomposition.PCA`

---

## 7. Handling Imbalanced Data

### 7.1 For Classification Problems

- **Oversampling**: Increase samples from minority class
  - Use: `imblearn.over_sampling.RandomOverSampler`, SMOTE
- **Undersampling**: Decrease samples from majority class
  - Use: `imblearn.under_sampling.RandomUnderSampler`
- **Class weights**: Assign higher weights to minority class
  - Use: `class_weight` parameter in sklearn models

---

## 8. Train-Test Split

### 8.1 Splitting Data

- Divide dataset into training (70-80%) and testing (20-30%) sets
- Ensures model evaluation on unseen data
- Use: `sklearn.model_selection.train_test_split`

### 8.2 Cross-Validation

- Divide data into k folds for more robust evaluation
- Use: `sklearn.model_selection.KFold`, `StratifiedKFold`

### 8.3 Stratified Split

- Maintain class distribution in train-test split
- Important for imbalanced datasets
- Use: `sklearn.model_selection.train_test_split(stratify=y)`

---

## 9. Data Transformation

### 9.1 Polynomial Features

- Create interaction terms and polynomial features
- Useful for non-linear relationships
- Use: `sklearn.preprocessing.PolynomialFeatures`

### 9.2 Binning

- Convert continuous variables into categorical bins
- Create age groups, income brackets, etc.
- Use: `pandas.cut()`, `pandas.qcut()`

### 9.3 Date/Time Features

- Extract year, month, day, day of week from timestamps
- Create cyclical features for seasonal patterns

---

## 10. Data Validation

### 10.1 Data Quality Checks

- Verify data types are correct
- Check value ranges and distributions
- Validate business logic constraints

### 10.2 Statistical Validation

- Analyze descriptive statistics (mean, median, std dev)
- Check data distribution (skewness, kurtosis)
- Identify anomalies or unexpected patterns

---

## 11. Handling Multicollinearity

### 11.1 Detecting Multicollinearity

- Calculate correlation matrix between features
- Compute Variance Inflation Factor (VIF)
- Use: `statsmodels.stats.outliers_influence.variance_inflation_factor`

### 11.2 Addressing Multicollinearity

- Remove one of the correlated features
- Use dimensionality reduction techniques (PCA)
- Regularization methods (L1/L2 regularization)

---

## Typical Preprocessing Pipeline

```
Raw Data
    ↓
1. Load and Explore Data
    ↓
2. Remove Duplicates and Invalid Data
    ↓
3. Handle Missing Values
    ↓
4. Detect and Handle Outliers
    ↓
5. Encode Categorical Variables
    ↓
6. Feature Engineering
    ↓
7. Scale/Normalize Features
    ↓
8. Handle Imbalanced Data (if needed)
    ↓
9. Select Important Features
    ↓
10. Train-Test Split
    ↓
Processed Data Ready for Model Training
```

---

## Best Practices

1. **Always explore data first** - Use EDA (Exploratory Data Analysis) before preprocessing
2. **Fit on training data only** - Fit scalers/encoders on training set, then transform test set
3. **Document preprocessing steps** - Keep track of all transformations applied
4. **Avoid data leakage** - Ensure test data is not used during fitting preprocessing objects
5. **Iterative approach** - Preprocessing is often iterative; monitor model performance and adjust
6. **Domain knowledge** - Use subject matter expertise to guide preprocessing decisions
7. **Validate results** - Check data quality after each preprocessing step

---

## Common Libraries Used

- **pandas**: Data manipulation and cleaning
- **numpy**: Numerical operations
- **scikit-learn**: Preprocessing tools and machine learning algorithms
- **imbalanced-learn**: Handling imbalanced datasets
- **matplotlib & seaborn**: Data visualization
