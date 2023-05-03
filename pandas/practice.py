import pandas as pd
ipl18 = pd.DataFrame({'Team': ['SRH', 'CSK', 'KKR', 'RR', 'MI', 'RCB', 'KXIP', 'DD'],
                         'Matches': [14, 14, 14, 14, 14, 14, 14, 14],
                         'Won': [9, 9, 8, 7, 6, 6, 6, 5],
                         'Lost': [5, 5, 6, 7, 8, 8, 8, 9],
                         'Tied': [0, 0, 0, 0, 0, 0, 0, 0],
                         'N/R': [0, 0, 0, 0, 0, 0, 0, 0],
                         'NRR': [0.284, 0.253, -0.070, -0.250, 0.317, 0.129, -0.502, -0.222],
                         'For': [2230, 2488, 2363, 2130, 2380, 2322, 2210, 2297],
                         'Against': [2193, 2433, 2425, 2141, 2282, 2383, 2259, 2304]},
                         index = range(1,9)
                    )
ipl17 = pd.DataFrame({'Team': ['MI', 'RPS', 'SRH', 'KKR', 'KXIP', 'DD', 'GL', 'RCB'],
                         'Matches': [14, 14, 14, 14, 14, 14, 14, 14],
                         'Won': [10, 9, 8, 8, 7, 6, 4, 3],
                         'Lost': [4, 5, 5, 6, 7, 8, 10, 10],
                         'Tied': [0, 0, 0, 0, 0, 0, 0, 0],
                         'N/R': [0, 0, 1, 0, 0, 0, 0, 1],
                         'NRR': [0.784, 0.176, 0.469, 0.641, 0.123, -0.512, -0.412, -1.299],
                         'For': [2407, 2180, 2221, 2329, 2207, 2219, 2406, 1845],
                         'Against': [2242, 2165, 2118, 2300, 2229, 2255, 2472, 2033]},
                         index = range(1,9)
                    )
print(ipl18)
print(ipl18.loc[(ipl18.NRR>0) & (ipl18.For > ipl18.Against),])