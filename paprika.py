import matplotlib.pyplot as plt

LAST_DATE_ON_RECORD = "May 9, 2020"


def make_country_list():
    # this function makes a list of countries from file
    print('')
    # populate list of countries from file
    country_list = []
    for country in open('countries.txt'):
        country = country.strip()
        country_list.append(country)
    return country_list


def make_date_list():
    # populate list of valid calendar dates from file
    date_list = []
    for date in open('dates.txt'):
        date = int(date.strip())
        date_list.append(date)
    return date_list


def print_country_list(country_list):
    # print list of countries with their index
    for index in range(len(country_list)):
        country = country_list[index]
        print(index, str(country), end=" | ")
        if index > 0 and index % 8 == 0:
            print("")


def dashboard_main_select_country(country_list, compare):
    # This condition is true if user selected user action 2 compare two countries
    if compare == 1:
        # print countries, select country1
        print_country_list(country_list)
        print('')
        print('')
        country_selection_1 = int(input('Select first country by number: '))
        # print('')
        print('you have selected country: ' + country_list[country_selection_1])

        # select country2
        print('')
        country_selection_2 = int(input('Select second country by number: '))
        # print('')
        print('you have selected country: ' + country_list[country_selection_2])

        return country_selection_1, country_selection_2

    # Single country view mode
    print_country_list(country_list)
    print('')
    print('')
    country_selection_1 = int(input('Select country by number: '))
    print('')
    print('you have selected country: ' + country_list[country_selection_1])
    return country_selection_1


def make_cases_day_list(country_list, country_selection_1):
    # opens .txt file in folder confirmed/ for selected country
    # makes list of values as INT from .txt file
    path = ('confirmed/' + country_list[country_selection_1] + '.txt')
    cases_day_list = []
    for cases_day in open(path):
        cases_day = int(cases_day.strip())
        cases_day_list.append(cases_day)
    return cases_day_list


def make_calendar_day_from_index(date_list, index, graph_y_n):
    # takes index and assigns it a full calendar date

    # if user selected to view graph this is true
    # uses short form month for graph display
    if graph_y_n == 0:
        month_name = ['1/', '2/', '3/', '4/', '5/']

    # regular long form month for non graph making
    else:
        month_name = ['January', 'February', 'March', 'April', 'May']

    if index <= 9:
        full_date_of_index = f'{month_name[0]} {date_list[index]}'
    elif 10 <= index <= 38:
        full_date_of_index = f'{month_name[1]} {date_list[index]}'
    elif 39 <= index <= 69:
        full_date_of_index = f'{month_name[2]} {date_list[index]}'
    elif 70 <= index <= 99:
        full_date_of_index = f'{month_name[3]} {date_list[index]}'
    elif 100 <= index <= 109:
        full_date_of_index = f'{month_name[4]} {date_list[index]}'

    return full_date_of_index


def make_graph_for_country_data(index, changes_per_day_list, date_list, country_list, country_selection_1):
    # value to pass to make calendar to tell whether or not to use short form month names
    graph_y_n = 0

    # make a list of all full dates to use for x axis of graph
    list_all_full_dates = []
    for date in range(index, len(date_list)):
        full_date = date_list[date]
        full_date = make_calendar_day_from_index(date_list, date, graph_y_n)
        list_all_full_dates.append(full_date)

    # data for y axis
    y = changes_per_day_list

    # label for x axis using first case date
    label_x = f'Cases from {list_all_full_dates[1]} through {list_all_full_dates[-1]}'
    label_title = f'Change in Positive cases per day for {country_list[country_selection_1]}'

    # to make the axes equal in count value but also bc the method to provide change is cases is day - next day
    # there is one less value of dates to display. So pop the first date to equalize
    list_all_full_dates.pop(0)

    fig, ax = plt.subplots(figsize=(20, 8))
    ax.plot(list_all_full_dates, y, 'b--', list_all_full_dates, y, 'ro')

    # rotates x axis label
    plt.xticks(rotation=75)

    # labels for making graph
    ax.set(xlabel=label_x, ylabel='Cases Per Day',
           title=label_title)
    ax.grid()

    fig.savefig("test.png")
    plt.show()


