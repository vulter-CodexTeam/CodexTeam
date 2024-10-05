#Analyzing Air Quality Data Using AI

import numpy as np
from sklearn.ensemble import RandomForestClassifier
air_quality_data = np.array([[35, 60, 25, 40, 10, 0.8]])
training_data = np.array([[30, 50, 20, 35, 8, 0.5], [70, 90, 45, 55, 25, 1.5], [15, 30, 12, 25, 5, 0.4]])
labels = np.array([0, 1, 0])  # Corresponding labels

model = RandomForestClassifier()
model.fit(training_data, labels)

prediction = model.predict(air_quality_data)
if prediction == 1:
    print("Air quality is unhealthy! Sending alert...")
else:
    print("Air quality is within safe limits.")
