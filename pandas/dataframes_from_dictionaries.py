import pandas as pd
s_on=[1,2,3,4,5]
names=["shyam","pavan","satya","manikanta","kumar"]
education_from_childhood=["bapu","vani","betany","narayana","thirumala"]
student_data={"s_on":s_on,"names":names,"education":education_from_childhood}
student=pd.DataFrame(student_data,header=None)
print(student)