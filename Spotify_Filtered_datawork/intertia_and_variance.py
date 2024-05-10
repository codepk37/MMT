import csv
import ast
import numpy as np

# Function to read CSV file and store data in a dictionary
def read_csv_file(file_path):
    track_dict = {}
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            track_name = row['trackName']
            audio_features = row['audio_features']
            track_dict[track_name] = audio_features
    return track_dict

# Provide the file path
file_path = "final_audio_features.csv"

# Call the function to read the CSV file and store data in a dictionary
track_dict = read_csv_file(file_path)

# Function to print audio features for a given track name
def print_audio_features(track_name, track_dict):
    if track_name in track_dict:
        audio_features_str = track_dict[track_name]
        if len(audio_features_str)==0:
            return 0
        audio_features_dict = ast.literal_eval(audio_features_str)  # Parse string to dictionary
        return audio_features_dict
    else:
        return 0  # Return None if track not found

# Provide the track name you want to search for
track_name_to_find = "Watermelon Sugar"

# Call the function with the track name and dictionary of track data
ans = print_audio_features(track_name_to_find, track_dict)
print(ans['danceability'])



#######################################################

from datetime import datetime



import os



# Function to calculate autocorrelation for a given list
def calculate_autocorrelation(data):
    if np.std(data) * len(data) == 0:
        return [0]
    else :
        return np.correlate(data[:-1], data[1:]) / (np.std(data) * len(data))



