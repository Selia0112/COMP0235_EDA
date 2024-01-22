import pandas as pd

def process_files(file_path_1, file_path_2, file_path_3, file_path_4, file_path_5, output_file_path):
    # Read the contents of the files, skipping the first row (header)
    data_1 = pd.read_csv(file_path_1, skiprows=1, header=None)
    data_2 = pd.read_csv(file_path_2, skiprows=1, header=None)
    data_3 = pd.read_csv(file_path_3, skiprows=1, header=None)
    data_4 = pd.read_csv(file_path_4, skiprows=1, header=None)
    data_5 = pd.read_csv(file_path_5, skiprows=1, header=None)

    # Drop rows with NaN values in both dataframes
    data_1 = data_1.dropna()
    data_2 = data_2.dropna()
    data_3 = data_3.dropna()
    data_4 = data_4.dropna()
    data_5 = data_5.dropna()

    # Concatenate the two dataframes (only the last two columns)
    combined_data = pd.concat([data_1.iloc[:, -2:], data_2.iloc[:, -2:], data_3.iloc[:, -2:], data_4.iloc[:, -2:], data_5.iloc[:, -2:]], ignore_index=True)

    # Calculate the average of the last column and second-to-last column
    ave_gmean = combined_data.iloc[:, -1].mean()
    ave_std = combined_data.iloc[:, -2].mean()

    # Create a new DataFrame to store these averages
    averages_data = pd.DataFrame({
        'ave_std': [ave_std],
        'ave_gmean': [ave_gmean]
    })

    # Save the new DataFrame to a CSV file
    averages_data.to_csv(output_file_path, index=False)


if __name__ == "__main__":
    file_path_1 = '/home/ec2-user/hhr_parse_1.out'  
    file_path_2 = '/home/ec2-user/hhr_parse_2.out' 
    file_path_3 = '/home/ec2-user/hhr_parse_3.out' 
    file_path_4 = '/home/ec2-user/hhr_parse_4.out'  
    file_path_5 = '/home/ec2-user/hhr_parse_5.out'  
    output_file_path = '/home/ec2-user/profile_output.csv'  # Replace with desired output path

    process_files(file_path_1, file_path_2, file_path_3, file_path_4, file_path_5, output_file_path)
