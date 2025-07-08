## 📦 1. FunctionTransformer
Wraps any custom Python function so it can be used inside a scikit-learn pipeline.
Your function must take a NumPy array or pandas Series/DataFrame and return the transformed version.

**🔑 Why?**
It makes your custom functions compatible with fit_transform.
```python
from sklearn.preprocessing import FunctionTransformer

def my_custom_func(X):
    return X + 1

transformer = FunctionTransformer(my_custom_func)

X = np.array([1, 2, 3])
print(transformer.transform(X))  # Output: [2 3 4]

```


## 🧩 2. ColumnTransformer
**✅ What it does:**
Lets you apply different preprocessing steps to different columns in a DataFrame.

Example: One column gets scaled, another gets encoded, another gets vectorized.

```ColumnTransformer applies one transformer per column```

**🔑 Why?**
For real-world data with mixed types (text, numbers, categories), you must preprocess them differently.

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

preprocessor = ColumnTransformer([
    ("scale_num", StandardScaler(), ["num_col"]),
    ("encode_cat", OneHotEncoder(), ["cat_col"])
])
```


## 🔗 3. Pipeline
**✅ What it does:**
Chains multiple steps (transformers + model) together in one object.

Data goes through each step in order.

Makes your workflow clean, reproducible, and cross-validated.

```python
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

pipe = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", LogisticRegression())
])
```