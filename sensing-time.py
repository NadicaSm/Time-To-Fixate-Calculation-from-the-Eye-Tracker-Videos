#%%
from bs4 import ResultSet
import pandas as pd
import numpy as np
import torch
import cv2
from tqdm import tqdm

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
user_id = 'user_1'
N_FRAMES = 650
fps = 50

#%% Import eye-tracker data
data = pd.read_csv('data/' + user_id + '/' + user_id + '_raw.csv',delimiter = ';')

scene_data = data[data['SUBTASK_NUMBER'] == 2]
scene_data = scene_data[scene_data['SUBTASK_ACTION'] == 2]

tx, ty = scene_data['T-GP_X'], scene_data['T-GP_Y']
tx = np.array(tx)
ty = np.array(ty)
#%%
flag = 0 
for frame in tqdm(range(0,N_FRAMES)):

    PATH = 'video/' + user_id + '/' + user_id + 'Frame' + str(frame) + '.jpg'
    img = cv2.imread(PATH)  
    
    results = model(img)
    labels, cord_thres = results.xyxyn[0][:, -1].numpy(), results.xyxyn[0][:, :-1].numpy() 

    # Check if the person is in labels
    if (0 in labels):
        
        cords_p = cord_thres[labels == 0, :][0]

        # Check if the person and bus are in labels
        if list(labels) == [0,2]:
            cords_b = cord_thres[labels == 2, :][0]
        else: cords_b = [0,0,0,0]

        # Get the bounding box coordinates
        xmin, ymin, xmax, ymax = cords_p[0], cords_p[1], cords_p[2], cords_p[3]
        
        if np.isnan(tx[2*frame]):
            tx[2*frame] = tx[2*frame - 1]
            ty[2*frame] = ty[2*frame - 1]

        # Check if the person is in front of the bus
        if  (xmax < cords_b[2]) and (ymax > cords_b[3]) and (flag == 0):
            start_frame = frame
            flag = 1
            
        # Check if the gaze is within the bounding box of detected object
        if (xmin < tx[2*frame] < xmax) and (ymin < ty[2*frame] < ymax) and (flag == 1): 
            end_frame = frame
            flag = 2

        if flag == 2:
            break;

#%% Calculate ST
sensing_time = (end_frame - start_frame)*1000/fps # in ms
print(sensing_time)

# %%
