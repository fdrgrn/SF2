#np.where() is a function that returns a list of all indices where condition is met
import pandas as pd
import numpy as np

def extract_runtime(df, velocity_inst):
    velocity = df[velocity_inst].fillna(0).to_numpy()
    
    #identify starting index by finding beginning hold (first point where the difference in velocity with neighbors is minimal)
    difference = np.abs(np.diff(velocity))
    begin_index  = np.where(difference < 0.02)[0][0]
    
    for i in range(begin_index, len(velocity) - 1):
        #we can presume we've reached the end when the change in velocity is great between neighbors and the sign of the velocity between neighbors are opposing (-) -> (+)
        if (np.sign(velocity[i]) != np.sign(velocity[i+1])) and (abs(velocity[i] - velocity[i+1]) > 0.2):
            end_index = i + 1
            break
    
    return df.iloc[begin_index:end_index]

file_name = "mechanics_lab1.csv"
df = pd.read_csv(file_name)

for i in range(1, 11):
    #columnn header for our cleaned files
    time = f"Time (s) Run #{i}"
    position = f"Position (m) Run #{i}"
    velocity_inst = f"Velocity (m/s) Run #{i}"
    accelration_inst = f"Acceleration (m/s²) Run #{i}"   

    #if all() assures all conditions are met before running subsequent lines, allows to skip if provlem (like with #6)
    if all(column in df.columns for column in [time, position, velocity_inst, accelration_inst]):
        cleaned_data = extract_runtime(df, velocity_inst)   
        output_file = f"filtered_run_multiples{i}.csv"
        cleaned_data[[time, position, velocity_inst, accelration_inst]].to_csv(output_file, index=False)
        print(f"Saved: {output_file}")    