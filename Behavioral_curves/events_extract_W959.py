import numpy as np
import mne
import os
import os.path as op

#Pilot 5

#subjects = ['W969'] 

#data = ['230503']


#subjects = ['W959', 'W967', 'W968'] 

#data = ['230517', '230516', '230512']

subjects = ['W959'] 

data = ['230524']

rounds = [1, 2, 3, 4, 5]
rounds_name = ['passive', 'active1', 'active2', 'active3', 'active4','active5']


marks = [2, 4, 6, 8, 10, 12, 130, 132, 134, 136, 138, 140]

data_path = '/net/server/data/Archive/piansrann/meg'

#stimulus = ['sound', 'sound_CS+', 'pict', 'pict_CS+' ]

for idx, subj in enumerate(subjects):
    for ir, r in enumerate(rounds):
        raw= mne.io.Raw(op.join(data_path, f'{subj}/{data[idx]}/RAW/{subj}_run{r}_raw.fif'), preload=True)

        events = mne.find_events(raw, stim_channel='STI101', shortest_event=1)
        events_clean = []
        for i in range(len(events)-1):
            if events[i][2] in marks:
                events_clean.append(list(events[i]))
                
        events_clean  = np.array(events_clean) 
        #подкрепляемых картинок нет!!! ни в одном раунде        
        sound_CS_R = []
        sound_CS_N = []
        sound_CS = []
        pict_CS_R = []
        pict_CS_N = []
        pict_CS = []
        comb_CS_R = []
        comb_CS_N = []
        comb_CS = []
        
        i=0
        #for i in range(len(events_clean)-2):
        while i <= (len(events_clean)-3):
        
            print(i)
            print(subj)
            print(r)
            if events_clean[i][2] == 2 and events_clean[i+2][2] == 2:
                sound_CS_N.append(list(events_clean[i]))
                i= i+3
                
            elif events_clean[i][2] == 2 and events_clean[i+2][2] == 130:
                sound_CS_R.append(list(events_clean[i]))
                i= i+3
                
            elif events_clean[i][2] == 2 and events_clean[i+2][2] not in [2, 130]:
                print(f'sound {r} has missing mark')
                i= i+2                   
                
            elif events_clean[i][2] == 8 and events_clean[i+2][2] == 8:
                sound_CS.append(list(events_clean[i]))
                i= i+3

            elif events_clean[i][2] == 4 and events_clean[i+2][2] == 4:
                pict_CS_N.append(list(events_clean[i]))
                i= i+3
                
            elif events_clean[i][2] == 4 and events_clean[i+2][2] == 132:
                pict_CS_R.append(list(events_clean[i]))
                i= i+3
            
            elif events_clean[i][2] == 4 and events_clean[i+2][2] not in [4, 132]:
                print(f'pict {r} has missing mark')
                i= i+2    
                
                
            elif events_clean[i][2] == 10:
                pict_CS.append(list(events_clean[i]))  
                i= i+3 
            elif events_clean[i][2] == 12 and events_clean[i+2][2] == 12:
                comb_CS_N.append(list(events_clean[i]))
                i= i+3
                
            elif events_clean[i][2] == 12 and events_clean[i+2][2] == 140:
                comb_CS_R.append(list(events_clean[i]))
                i= i+3

            elif events_clean[i][2] == 4 and events_clean[i+2][2] not in [12, 140]:
                print(f'comb {r} has missing mark')
                i= i+2   
                
            elif events_clean[i][2] == 6:
                comb_CS.append(list(events_clean[i]))  
                i= i+3
                
                     
                
                        
        sound_CS_R = np.array(sound_CS_R)
        sound_CS_N = np.array(sound_CS_N)
        sound_CS = np.array(sound_CS)
        pict_CS_R = np.array(pict_CS_R)
        pict_CS_N = np.array(pict_CS_N)
        pict_CS = np.array(pict_CS)  
        
        comb_CS_R = np.array(comb_CS_R)
        comb_CS_N = np.array(comb_CS_N)
        comb_CS = np.array(comb_CS)  
        
        
        events_list = [sound_CS_R, sound_CS_N, sound_CS, pict_CS_R, pict_CS_N, pict_CS, comb_CS_R, comb_CS_N, comb_CS]
        events_name = ['sound_CS_R', 'sound_CS_N', 'sound_CS', 'pict_CS_R', 'pict_CS_N', 'pict_CS', 'comb_CS_R', 'comb_CS_N', 'comb_CS']
        for ind, el in enumerate(events_list):
            np.savetxt(f"/net/server/data/Archive/piansrann/data_processing/pilot6_electrostim_W959/events/{rounds_name[ir]}_{subj}_{events_name[ind]}.txt", el, fmt="%s")                           





