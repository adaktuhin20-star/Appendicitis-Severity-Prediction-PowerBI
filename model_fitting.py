# 'dataset' holds the input data for this script
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score

# Power BI automatically loads your data into 'dataset'
df = dataset.copy()

# 1. Prevent Data Leakage & Drop Identifiers
cols_to_drop = ['Patient_ID', 'Pathological_Cause', 'Management', 'Final_Diagnosis']
df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])

# 2. Define Features (X) and Target (y)
target_column = 'Severity'
X = df.drop(columns=[target_column])
y = df[target_column]

# 3. Encode Categorical Variables
categorical_cols = X.select_dtypes(include=['object', 'category']).columns
for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])

le_target = LabelEncoder()
y_encoded = le_target.fit_transform(y)

# 4. Train-Test Split (Hold out 20% of data for pure testing)
# Using stratify to ensure the same ratio of severe cases in both sets
X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(
    X, y_encoded, df.index, test_size=0.2, random_state=42, stratify=y_encoded
)

# 5. Initialize the Model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')

# 6. Perform 5-Fold Cross-Validation on the Training Set
cv_scores = cross_val_score(rf_model, X_train, y_train, cv=5, scoring='accuracy')
cv_mean_accuracy = cv_scores.mean()

# 7. Train the final model ONLY on the Training Set
rf_model.fit(X_train, y_train)

# 8. Generate Predictions & Attach to Original Dataset
# We predict on X (the whole dataset) so the dashboard is fully populated
dataset['Predicted_Severity'] = le_target.inverse_transform(rf_model.predict(X))
dataset['Prediction_Confidence'] = rf_model.predict_proba(X).max(axis=1)

# Tag each row so Power BI knows if it was used to train or test the model
dataset['Data_Split'] = 'Train'
dataset.loc[indices_test, 'Data_Split'] = 'Test'

# Attach the CV score as a metric for the dashboard KPI cards
dataset['CV_Accuracy_Score'] = cv_mean_accuracy