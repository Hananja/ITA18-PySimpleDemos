# Tagesnamen; Demonstration von elif


dow = 4 # Day Of Week

if dow == 1:
    day = "Sonntag"
else:
    if dow == 2:
        day = "Montag"
    else:
        if dow == 3:
            day = "Dienstag"
        else:
            if dow == 4:
                day = "Mittwoch"
            else:
                if dow == 5:
                    day = "Donnerstag"
                else:
                    if dow == 6:
                        day = "Freitag"
                    else:
                        if dow == 7:
                            day = "Samstag"
                        else:
                            day = None
print(day)



if dow == 1:
    day = "Sonntag"
elif dow == 2:
    day = "Montag"
elif dow == 3:
    day = "Dienstag"
elif dow == 4:
    day = "Mittwoch"
elif dow == 5:
    day = "Donnerstag"
elif dow == 6:
    dey = "Freitag"
elif dow == 7:
    day = "Samstag"
else:
    day = None
print(day)
