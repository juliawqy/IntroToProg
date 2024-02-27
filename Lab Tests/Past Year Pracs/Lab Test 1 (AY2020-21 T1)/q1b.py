# Name:
# Email ID:

def is_compatible(patient_group, donor_group):
    # Replace the code below with your implementation.

    if donor_group == "AB":
        yes_compatible = True
    elif donor_group == "O":
        if patient_group == "O":
            yes_compatible = True
        else:
            yes_compatible = False
    elif donor_group == "A":
        if patient_group == "A" or patient_group == "O":
            yes_compatible = True
        else:
            yes_compatible = False
    elif donor_group == "B":
        if patient_group == "B" or patient_group == "O":
            yes_compatible = True
        else:
            yes_compatible = False

    return yes_compatible