def graph_highest_avg_change(averages_for_graph, countries_for_graph):
    x = [countries_for_graph[0], countries_for_graph[1], countries_for_graph[2], countries_for_graph[3],
         countries_for_graph[4], countries_for_graph[5], countries_for_graph[6], countries_for_graph[7],
         countries_for_graph[8], countries_for_graph[9]]
    avgs = [averages_for_graph[0], averages_for_graph[1], averages_for_graph[2], averages_for_graph[3],
            averages_for_graph[4], averages_for_graph[5], averages_for_graph[6], averages_for_graph[7],
            averages_for_graph[8], averages_for_graph[9]]

    fig, ax = plt.subplots(figsize=(20, 8))
    plt.bar(x, avgs)
    plt.xlabel("Countries")
    plt.ylabel("Average change per day value")
    plt.title("Top 10 countries with highest average change per day")
    plt.xticks(x, (countries_for_graph[0], countries_for_graph[1], countries_for_graph[2], countries_for_graph[3],
                   countries_for_graph[4], countries_for_graph[5], countries_for_graph[6], countries_for_graph[7],
                   countries_for_graph[8], countries_for_graph[9]))
    plt.show()


def graph_highest_total_cases(top_ten_for_graph, countries_for_graph):
    x = [countries_for_graph[0], countries_for_graph[1], countries_for_graph[2], countries_for_graph[3],
         countries_for_graph[4], countries_for_graph[5], countries_for_graph[6], countries_for_graph[7],
         countries_for_graph[8], countries_for_graph[9]]
    case_totals = [top_ten_for_graph[0], top_ten_for_graph[1], top_ten_for_graph[2], top_ten_for_graph[3],
                   top_ten_for_graph[4], top_ten_for_graph[5], top_ten_for_graph[6], top_ten_for_graph[7],
                   top_ten_for_graph[8], top_ten_for_graph[9]]

    fig, ax = plt.subplots(figsize=(20, 8))
    plt.bar(x, case_totals)
    plt.xlabel("Countries")
    plt.ylabel("Total Cases")
    plt.title(f"Top 10 highest amount of cases as of {LAST_DATE_ON_RECORD}")
    plt.xticks(x, (countries_for_graph[0], countries_for_graph[1], countries_for_graph[2], countries_for_graph[3],
                   countries_for_graph[4], countries_for_graph[5], countries_for_graph[6], countries_for_graph[7],
                   countries_for_graph[8], countries_for_graph[9]))
    plt.show()


def generate_data_for_dashboard(country_list, date_list, country_selection_1, cases_day_list, compare):
    # get first non zero value from cases/day data
    index = 0
    for value in cases_day_list:
        if value == 0:
            index += 1
        # index at end of loop = location of first non-zero number

        # default value reference to NOT make graph
        graph_y_n = 1
        # get date of index
        full_date_of_index = make_calendar_day_from_index(date_list, index, graph_y_n)

    # get change per day by calling list of cases per day and finding difference between days
    changes_per_day_list = []
    # for each value in list of cases per day from index of first non zero day until the end of list
    # append the difference of two days into changes_per_day_list
    # pop the last value bc fence posting
    for i in range(index, len(cases_day_list)):
        day_value_current = cases_day_list[i]
        day_value_next = cases_day_list[i - 1]
        difference = day_value_current - day_value_next
        changes_per_day_list.append(difference)
    changes_per_day_list.pop(0)

    print(f'Date of first case: {full_date_of_index} - Number of cases: {cases_day_list[index]}')
    print(f'Total number of cases as of May 9, 2020: {cases_day_list[-1]}')

    print('Average new cases per day from ' + str(full_date_of_index) + " to " +
          str(LAST_DATE_ON_RECORD) + ": " + str(sum(changes_per_day_list) / len(changes_per_day_list)))

    # ask to view graph
    graph_yes_or_no = int(input(f'To view graph of data for {country_list[country_selection_1]} enter 0. '
                                f'To continue with no graph enter 1: '))
    print('')

    # call make graph condition
    if graph_yes_or_no == 0:
        make_graph_for_country_data(index, changes_per_day_list, date_list, country_list, country_selection_1)

    # conditions for next user action
    if compare == 0:
        print('')
        loop_or_exit_or_compare = int(input('View a single country enter 0. Exit enter 1. '
                                            'Compare two countries enter 2. '
                                            'Top ten highest cases enter 3. '
                                            'Top ten average change enter 4: '))
    if compare == 1:
        loop_or_exit_or_compare = 0

    return loop_or_exit_or_compare


