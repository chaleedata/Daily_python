#create calendar list
(2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm

#You must to merge range
[(2, 3) ,(6, 9)] #this sample condition 

#If overlap
[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#it return
[(0, 1), (3, 8), (9, 12)]

#Look by step 

# Sort by start time
def merge_range(meeting):

    #sort by time 
    sorted_meetings = sorted(meetings) 

    #choose earliest meeting
    merged_meetings = [sorted_meetings[0]]

    #create for loop  write condition 
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        #if current meeting overlaps with last use later end time
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                    max(last_merged_meeting_end,
                                        current_meeting_end)) 
        
        else:
            merged_meetings.append((current_meeting_start,current_meeting_end))
    
    return merged_meetings                                                          )


