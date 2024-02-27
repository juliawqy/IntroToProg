# Name:
# Email ID:

import q3a

def swap_members(team1, team2):
    # Replace the code below with your implementation.

    global q3a


    for num_members1 in range(5):
        for num_members2 in range(5):

            new_team_1 = team1[:num_members1] + [team2[num_members2]] + team1[num_members1+1:]
            new_team_2 = team2[:num_members2] + [team1[num_members1]] + team2[num_members1+1:]
            

            if q3a.check_diversity(new_team_1) == True and q3a.check_diversity(new_team_2) == True:
                return (team1[num_members1][0], team2[num_members2][0])

    return None
            