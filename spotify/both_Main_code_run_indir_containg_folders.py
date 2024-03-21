from datetime import datetime

# datetime_string = "2021-09-18 15:50"
# datetime_object = datetime.strptime(datetime_string, "%Y-%m-%d %H:%M")
# seconds_since_epoch = datetime_object.timestamp()

# print(seconds_since_epoch)
# datetime_string = "2021-09-19 15:16"
# datetime_object = datetime.strptime(datetime_string, "%Y-%m-%d %H:%M")
# seconds_since_epoch = datetime_object.timestamp()
# print(seconds_since_epoch)

import os

def list_folders_relative_to_script():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print("script dir ",script_dir)
    # Get a list of all items (files and directories) in the script directory
    items = os.listdir(script_dir)
    # Iterate through each item
    for item in items:
        # Check if the item is a directory
        if os.path.isdir(os.path.join(script_dir, item)):
            # If it is a directory, print its name
            print(item)
            script_dirn=script_dir+f"\\{item}"
            # print(script_dirn) ****

            filename = []
            for x in os.listdir(script_dirn):
                if x.endswith(".json") and x[0].isdigit():
                    # Prints only text file present in My Folder
                    xx=item +"\\"+x
                    print(xx)
                    filename.append(xx) 
            
            import json
            lis=[]
            prev_time = 0
            session_num = 0

            for file_name in filename:
                # Read the JSON file
                with open(file_name, 'r',encoding='utf-8') as file:
                    data = json.load(file)

                    # Print the data
                    # print(data[0])
                    
                    for entry in data:
                        
                        tem={}
                        # print("End Time:", entry.get("endTime"))
                        # print("Artist Name:", entry.get("artistName"))
                        # print("Track Name:", entry.get("trackName"))
                        # print("Milliseconds Played:", entry.get("msPlayed"))
                        # print()

                        tem["endTime"] = entry.get("endTime")
                        tem["artistName"] =  entry.get("artistName")
                        tem["trackName"] = entry.get("trackName")
                        tem["msPlayed"] =entry.get("msPlayed")

                        endtime_string = entry.get("endTime") ####
                        endtime_object = datetime.strptime(endtime_string, "%Y-%m-%d %H:%M")
                        endsec = endtime_object.timestamp()
                        startsec= int(endsec- (entry.get("msPlayed")/1000))

                        # tem["startsec"]=startsec
                        # tem["endsec"]=endsec
                        # tem["time_p_sec"]= (endsec-startsec) # correct sec, gap_insec<7200

                        if startsec-prev_time > 7200:
                            session_num +=1
                        # print("   ",startsec-prev_time)
                        # tem["diff"]=startsec-prev_time
                        tem["sessionumber"]=session_num
                        prev_time = endsec

                        lis.append(tem)

            
            print("item ",item)
            with open(item+'\modified_data.json', 'w', encoding='utf-8') as file:
                json.dump(lis, file, indent=2)

            
                        
            import json

            session_track_dict={}

            inti_tot=0
            with open(item+"\modified_data.json", 'r',encoding='utf-8') as file:
                    data = json.load(file)

                    # Print the data
                    # print(data[0])
                    last_sess= data[-1].get("sessionumber")
                    print("last session  ",last_sess)

                    for i in range(last_sess):
                        session_track_dict[i+1]=[]
                    

                    
                    for entry in data:                       
                        inti_tot+=1
                        
                        session_track_dict[entry.get("sessionumber")].append(entry.get("trackName"))
                            
                        
                            
                        # tem={}-
                        # print("End Time:", entry.get("endTime"))
                        # print("Artist Name:", entry.get("artistName"))
                        # print("Track Name:", entry.get("trackName"))
                        # print("Milliseconds Played:", entry.get("msPlayed"))
                        # print()
                        # print("Track Name:", entry.get("trackName"))
                        # print("sessionumber", entry.get("sessionumber"))


            #** session_track_dict has [1:[all trackis in session],2:[all trackis in session 2]...

            
            ri_dict={}
            tot_2=0
            ri_user_statictillnow=0
            for ele in session_track_dict: #each session at time
                # tot_2+=len(session_track_dict[ele])

                curr_ri_numerator=0

                set_ele=list(set(session_track_dict[ele])) #get unique tracks

                # tot_2+=len(set_ele)

                for unique_ in set_ele:
                    a=session_track_dict[ele].count(unique_) 
                    if( a>=2):
                        curr_ri_numerator+=a #add its effect
                    else:
                        curr_ri_numerator+=0
                
                session_ri= curr_ri_numerator/len(session_track_dict[ele])

                ri_dict[ele]=format(session_ri, '.5f')#session_ri

                ri_user_statictillnow += session_ri

            ri_dict["ri_tillnow"]= ri_user_statictillnow/len(session_track_dict)



            # print("tot init ",inti_tot)
            # print("tot_2 ",tot_2)
            print(ri_dict)

            
            with open(item+"\\ri_sessionwise.json", 'w', encoding='utf-8') as file:
                json.dump(ri_dict, file, indent=2)








# Call the function to list folders relative to the script directory
list_folders_relative_to_script()
