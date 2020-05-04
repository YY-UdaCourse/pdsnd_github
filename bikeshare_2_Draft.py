import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = ()

    valid_city = ["chicago", "new york city", "washington"]

    while city == ():

        user_city = input('\nFor which city would you like to view data: Chicago, New York City, or Washington?\n').lower() #convert input to lowercase

        while user_city not in valid_city:

            user_city = input("\nI'm having trouble reading your city. Please re-enter the city whose data you would like to view: Chicago, New York City, or Washington.\n").lower() #convert input to lowercase

        if user_city in valid_city:

            city = user_city

        else:

            city = ()

    print("\nHere's the city you selected:\n", city.title())

    # get user input for month (all, january, february, ... , june)

    month = ()

    valid_month = ["all", 'january', 'february', 'march', 'april', 'may', 'june']

    while month == ():

        user_month = input("\nFor which month would you like to view data? Enter 'all' or a specific month. Type in the full spelling (e.g. January, February, etc.)\n").lower()

        while user_month not in valid_month:

              user_month = input("\nI'm having trouble reading your month. Please re-enter the month for which you would like to view data. Enter 'all' or a specific month. Spell out the month (e.g. January, February, May, etc.)\n").lower() #convert input to lowercase

        if user_month in valid_month:

            month = user_month

        else:

            month = ()

    print("\nHere's the month you selected:\n", month.title())

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = ()

    valid_day = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    while day == ():

        user_day = input("\nFor which day of the week would you like to view data? Enter 'all' or a specific day. Please spell out the entire day (e.g. Monday, Tuesday, etc.).\n").lower()

        while user_day not in valid_day:

              user_day = input("\nI'm having trouble reading the day of the week. Please re-enter the day for which you would like to view data. Enter 'all' or a specific day. Please spell out the entire day (e.g. Monday, Tuesday, etc.).\n").lower() #convert input to lowercase

        if user_day in valid_day:

            day = user_day

        else:

            day = ()

    print("\nHere's the day of week you selected:\n", day.title())

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city]) # similar to practiceQ3, load data file into a dataframe

    df['Start Time'] = pd.to_datetime(df['Start Time']) # similar to practiceQ3, convert the "Start Time" column to to_datetime YY

    # similar to practiceQ3, extract month and day of week from "Start Time" to create new columns YY
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month, if applicable
    if month != 'all':
        # use the index of months list to get the corresponding int YY

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create new dataframe
        df = df[df['month'] == month]

    #filter by day of week, if applicable
    if day != 'all':
        #filter by day of week to create the new dataframe YY
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time']) # convert the "Start Time" column to datetime YY

    print(df['month'])
    # display the most common month
    popular_month = df['month'].mode()[0]

    print('after pop month', df['month'])

    print("\nMost common month:\n", int(popular_month))

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print("\nMost popular day:\n", popular_day)

    # need to extract hour from "Start Time" to create an hour column YY
    df['hour'] = df['Start Time'].dt.hour

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('\nMost popular start hour:\n', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('\nMost popular start station:\n', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('\nMost popular end station:\n', popular_end_station)

    # display most frequent combination of start station and end station trip
    # combine start and end station data & create new column YY
    df['Station Pair'] = df['Start Station'] + ' AND ' + df['End Station']

    popular_station_pair = df['Station Pair'].mode()[0]

    print('\nMost frequent combination of start and end station per trip:\n', popular_station_pair)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # travel time is in seconds in the csv files. sum the travel times, then convert from sec to min YY

    duration_total_min = df['Trip Duration'].sum()/60

    print('\nTotal travel time: {} minutes\n'.format(duration_total_min))

    # display mean travel time
    duration_mean = df['Trip Duration'].mean()/60

    print('\nMean travel time: {} minutes\n'.format(duration_mean))

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:

        # Display counts of user types
        user_types = df['User Type'].value_counts()

        print('\nHere are the counts of user types:\n', user_types)

        # Display counts of gender

        sex_count = df['Gender'].value_counts()
        sex_nodata = df['Gender'].isnull().sum().sum()

        print('\nBased on the available data, here is the breakdown of users by sex:\n', sex_count)
        print('\nNote there were {} recorded trips without user data for sex.\n'.format(sex_nodata))

        # identify and drop rows with null values in 'Birth Year' column, convert type to string YY
        df['Birth Year'].isnull()
        birthyear_nonulls = df['Birth Year'].dropna(axis = 0).astype(str)
        birthyear_nodata = df['Birth Year'].isnull().sum().sum()

        # Display earliest, most recent, and most common year of birth

        oldest_birthyear = birthyear_nonulls.min()
        youngest_birthyear = birthyear_nonulls.max()
        common_birthyear = birthyear_nonulls.mode()[0]

        print('\nThe earliest birth year is:\n', (oldest_birthyear[:4]))
        print('\nThe most recent birth year is:\n', (youngest_birthyear[:4]))
        print('\nThe most common birth year is:\n', common_birthyear[:4])
        print('\nNote there were {} recorded trips without user data for birth year.\n'.format(birthyear_nodata))

    except:

        print("\nThere is no further user data available for your city.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """displays more data for df if user desires"""

    #created this function to use multiple times in program

    view_data = 'yes'
    n = 6

    # if user wants to view more data, add 5 more rows to view at a time
    while view_data == 'yes':

        view_data = input("\nWould you like to view additional raw data? Enter 'yes' or 'no'.\n").lower()

        if view_data == 'no':

            break

        if view_data == 'yes':

            df.head(n)

            print("\nHere's the data: \n", df.head(n))

            n = n + 5

        else:

            view_data = input("I'm having trouble reading your response. Please enter 'yes' to continue or 'no' to move to the next section.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        raw_data(df[df.columns[1:3]])
        station_stats(df)
        raw_data(df[df.columns[4:6]])
        trip_duration_stats(df)
        raw_data(df[df.columns[3:4]])
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
