#Edulito practice exams 2 1CP2/02 Q05b

weight=[["Sophia",73,72,69,67,65,65],
        ["Alex",94,91,88,90,88,87],
        ["Kayla",69,68,67,65,62,61],
        ["Logan",75,75,74,73,74,73],
        ["Priya",68,68,65,66,65,65]]

for person in weight:
    lost_weight = person[1] - person[6]

    if lost_weight > 4:
        print(f"{person[0]} : {lost_weight}kg lost")
    

