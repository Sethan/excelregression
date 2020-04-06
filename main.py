import numpy as np
import pandas as pd

df=pd.read_excel(open('sfhregression2_file_Renovation.xlsx', 'rb'),sheet_name='Default')

a=df.to_numpy()
array=a[4:,2:]
total_row_counter=0
print(array.shape)
for row in array.T:
    points = []
    distances = []
    last=np.nan
    distance=1
    flag=True
    top_down=0
    row=np.append(row,np.nan)
    for cell in row:
        if np.isnan(cell) and not np.isnan(last):
            if flag:
                flag=False
                points.append(last)
                distances.append(distance+1)
                distance=1
            else:
                distance+=1
        else:
            last=cell
            flag=True
            top_down+=1
    insert=np.round(np.linspace(points[0],points[1],distances[1]),2)
    row[top_down-2:top_down-2+distances[1]]=insert
    insert=np.round(np.linspace(points[1],points[2],distances[2]+1),2)
    row[top_down+distances[1]-3:top_down+distances[1]+distances[2]-2]=insert
    row[top_down+distances[1]+distances[2]-2:]=last
    array[:,total_row_counter]=row[:-1]
    total_row_counter+=1
    print(row)
    break
"""    
a[4:,2:]=array
returnFrame = pd.DataFrame(data=a, index=df.index, columns=df.columns)
returnFrame.to_excel('out.xlsx', sheet_name='default', index = False)
"""   