import csv
from operator import itemgetter

if __name__ == "__main__":
    
    l = []
    fieldnames = ["first_name", 'last_name', 'grade']
    
    with open("backup.csv", "r", encoding="utf-8", newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)

        # Build list from CSV
        for row in csv_reader:
            d = {
                'first_name' : row[0],
                'last_name' : row[1],
                'grade' : row[2]
            }
            l.append(d)
    
    # Sort list based on last_name DESC
    sorted_l = sorted(l, key=itemgetter('last_name'), reverse=True)

    # Write to new CSV
    with open("new_csv.csv", mode="w", newline="") as newfile:
        writer = csv.DictWriter(newfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_l)

    print("Successfully wrote data to new file")

         
            
        