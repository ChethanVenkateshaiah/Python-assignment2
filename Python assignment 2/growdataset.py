import pandas as pd              # Importing the pandas package for data manipulation
import matplotlib.pyplot as plt  # Importing the matplotlib.pyplot module for data visualization


# Define a function to rename dataframe columns
def col_rename(dataframe):
    """Renames columns to latitude and longitude if they are swapped."""
    # Check if the 'Latitude' and 'Longitude' columns are in the dataframe
    if 'Latitude' in dataframe.columns and 'Longitude' in dataframe.columns:
        # Create a dictionary to map the current column names to the desired ones
        new_col_names = {'Longitude': 'latitude', 'Latitude': 'longitude'}
        # Rename the columns using the mapping dictionary
        dataframe = dataframe.rename(columns=new_col_names)
    # Return the dataframe with the columns renamed
    return dataframe

# Define a function to filter the dataframe for valid latitude and longitude values
def data_filter(dataframe):
    """Filters the dataframe for valid latitude and longitude values."""
    # Define bounding box values for the UK
    lon_min, lon_max = -10.592, 1.6848
    lat_min, lat_max = 50.681, 57.985

    # Filter the dataframe to include only rows with latitude and longitude within the defined bounds
    dataframe = dataframe[
        (dataframe['latitude'] >= lat_min) & (dataframe['latitude'] <= lat_max) &
        (dataframe['longitude'] >= lon_min) & (dataframe['longitude'] <= lon_max)
    ]
    # Return the filtered dataframe
    return dataframe

# Define the main function to plot Grow locations on a map of the UK
def GrowMap(file_path):
    """Main function to plot Grow locations on a map of the UK."""
    try:
        # Attempt to read the CSV data into a pandas dataframe
        grow_data = pd.read_csv(file_path)

        # Process the data by renaming columns and filtering invalid data
        grow_data = col_rename(grow_data)
        grow_data = data_filter(grow_data)

        # Start the plotting process
        plt.figure(figsize=(10, 15))                       # Set the size of the figure
        uk_map = plt.imread('resources/map7.png')          # Read the UK map image from the specified path
        plt.imshow(uk_map, extent=[-10.5, 1.8, 50.6, 57.8])# Display the UK map as a background image
        plt.scatter(grow_data['longitude'], grow_data['latitude'], alpha=0.7, c='red', marker='o')# Plot the Grow data points on the map
        plt.title("Grow Sensor Locations on UK Map")       # Set the title of the plot
        plt.xlabel("Longitude")                            # Set the label for the x-axis
        plt.ylabel("Latitude")                             # Set the label for the y-axis
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')# Enable the grid for better readability
        plt.savefig('GrowDataset.png')                         # Save the figure to a file
        plt.show()                                         # Display the plot on screen

    except FileNotFoundError:             # Catch and handle the FileNotFoundError exception
        print("File not found. Please ensure the file path is correct.")
    except Exception as e:                # Catch and handle any other exceptions
        print(f"An error occurred: {e}")

if __name__ == '__main__':                   # Check if the script is run as the main program and not as a module
    GrowMap('resources/GrowLocations.csv')   # Call the main function with the path to the Grow data CSV file