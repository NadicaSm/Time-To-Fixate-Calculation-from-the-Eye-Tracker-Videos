#%%
import numpy as np 
import seaborn as sb
import pandas as pd


user_id = 'user_1'
index = 174

data = pd.read_csv('data/' + user_id + '/' + user_id + '_raw.csv',delimiter = ';')

begin_time = np.loadtxt('video/' + user_id + '/' + user_id + '.txt', dtype = int)
scene_data = data[data['SUBTASK_NUMBER'] == 2]
scene_data = scene_data[scene_data['SUBTASK_ACTION'] == 2]
scene_begin_time = (scene_data.iloc[0,0] - begin_time) / 1000
scene_end_time = (scene_data.iloc[-1,0] - begin_time) / 1000
diff = scene_end_time - scene_begin_time



#%%

speed = scene_data['SPEED'].iloc[index]
x1 = scene_data['POSITION_X'].iloc[index]
y1 = scene_data['POSITION_Y'].iloc[index]
z1 = scene_data['POSITION_Z'].iloc[index]


x2 = scene_data['COLLISION_LOCATION_X_1'].iloc[index]
y2 = scene_data['COLLISION_LOCATION_Y_1'].iloc[index]
z2 = scene_data['COLLISION_LOCATION_Z_1'].iloc[index]
distance = np.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
ttl = distance/speed

print(speed*3.6) # in kmh
print(distance)
print(ttl)

#%%
d = {
    'id': [1,2,3,5,6,7,8,10,13,14,16,17,21,23,26,27,34,38,39,40,41,42,43,44,45,46,48,51,54,56,57,60,61,62,64,66,67,68,71,72,75,78,79,881,82,85,86,88,98,100,102,106,107],
    'ST': [140, 360, 320, 440, 160, 300, 300, 460, 220, 200, 160, 440, 320, 400, 220, 140, 260, 280, 220, 260, 160, 140, 180, 380, 120, 200, 140, 240, 140, 120, 400, 220, 180, 140, 120, 360, 240, 280, 320, 260, 200, 140, 380, 120, 240, 120, 280, 160, 100, 140, 200, 160, 160],
    'gaze2object_distance': [165,53,42,261,46,25,66,27,40,52,92,69,56,63,22,21,39,31,58,61,32,137,9,35,59,36,27,35,26,26,34,39,232,10,23,30,67,74,87,43,18,39,33,121,39,242,6,56,60,22,47,18,62],
    'fitness': ['fit','unfit','unfit','unfit','fit','cond fit','cond fit','cond fit','unfit', 'fit', 'cond fit', 'unfit', 'cond fit', 'cond fit', 'unfit', 'fit', 'unfit', 'cond fit', 'unfit','unfit','fit','fit','fit','cond fit','fit','fit','cond fit','unfit','fit','unfit','cond fit','fit','fit','unfit','fit','unfit','unfit','cond fit','fit','unfit','cond fit','fit','unfit','fit','unfit','fit','cond fit','unfit','unfit','fit','cond fit','fit','fit'],
    'velocity': [13.2,18.9,np.nan,3.3,15.4,32.5,np.nan,31.7,12.2,14.2,10.3,np.nan,8.1,7.5,20.0,14.6,13.8,np.nan,41.1,24.4,7.4,21.3,30.5,27.8,11.4,5.5,19.5,np.nan,9.6,15.3,33.5,46.9,25.1,11.0,14.5],
    'ttl' : [3.3,2.4,np.nan,19.6,2.3,0.7,np.nan,0.5,4.7,3.4,5.4,np.nan,8.8,9.6,3.2,3.2,6.8,np.nan,1.1,0.7,6.8,3.7,0.8,0.8,5.3,6.8,2.3,np.nan,6.9,3.4,0.9,0.8,2.2,4.1,2.7]
           
}

df = pd.DataFrame(data = d)
df.to_csv('parameter_table.csv')
