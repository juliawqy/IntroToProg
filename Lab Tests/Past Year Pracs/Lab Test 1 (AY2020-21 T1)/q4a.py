# Name:
# Email ID:




def trace_contacts(patient, history):
    # Replace the code below with your implementation.

    list_infected_w_days = []
    list_infected = []

    for history_list in history:
        for n in range(-5,0):
            if patient in history_list and history_list[2] >= n:
                if history_list[0] == patient and history_list[1] not in list_infected:
                    list_infected_w_days = list_infected_w_days + [(history_list[1], history_list[2])]
                    list_infected = list_infected + [history_list[1]]
                elif history_list[1] == patient and history_list[0] not in list_infected:
                    list_infected_w_days = list_infected_w_days + [(history_list[0], history_list[2])]
                    list_infected = list_infected + [history_list[0]]

    first_list_infected = []

    for n in range(len(history)*len(history)):
        if list_infected != first_list_infected:
            first_list_infected = list_infected
            for index_infected in range(len(list_infected_w_days)):
                day_0 = list_infected_w_days[index_infected][1]
                for history_list in history:
                    for n in range(day_0+2,0):
                        if patient in history_list:
                            continue
                        elif list_infected_w_days[index_infected][0] in history_list and history_list[2] >= n:
                            if history_list[0] == list_infected_w_days[index_infected][0] and history_list[1] not in list_infected:
                                list_infected_w_days = list_infected_w_days + [(history_list[1], history_list[2])]
                                list_infected = list_infected + [history_list[1]]
                            elif history_list[1] == list_infected_w_days[index_infected][0] and history_list[0] not in list_infected:
                                list_infected_w_days = list_infected_w_days + [(history_list[0], history_list[2])]
                                list_infected = list_infected + [history_list[0]]

        else:
            break



        
            
    return list_infected



        