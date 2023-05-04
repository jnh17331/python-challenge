# Imports dependencies
import csv
import os

# Sets each resource spreadsheet path as a variable that can be called
bank = os.path.join('Resources', 'budget_data.csv')
poll =  os.path.join('Resources', 'election_data.csv')

# Sets output file path and creates text file
analysisoutput = os.path.join("Analysis.txt")

# Initialize our variables
TotalMonths = 0
PLtotal = 0
AvgChange = 0
PrevPL = 0
MonthlyChange = {'Month: ':[], 'P/L: ' : []}
monthly_changes = []

TotalVotes = 0
Charles = 0
Diana = 0
Raymon = 0
Winner = ''

# Opens the budget file and reads from it
with open(bank) as bankfile:
    
    bankreader = csv.DictReader(bankfile, delimiter=",")

    # Goes through each row of the csv with a for loop
    for row in bankreader:

        # Adds a total month for each row
        TotalMonths += 1

        # Gets the value of the current Profit/Loss amount while on that row
        PLchange = int(row['Profit/Losses'])

        # Gets date of the trow
        CurrentMonth = row['Date']

        # Adds to the total Profit/Loss variable
        PLtotal = PLtotal + int(PLchange)

        #Adds the values of the month and profit/loss to the dict.
        MonthlyChange['Month: '].append(CurrentMonth)
        MonthlyChange['P/L: '].append(PLchange)
  
        # Checks the amount of change per row and adds changes to a list
        if PrevPL != 0:
            monthly_change = PLchange - PrevPL
            monthly_changes.append(monthly_change)

        PrevPL = PLchange
    
# Gets the total of the change per month list and divides it by the length of the list
if monthly_changes:
    AvgChange = sum(monthly_changes) / len(monthly_changes)

# Gets the highest and lowest amounts in the monthly changes
GreatestIncrease = max(monthly_changes)
GreatestDecrease = min(monthly_changes)


# Gets the month for each of the greatest increases and decreases each month
max_increase_index = monthly_changes.index(GreatestIncrease)
GreatestIncMonth = MonthlyChange['Month: ' ][max_increase_index + 1]

max_decrease_index = monthly_changes.index(GreatestDecrease)
GreatestDecMonth = MonthlyChange['Month: ' ][max_decrease_index + 1]


# Opens the election cvs to read from it
with open(poll) as pollfile:

    pollreader = csv.DictReader(pollfile, delimiter=',')

    # Loops through the cvs and counts each time a candidate is elected
    for row in pollreader:
        TotalVotes += 1
        if row['Candidate'] == 'Charles Casper Stockham':
            Charles += 1
        elif row['Candidate'] == 'Diana DeGette':
            Diana += 1
        elif row['Candidate'] == 'Raymon Anthony Doane':
            Raymon += 1
            
# Gets the percent of the votes for each candidate
CharlesPercent = Charles/TotalVotes * 100
DianaPercent = Diana/TotalVotes * 100
RaymonPercent = Raymon/TotalVotes * 100

# Checks for the winner by looking for the highest amount of votes
if Diana > Charles:
    Winner = 'Diana DeGette'
elif Diana > Raymon:
    Winner = 'Diana DeGette'
elif Charles > Diana:
    Winer = 'Charles Casper Stockham'
elif Charles > Raymon:
    Winner - 'Charles Casper Stockham'
elif Raymon > Diana:
    Winner = 'Raymon Anthony Doane'
elif Raymon > Charles:
    Winner = 'Raymon Anthony Doane'
else:
    Winner = 'Tie'




# Writes out our analysis to a txt file
with open(analysisoutput, 'w') as analysis:

    # Initialize csv.writer
    analysiswriter = csv.writer(analysis, delimiter=',')

    # Writes title for our bank analysis
    analysiswriter.writerow(['Fiancial Analysis'])
    analysiswriter.writerow(['-----------------------------------------'])

    # Writes bank analysis data to txt file
    analysiswriter.writerow([f'Total Months: {TotalMonths}'])
    analysiswriter.writerow([f'Total: ${PLtotal:.2f}'])
    analysiswriter.writerow([f'Average Change: ${AvgChange:.2f}'])
    analysiswriter.writerow([f'Greatest Increase: {GreatestIncMonth} ${GreatestIncrease:.2f}'])
    analysiswriter.writerow([f'Greatest Decrease: {GreatestDecMonth} ${GreatestDecrease:.2f}'])

    analysiswriter.writerow([' '])
    analysiswriter.writerow([' '])

    # Writes out the poll results
    analysiswriter.writerow(['Election Results'])
    analysiswriter.writerow(['-----------------------------------------'])
    analysiswriter.writerow([f'Total Votes: {TotalVotes}'])
    analysiswriter.writerow(['-----------------------------------------'])
    analysiswriter.writerow([f'Charles Casper Stockham: {Charles} ({CharlesPercent:.2f}%)'])
    analysiswriter.writerow([f'Diana DeGette: {Diana} ({DianaPercent:.2f}%)'])
    analysiswriter.writerow([f'Raymon Anthony Doane: {Raymon} ({RaymonPercent:.2f}%)'])
    analysiswriter.writerow(['-----------------------------------------'])
    analysiswriter.writerow([f'Winner: {Winner}'])
    analysiswriter.writerow(['-----------------------------------------'])

# Prints out all of our results to the console
print('Fiancial Analysis')
print('-----------------------------------------')
print(f'Total Months: {TotalMonths}')
print(f'Total: ${PLtotal:.2f}')
print(f'Average Change: ${AvgChange:.2f}')
print(f'Greatest Increase: {GreatestIncMonth} ${GreatestIncrease:.2f}')
print(f'Greatest Decrease: {GreatestDecMonth} ${GreatestDecrease:.2f}')
print(' ')
print(' ')
print('Election Results')
print('-----------------------------------------')
print(f'Total Votes: {TotalVotes}')
print(f'Charles Casper Stockham: {Charles} ({CharlesPercent:.2f}%)')
print(f'Diana DeGette: {Diana} ({DianaPercent:.2f}%)')
print(f'Raymon Anthony Doane: {Raymon} ({RaymonPercent:.2f}%)')
print('-----------------------------------------')
print(f'Winner: {Winner}')
print('-----------------------------------------')



    