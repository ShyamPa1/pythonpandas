import numpy as np
import pandas as pd

# Defining the three dataframes indicating the gold, silver, and bronze medal counts
# of different countries
gold = pd.DataFrame({'Country': ['USA', 'France', 'Russia'],
                         'Medals': [15, 13, 9]}
                    )
silver = pd.DataFrame({'Country': ['USA', 'Germany', 'Russia'],
                        'Medals': [29, 20, 16]}
                    )
bronze = pd.DataFrame({'Country': ['France', 'USA', 'UK'],
                        'Medals': [40, 28, 27]}
                    )

Total = gold.add(silver,fill_value = 0).add(bronze,fill_value = 0)
Total.sort_values('Medals',ascending = True)
print(Total)