def compare_two_countries(country_list, date_list):
    print('')
    print('Select two countries to compare')
    print('')

    # pass compare value so the dashboard prints data in compare two countries mode
    compare = 1

    country_selection_1_2 = dashboard_main_select_country(country_list, compare)

    # repackage country selection returns
    country_selection_1 = (country_selection_1_2[0])
    country_selection_2 = (country_selection_1_2[1])

    # make data list for country selection_1
    cases_day_list_c1 = make_cases_day_list(country_list, country_selection_1)
    # make data list for country selection_2
    cases_day_list_c2 = make_cases_day_list(country_list, country_selection_2)

    # presents data for for country selection_1
    print('')
    print(f'Data results for {country_list[country_selection_1]}:')
    # for country selection 1, new box for variable to to keep generate function generic
    country_selection = country_selection_1
    cases_day_list = cases_day_list_c1
    # generate and print data for country selection_1
    generate_data_for_dashboard(country_list, date_list,
                                country_selection, cases_day_list, compare)

    # presents data for for country selection_2
    print(f'Data results for {country_list[country_selection_2]}:')
    # for country selection 2, new box for variable to to keep generate function generic
    country_selection = country_selection_2
    cases_day_list = cases_day_list_c2
    # generate and print data for country selection_2
    generate_data_for_dashboard(country_list, date_list,
                                country_selection, cases_day_list, compare)

    print('')


def print_top_ten(country_list):
    print('')
    print(f'Top 10 countries highest case totals as of {LAST_DATE_ON_RECORD}')
    print('')

    # make list of descending average values for graph
    top_ten_for_graph = []
    # make list of index values for country names or just a list of name
    countries_for_graph = []

    max_cases_per_country = []
    # this loop makes a list of max cases for each country in country_list in order of country list index
    for country in range(0, len(country_list)):
        country_selection_1 = country
        country_selection_1 = country
        cases_day_list = make_cases_day_list(country_list, country_selection_1)

        max_cases = cases_day_list[-1]
        max_cases_per_country.append(max_cases)
    max_cases_country_index = max_cases_per_country.index(max(max_cases_per_country))

    print('Country 1: ' + str(country_list[max_cases_country_index])
          + ": " + str(max(max_cases_per_country)))
    top_ten_for_graph.append(max(max_cases_per_country))
    countries_for_graph.append(country_list[max_cases_country_index])

    # repeat x9 to print remaining top 9 countries with most cases
    for i in range(9):
        max_cases_per_country[max_cases_country_index] = 0

        max_cases_country_index = max_cases_per_country.index(max(max_cases_per_country))
        print(f'Country:{i + 2} ' + str(country_list[max_cases_country_index])
              + ": " + str(max(max_cases_per_country)))
        top_ten_for_graph.append(max(max_cases_per_country))
        countries_for_graph.append(country_list[max_cases_country_index])

    print('')

    # ask to view graph
    graph_yes_or_no = int(input(f'To view graph enter 0. '
                                f'To continue with no graph enter 1: '))
    print('')

    # call make graph condition
    if graph_yes_or_no == 0:
        graph_highest_total_cases(top_ten_for_graph, countries_for_graph)


