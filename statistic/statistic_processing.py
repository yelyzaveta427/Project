numbers = [10,11,12,13,14,15,16,17,18,19,20]
density = [0.05,0.1, 0.15, 0.2, 0.25]
with open("condensed_statistic_list.csv","w") as list_file,open("condensed_statistic_matrix.csv","w") as matrix_file:
    list_file.write(f"Density,10,11,12,13,14,15,16,17,18,19,20,\n")
    matrix_file.write(f"Density,10,11,12,13,14,15,16,17,18,19,20,\n")
    for denst in density:
        list_file.write(f"{denst},")
        matrix_file.write(f"{denst},")
        for number in numbers:
            list_time = 0
            matrix_time = 0
            with open(f"statistic_{number}_{denst}.csv","r") as stat_file:
                for line in stat_file.readlines():
                    list_time += float(line.split(",")[-3])
                    matrix_time += float(line.split(",")[-2])
            list_time /= 20
            matrix_time /= 20
            list_file.write(f"{list_time},")
            matrix_file.write(f"{matrix_time},")
        list_file.write("\n")
        matrix_file.write("\n")