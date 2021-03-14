import csv  # used to read csv

# used to plot and plot in real time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# finding how many stocks there are so how many need to be tracked
amount_of_graphs_needed = 0

# making all names for graphs None so I can override then check if none which will tell me if I need to add onto that graph
ax1 = None
ax2 = None
ax3 = None
ax4 = None


with open(r"PATH-TO-SPREADSHEET.csv") as r:
    read = csv.reader(r)
    headers = next(read)

    # finding how many stocks there are so how many need to be tracked
    for index, column_header in enumerate(headers):
        if index >= 2 and index % 2 == 0:  # if the index is >= 2 and its an even number it means it is the name of a stock in the csv
            amount_of_graphs_needed += 1


# setting up graph
plt.style.use('fivethirtyeight')

fig = plt.figure()

if amount_of_graphs_needed > 0:
    ax1 = plt.subplot(2, 2, 1)
    amount_of_graphs_needed -= 1

if amount_of_graphs_needed > 0:
    ax2 = plt.subplot(2, 2, 2)
    amount_of_graphs_needed -= 1

if amount_of_graphs_needed > 0:
    ax3 = plt.subplot(2, 2, 3)
    amount_of_graphs_needed -= 1

if amount_of_graphs_needed > 0:
    ax4 = plt.subplot(2, 2, 4)
    amount_of_graphs_needed -= 1


def animate(i):
    stocks_dict = {}
    with open(r"PATH-TO-SPREADSHEET.csv") as f:
        reader = csv.reader(f)
        header_text = next(reader)

        amount_of_rows = 0

        # adding stocks to stock dictionary and stock names list
        for index, column_header in enumerate(header_text):  # adding all stocks to a dictionary with a list connected to them so I can add there prices to that list
            if index >= 2 and index % 2 == 0:  # if the index is >= 2 and its an even number it means it is the name of a stock in the csv
                stocks_dict[column_header] = []  # add the stock to the dictionary and make it a list

        for row in reader:  # loop through all rows
            for i in range(len(row)):  # loop through all parts of that row
                if '.' in row[i]:  # if there is a . in the row[i] it is the price
                    number = row[i].replace(',', '')   # remove comma so I can convert string into a number
                    rounded_number = round(float(number))   # rounds it so the decimal isn't there
                    stocks_dict[row[i + 1]].append(rounded_number)  # add that price to the dict key it relates to
            amount_of_rows += 1  # add 1 to the amount of rows this is how I know how long the x_axis needs to be

        xaxis = list(range(1, amount_of_rows + 1))  # create the x_axis

        # adding all of the graphs

        if ax1 is not None:
            ax1.clear()
            stock = list(stocks_dict.keys())[0]  # creates a list of all stock names and picks first one
            prices = stocks_dict[stock]
            ax1.plot(xaxis, prices)
            ax1.set_title(f"{stock}", fontsize=9)

        if ax2 is not None:
            ax2.clear()
            stock = list(stocks_dict.keys())[1]
            prices = stocks_dict[stock]
            ax2.plot(xaxis, prices)
            ax2.set_title(f"{stock}", fontsize=9)

        if ax3 is not None:
            ax3.clear()
            stock = list(stocks_dict.keys())[2]
            prices = stocks_dict[stock]
            ax3.plot(xaxis, prices)
            ax3.set_title(f"{stock}", fontsize=9)

        if ax4 is not None:
            ax4.clear()
            stock = list(stocks_dict.keys())[3]
            prices = stocks_dict[stock]
            ax4.plot(xaxis, prices)
            ax4.set_title(f"{stock}", fontsize=9)


ani = animation.FuncAnimation(fig, animate, interval=100)

plt.tight_layout()
plt.show()