def top_ten_avg_change(country_list, ):
    print('')
    print(f'Top 10 countries with highest average change per day as of {LAST_DATE_ON_RECORD}')
    print('')

    # list of avg case change for all countries
    all_country_avg_case_change = []
    # this loop makes a list of average case change for all countries
    for country in range(0, len(country_list)):
        country_selection_1 = country
        country_selection_1 = country
        cases_day_list = make_cases_day_list(country_list, country_selection_1)

        # make case day list from first non zero value of country cases/day list
        index = 0
        for value in cases_day_list:

            if value == 0:
                index += 1
                # index at end of loop = location of first non-zero number

        # get change per day by calling list of cases per day and finding difference between days
        changes_per_day_list = []
        for i in range(index, len(cases_day_list)):
            day_value_current = cases_day_list[i]
            day_value_next = cases_day_list[i - 1]
            difference = day_value_current - day_value_next
            changes_per_day_list.append(difference)
        changes_per_day_list.pop(0)
        avg = sum(changes_per_day_list) / len(changes_per_day_list)
        all_country_avg_case_change.append(avg)

    # get index of max avg
    max_avg_country_index = all_country_avg_case_change.index(max(all_country_avg_case_change))

    # make list of descending average values for graph
    averages_for_graph = []
    # make list of index values for country names or just a list of name
    countries_for_graph = []

    # print country with most cases
    print('Country:1 ' + str(country_list[max_avg_country_index])
          + ": " + str(max(all_country_avg_case_change)))
    averages_for_graph.append(max(all_country_avg_case_change))
    countries_for_graph.append(country_list[max_avg_country_index])

    # repeat x9 to print remaining top 9 countries with highest avg change
    for i in range(9):
        all_country_avg_case_change[max_avg_country_index] = 0

        max_avg_country_index = all_country_avg_case_change.index(max(all_country_avg_case_change))

        print(f'Country:{i + 2} ' + str(country_list[max_avg_country_index])
              + ": " + str(max(all_country_avg_case_change)))
        averages_for_graph.append(max(all_country_avg_case_change))
        countries_for_graph.append(country_list[max_avg_country_index])
    print('')

    # ask to view graph
    graph_yes_or_no = int(input(f'To view graph enter 0. '
                                f'To continue with no graph enter 1: '))
    print('')

    # call make graph condition
    if graph_yes_or_no == 0:
        graph_highest_avg_change(averages_for_graph, countries_for_graph)


def user_action_choice():
    # ask user what to do
    choice = int(input('View a single country enter 0. Exit enter 1. '
                       'Compare two countries enter 2. '
                       'Top ten highest cases enter 3. '
                       'Top ten average change enter 4: '))
    print('')
    return choice  # return what to do


def welcome():
    print('Hello and welcome to -@ paprika @- a minimalistic data dashboard for international covid data')
    print('paprika is a tool that displays covid case data for the country you select.')
    print('')
    print('This version of paprika has access to the amount of cases per day in a given country '
          'from dates: January 22, 2020 to May 9, 2020')
    print('Please select from the following menu:')
    print('')


def goodbye():
    print('')
    print("@@@ Thank you for visiting, please come again! @@@")
    print("@@@ Don't forget, paprika makes data delicious! @@@")


