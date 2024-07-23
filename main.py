import csv

def generato(date):
	file = open("group_template.csv", "a")
	query = f",,{date},\n"
	file.write(query)
	file.close()




# Emails list file 
file1 = open('emails_list.txt', 'r')
count = 0


file = open("group_template.csv", "a")
# new line
# Heder
file.write('First Name,Last Name,Email,Position\n')
file.close()



# Start code
while True:
    count += 1
  
    # Get next line from file
    line = file1.readline()
  
    # if line is empty
    # end of file is reached
    if not line:
        break

    date = line.strip()
    print(f"[! Debug add email: {date}")

    generato(date)
  
file1.close()