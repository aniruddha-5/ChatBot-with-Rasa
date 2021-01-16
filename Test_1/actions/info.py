
#Copy this file in the actions folder of your rasa initialization and use the below code to get the coordinates of event event_name.
'''
import info    #add this line to the top of your file
(x_coord,y_coord)=info.info("event_name")  #use this to get the coordinates and then use x_coord,y_coord in the file.
'''
## below are the event names, make sure you use it exactly like mentioned below
'''
"arduinos_trial"
"circuital_dilemma"
"fizzbuzz"
"hackoverflow"
"pandoras_box_ctf"
"unite_for_unity"
"frame_the_crane"
"cool_your_engine"
"fiducia"
"take_charge"
"chit_chat_with_chat_bot"
"pythonize_everything"
"ar_and_vr"
"iceev_hybrid"
"cyber_expert"
'''
###DO NOT change or use any part of the code below. Doing so might get you disqualified.

 
import random
def info(a):
    cords={}
    mapp={"arduinos_trial":"Event_0001",
        "circuital_dilemma":"Event_0002",
        "fizzbuzz":"Event_0003",
        "hackoverflow":"Event_0004",
        "pandoras_box_ctf":"Event_0005",
        "unite_for_unity":"Event_0006",
        "frame_the_crane":"Event_0007",
        "cool_your_engine":"Event_0008",
        "fiducia":"Event_0009",
        "take_charge":"Event_0010",
        "chit_chat_with_chat_bot":"Event_0011",
        "pythonize_everything":"Event_0012",
        "ar_and_vr":"Event_0013",
        "iceev_hybrid":"Event_0014",
        "cyber_expert":"Event_0015",

        }
    generic="Event_"
    b=[]
    random.seed(134567)
    ##for those nerds who might want to hardcode the SEED will be changed before evaluation so make your code generic
    for i in range(1,16):
        for j in range(1,16):
            b.append(generic + str(10000+(i-1)+(j-1)*10 +1)[1:]) 
    random.shuffle(b)
    for i in range(1,16):
        for j in range(1,16):
            cords[b[(i-1)+(j-1)*10]] = (i,j)
    try:
       return(cords[mapp[a]])
    except :
        return((-1,-1))