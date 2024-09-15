import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

result_df=pd.read_csv("candidate_result.csv")
# placement_df
result_df_required=result_df.drop("sl_no",axis=1)
# placement_df_required
