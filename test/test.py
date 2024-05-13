import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
import pickle

with open('model.pkl', 'rb') as file:
    tree_model = pickle.load(file)

df="Data to Addd"

object_cols = ['address', 'first_borrow_date', 'token_borrow_mode', 'calc_start_time', 'added_at']
label_encoder = LabelEncoder()
for col in object_cols:
    new_data[col] = label_encoder.transform(new_data[col])

y_pred_new = tree_model.predict(new_data)

predictions_df = pd.DataFrame({
    'Unnamed: 0': new_data.index,  # Using the index of new_data as 'Unnamed: 0'
    'Prediction': y_pred_new
})


predictions_df.to_csv('new_predictions.csv', index=False)