def main():
    # create initial reference for user action loop
    loop_or_exit_or_compare = 0
    # makes list of countries for country reference by index
    country_list = make_country_list()
    # makes list of dates for date reference by index
    date_list = make_date_list()
    # welcome info and intro
    welcome()

    # main program run loop. program life line. runs until user selects an exit/break function
    while True:
        # this value check exists to carry over user action choice after user action loop break -
        # if user selected exit option aka user option 1 from prompt
        if loop_or_exit_or_compare == 1:
            goodbye()
            break

        # asks user for action option and loop check
        if loop_or_exit_or_compare == 0:
            action = user_action_choice()

        # @@@ USER ACTION 0 to view single country data aka user option 0 from prompt @@@ #
        if action == 0:
            while True:
                print('')
                # compare value to pass to helper functions -
                # to let them know whether to run as single country mode view or compare mode
                compare = 0

                # prompts user to select a country
                country_selection_1 = dashboard_main_select_country(country_list, compare)

                # makes a list of cumulative cases per day for the country selected by the user
                cases_day_list = make_cases_day_list(country_list, country_selection_1)

                # generates data to view for user selected country -
                # and returns user option to continue or exit
                loop_or_exit_or_compare = generate_data_for_dashboard(country_list, date_list, country_selection_1,
                                                                      cases_day_list, compare)

                # these conditions check whether or not user wants to:
                # exit loop return user action 1 to exit
                if loop_or_exit_or_compare == 1:
                    action = 1
                    break
                if loop_or_exit_or_compare == 2:
                    action = 2
                    break
                if loop_or_exit_or_compare == 0:
                    action = 0
                    loop_or_exit_or_compare = 5
                    break
                if loop_or_exit_or_compare == 3:
                    action = 3
                    loop_or_exit_or_compare = 5
                    break
                if loop_or_exit_or_compare == 4:
                    action = 4
                    loop_or_exit_or_compare = 5
                    break

        #  @@@ USER ACTION 1 this condition will exit user from program @@@ #
        if action == 1:
            goodbye()
            break

        # @@@ USER ACTION 2 this condition will run if user wants to compare two countries @@@ #
        if action == 2:
            while True:
                # call function to compare two countries
                compare_two_countries(country_list, date_list)

                # user action complete, now what?
                loop_or_exit_or_compare = int(input('View a single country enter 0. Exit enter 1. '
                                                    'Compare two countries enter 2. '
                                                    'Top ten highest cases enter 3. '
                                                    'Top ten average change enter 4: '))

                # conditions to return user action to main loop and break top ten loop
                if loop_or_exit_or_compare == 1:
                    action = 1
                    break
                if loop_or_exit_or_compare == 2:
                    action = 2
                    break
                if loop_or_exit_or_compare == 0:
                    action = 0
                    loop_or_exit_or_compare = 5
                    break
                if loop_or_exit_or_compare == 3:
                    action = 3
                    loop_or_exit_or_compare = 5
                    break
                if loop_or_exit_or_compare == 4:
                    action = 4
                    loop_or_exit_or_compare = 5
                    break

        # @@@ USER ACTION 3 this condition will run if user wants to print top 10 total cases @@@ #
        if action == 3:
            while True:
                # calls function to print top 10 total cases
                print_top_ten(country_list)

                # user action complete, now what?
                loop_or_exit_or_compare = int(input('View a single country enter 0. Exit enter 1. '
                                                    'Compare two countries enter 2. '
                                                    'Top ten highest cases enter 3. '
                                                    'Top ten average change enter 4: '))

                # conditions to return user action to main loop and break top ten loop
                if loop_or_exit_or_compare == 1:
                    action = 1
                    break
                if loop_or_exit_or_compare == 2:
                    action = 2
                    break
                if loop_or_exit_or_compare == 0:
                    action = 0
                    loop_or_exit_or_compare = 5
                    break
                if loop_or_exit_or_compare == 3:
                    action = 3
                    loop_or_exit_or_compare = 5
                    break
                if loop_or_exit_or_compare == 4:
                    action = 4
                    loop_or_exit_or_compare = 5
                    break

        # @@@ USER ACTION 4 this condition will run if user wants to print top 10 avg change in cases @@@ #
        if action == 4:
            while True:
                # call function to print top ten avg change list
                top_ten_avg_change(country_list)

                # user action complete, now what?
                loop_or_exit_or_compare = int(input('View a single country enter 0. Exit enter 1. '
                                                    'Compare two countries enter 2. '
                                                    'Top ten highest cases enter 3. '
                                                    'Top ten average change enter 4: '))

                # conditions to return user action to main loop and break top ten loop
                if loop_or_exit_or_compare == 1:
                    action = 1
                    break
                if loop_or_exit_or_compare == 2:
                    action = 2
                    break
                if loop_or_exit_or_compare == 0:
                    action = 0
                    loop_or_exit_or_compare = 5
                    break
                if loop_or_exit_or_compare == 3:
                    action = 3
                    loop_or_exit_or_compare = 5
                    break
                if loop_or_exit_or_compare == 4:
                    action = 4
                    loop_or_exit_or_compare = 5
                    break


if __name__ == '__main__':
    main()
