import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Please enter a city you want to explore the data (the options are Chicago, New York City or Washington): ")
            city = city.title() 
        except ValueError:
            print("Sorry, I didn't understand that.")
            #better try again... Return to the start of the loop
            continue
        if city not in ('Chicago', 'New York City', 'Washington'):
            print("Sorry, your response must be one of the three options give in the list.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Please enter a month you want to explore the data (all, january, february, march, april, may or june): ")
            month = month.lower()
        except ValueError:
            print("Sorry, I didn't understand that.")
            #better try again... Return to the start of the loop
            continue
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Sorry, your response must be one of the three options give in the list.")
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Please enter a day of week you want to explore the data (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ")
            day = day.lower()
        except ValueError:
            print("Sorry, I didn't understand that.")
            #better try again... Return to the start of the loop
            continue
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Sorry, your response must be one of the three options give in the list.")
            continue
        else:
            break

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
    
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    # filter by day of week
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()] 
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = df['month'].mode()[0]
    month = months[common_month - 1]
    print(f'The most common month is: {month}.')

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f'The most common day of week is: {common_day}.')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f'The most common hour is: {common_hour}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'The most common start station is: {common_start_station}.')

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f'The most common end station is: {common_end_station}.')

    # TO DO: display most frequent combination of start station and end station trip
    df['Start/End Station'] = df['Start Station'] + '/' + df['End Station']
    common_comb = df['Start/End Station'].mode()[0]   
    print(f'The most frequent combination of start station and end station trip is: {common_comb}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['travel_time'] = (df['End Time'] - df['Start Time'])
    total_duration = df['travel_time'].sum()
    print(f'Total trip duration is: {total_duration}.')
    
    # TO DO: display mean travel time
    df['travel_time'] = (df['End Time'] - df['Start Time'])
    average_duration = df['travel_time'].mean()
    print(f'Average trip duration is: {average_duration}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_types = df['User Type'].value_counts().to_frame()
    print(f'The counts of user types is: \n {count_types} \n')

    try:
        # TO DO: Display counts of gender
        count_gender = df['Gender'].value_counts().to_frame()
        print(f'The counts of user types is: \n {count_gender}\n')

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        print(f'The earliest year of birth is: {earliest}\n The most recent year of birth is: {recent}\n The most common year of birth is: {common}')

    except:
        print('City Washington does not have information about gender end birth year.')
                
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_raw_data(df):
    """ Displays raw data upon request by the user. """
    i = 0
    raw = input("Would you like to see the raw data?").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Would you like to see the raw data?").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
