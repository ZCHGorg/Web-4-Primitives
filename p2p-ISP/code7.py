import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Define preprocessing steps
preprocessing = StandardScaler()

# Define feature selection
feature_selection = SelectKBest()

# Define model
model = RandomForestClassifier()

# Create pipeline
pipeline = Pipeline([('preprocessing', preprocessing),
                     ('feature_selection', feature_selection),
                     ('model', model)])

# Fit model to training data
X = df[df.columns[:-1]]
y = df[df.columns[-1]]
pipeline.fit(X, y)

# Use model to make predictions on test data
X_test = pd.read_csv('your_test_data.csv')
predictions = pipeline.predict(X_test)