import mne
import os
import os.path as op
import numpy as np
#from function import events_bottom

#Pilot 6

subjects = ['W959'] 

date = ['230524']

rounds = [1, 2, 3, 4, 5]   

rounds_name = ['passive', 'active1', 'active2', 'active3', 'active4']

trial_type = ['sound_CS_R', 'sound_CS_N', 'sound_CS', 'pict_CS_R', 'pict_CS_N', 'pict_CS', 'comb_CS_R', 'comb_CS_N', 'comb_CS' ]


data_path_raw = '/net/server/data/Archive/piansrann/meg'
raw_name = '{0}/{1}/RAW/{0}_run{2}_raw.fif'
data_path_events = '/net/server/data/Archive/piansrann/data_processing/pilot6_electrostim_W959/events'
name_events = '{0}_{1}_{2}.txt' 

for idx, subj in enumerate(subjects):
    for rn, r in enumerate(rounds):
    
        for t in trial_type:

                

            
            
                # для чтения файлов с events используйте либо np.loadtxt либо read_events либо read_events_N
                trial_type_event = np.loadtxt(op.join(data_path_events, name_events.format(rounds_name[rn], subj,  t)), dtype='int')
                print('trial_type_event %s' % len(trial_type_event))
                #print(type(trial_type_event))
                # Load data
                if len(trial_type_event) != 0:
                    raw_fname = op.join(data_path_raw, raw_name.format(subj, date[idx], r))
                    


                    raw = mne.io.Raw(raw_fname, preload=True)

                    events_raw = mne.find_events(raw, stim_channel='STI101', shortest_event=1, mask=None)
                    print('raw events %s' %len(events_raw))
                    #print(type(events_raw))
                                

                         
                    #events_bottom = events_bottom(events_raw, trial_type_event)
                    # Находим индексы ивентов конкретного события в общем списке меток
                    x = []
                    for i in range(len(events_raw)):
	                    for j in range(len(trial_type_event)):
		                    if np.all((events_raw[i] - trial_type_event[j] == 0)):
			                    x+=[i]
                    #print(x)
                    x1 = [16, 32, 64]

                    full_ev = []
                    for i in x:
                        full_ev += [list(events_raw[i])] # список из 3ех значений время х 0 х метка
                        j = i + 1
                        ok = True      
                        while ok:
                            full_ev += [list(events_raw[j])]
                            if events_raw[j][2] in x1:
                                ok = False
                            j += 1 
                    #print(full_ev)

                                
                    event_bottom = []

                    for i in full_ev:
                        if i[2] in x1:
                            event_bottom.append(i)                    
                    
                    event_bottom = np.array(event_bottom)
                    np.savetxt("/net/server/data/Archive/piansrann/data_processing/pilot6_electrostim_W959/events_bottom/{0}_{1}_{2}_bottom.txt".format(rounds_name[rn], subj, t), event_bottom, fmt="%s")
                    
                else:
                    print('zero')


                    

                    
                    
