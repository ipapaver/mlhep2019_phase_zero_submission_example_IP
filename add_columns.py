#!/usr/bin/python
import pandas as pd
import numpy as np

df = np.loadtxt('./data.data')
df_data = pd.DataFrame(df, columns=('A', 'B'))
df_data['add_A_B'] = df_data['A']+df_data['B']
np.savetxt('./sum_A_B.data', np.array(df_data['add_A_B']))