def list_folders_relative_to_script():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # print("script dir ",script_dir)
    # Get a list of all items (files and directories) in the script directory
    items = os.listdir(script_dir)
    # Iterate through each item
    for item in items:
        # Check if the item is a directory
        if os.path.isdir(os.path.join(script_dir, item)):
            # If it is a directory, print its name
            # print(item)
            if(item[0]!='p'):
                continue

            script_dirn=script_dir+f"\\{item}"
            # print(script_dirn) ****
            
                        
            import json

            session_track_dict={}
           

            with open(item+"\modified_data.json", 'r',encoding='utf-8') as file:
                    data = json.load(file)

                    # Print the data
                    # print(len(data))
                    last_sess= data[-1].get("sessionumber")
                    # print("last session  ",last_sess)


                    for i in range(last_sess):
                        session_track_dict[i+1]=[]                    

                    
                    for entry in data:                                          
                        session_track_dict[entry.get("sessionumber")].append(entry.get("trackName"))                           
                        
                    
            
            dynamic_sess_danceability={}    

            list_danceability=[]
            list_energy=[]
            list_loudness=[]
            list_mode=[]
            list_speechiness=[]
            list_acousticness=[]
            list_instrumentalness=[]
            list_liveness=[]
            list_valence=[]
            list_tempo=[]


            tot_2=0
            ri_user_statictillnow=0
            print(   item   ,"      ",len(session_track_dict))
           
            for ele in session_track_dict: #each session at time
               

                danceability=0
                energy=0
                loudness=0
                mode=0
                speechiness=0
                acousticness=0
                instrumentalness=0
                liveness=0
                valence=0
                tempo=0
                

                tracks=(session_track_dict[ele]) #get unique tracks

                empty_data=0   #count of songs: data for song not exist
                for track in tracks:#track in tracks
                    
                    # print(track)
                    ans= print_audio_features(track, track_dict) #Data absent
                    if(ans==0):
                        empty_data+=1
                        danceability+=0  #data for song not exist
                        energy+=0
                        loudness+=0
                        mode+=0
                        speechiness+=0
                        acousticness+=0
                        instrumentalness+=0
                        liveness+=0
                        valence+=0
                        tempo+=0

                    else:
                        danceability+=ans['danceability']
                        energy+=ans['energy']
                        loudness+=ans['loudness']
                        mode+=ans['mode']
                        speechiness+=ans['speechiness']
                        acousticness+=ans['acousticness']
                        instrumentalness+=ans['instrumentalness']
                        liveness+=ans['liveness']
                        valence+=ans['valence']
                        tempo+=ans['tempo']

                if(danceability!=0):
                    danceability/= len(tracks)-empty_data
                if(energy!=0):
                    energy/= len(tracks)-empty_data
                if( loudness!=0):
                    loudness/= len(tracks)-empty_data
                if( mode!=0):
                    mode/= len(tracks)-empty_data
                if( speechiness!=0):
                    speechiness/= len(tracks)-empty_data
                if( acousticness!=0):
                    acousticness/= len(tracks)-empty_data
                if( instrumentalness!=0):
                    instrumentalness/= len(tracks)-empty_data
                if( liveness!=0):
                    liveness/= len(tracks)-empty_data
                if( valence!=0):
                    valence/= len(tracks)-empty_data
                if( tempo!=0):
                    tempo/= len(tracks)-empty_data


                
                dynamic_sess_danceability[f"dance_{ele}"]=danceability #sessionwise average
                dynamic_sess_danceability[f"energy_{ele}"]=energy
                dynamic_sess_danceability[f"loudness_{ele}"]=loudness
                dynamic_sess_danceability[f"mode_{ele}"]=mode
                dynamic_sess_danceability[f"speechi_{ele}"]=speechiness
                dynamic_sess_danceability[f"acoustic_{ele}"]=acousticness
                dynamic_sess_danceability[f"instrumental_{ele}"]=instrumentalness
                dynamic_sess_danceability[f"liveness_{ele}"]=liveness
                dynamic_sess_danceability[f"valence_{ele}"]=valence
                dynamic_sess_danceability[f"tempo_{ele}"]=tempo


                list_danceability.append(danceability)
                list_energy.append(energy)
                list_loudness.append(loudness)
                list_mode.append(mode)
                list_speechiness.append(speechiness)
                list_acousticness.append(acousticness)
                list_instrumentalness.append(instrumentalness)
                list_liveness.append(liveness)
                list_valence.append(valence)
                list_tempo.append(tempo)


                # print(len(tracks))
                #



            ###### Jatin varinace of dynamic ri
            
            # Exclude the last item from the dataset
        
            dict_vara_autocorr={}



            dict_vara_autocorr["dance_vara"]=np.std(list_danceability)
            dict_vara_autocorr["energy_vara"]=np.std(list_energy)
            dict_vara_autocorr["loudness_vara"]=np.std(list_loudness)
            dict_vara_autocorr["mode_vara"]=np.std(list_mode)
            dict_vara_autocorr["speechiness_vara"]=np.std(list_speechiness)
            dict_vara_autocorr["acoustic_vara"]=np.std(list_acousticness)
            dict_vara_autocorr["instrument_vara"]=np.std(list_instrumentalness)
            dict_vara_autocorr["liveness_vara"]=np.std(list_liveness)
            dict_vara_autocorr["valence_vara"]=np.std(list_valence)
            dict_vara_autocorr["tempo_vara"]=np.std(list_tempo)




            dict_vara_autocorr["dance_autocorr"]= calculate_autocorrelation(list_danceability)[0]
            dict_vara_autocorr["energy_autocorr"]=calculate_autocorrelation(list_energy)[0]
            dict_vara_autocorr["loudness_autocorr"]=calculate_autocorrelation(list_loudness)[0]
            dict_vara_autocorr["mode_autocorr"]=calculate_autocorrelation(list_mode)[0]
            dict_vara_autocorr["speechiness_autocorr"]=calculate_autocorrelation(list_speechiness)[0]
            dict_vara_autocorr["acoustic_autocorr"]=calculate_autocorrelation(list_acousticness)[0]
            dict_vara_autocorr["instrument_autocorr"]=calculate_autocorrelation(list_instrumentalness)[0]
            dict_vara_autocorr["liveness_autocorr"]=calculate_autocorrelation(list_liveness)[0]
            dict_vara_autocorr["valence_autocorr"]=calculate_autocorrelation(list_valence)[0]
            dict_vara_autocorr["tempo_autocorr"]=calculate_autocorrelation(list_tempo)[0]

          

            #UNCOMMET TO USE AVG DANCEABILITY,... PER SESSION, NOT USEFUL RIGHT NOW=> EXTRACTED IMP INFO BEYHTE WAY UP
            with open(item+"\\dance__.json", 'w', encoding='utf-8') as file:
                json.dump(dynamic_sess_danceability, file, indent=2)

            # with open(item+"\\dance.json", 'w', encoding='utf-8') as file:
            #     json.dump(dict_vara_autocorr, file, indent=2)








# Call the function to list folders relative to the script directory
list_folders_relative_to_script()


# print(list_tempo)