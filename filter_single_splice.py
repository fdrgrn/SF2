#Same as filter_multiples_sclice.py, except that file path is changed
import pandas as pd
import numpy as np

def extract_runtime(df, velocity_inst):
    velocity = df[velocity_inst].fillna(0).to_numpy()
    
    difference = np.abs(np.diff(velocity))
    begin_index  = np.where(difference < 0.02)[0][0]
    
    for i in range(begin_index, len(velocity) - 1):
        if (np.sign(velocity[i]) != np.sign(velocity[i+1])) and (abs(velocity[i] - velocity[i+1]) > 0.2):
            end_index = i + 1
            break
    
    return df.iloc[begin_index:end_index]

file_name = "mechanics..lab..2..terminal.csv"
df = pd.read_csv(file_name)

for i in range(1, 11):
    time = f"Time (s) Run #{i}"
    position = f"Position (m) Run #{i}"
    velocity_inst = f"Velocity (m/s) Run #{i}"
    accelration_inst = f"Acceleration (m/s²) Run #{i}"   

    if all(column in df.columns for column in [time, position, velocity_inst, accelration_inst]):
        cleaned_data = extract_runtime(df, velocity_inst)   
        output_file = f"filtered_run_single{i}.csv"
        cleaned_data[[time, position, velocity_inst, accelration_inst]].to_csv(output_file, index=False)
        print(f"Saved: {output_file}")    