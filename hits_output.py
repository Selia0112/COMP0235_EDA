import pandas as pd


def process_files(file_path_1, file_path_2, file_path_3, file_path_4, file_path_5, output_file_path):
    # Read the contents of the files, skipping the first row (header)
    data_1 = pd.read_csv(file_path_1, skiprows=1, header=None, usecols=[0, 1])
    data_2 = pd.read_csv(file_path_2, skiprows=1, header=None, usecols=[0, 1])
    data_3 = pd.read_csv(file_path_3, skiprows=1, header=None, usecols=[0, 1])
    data_4 = pd.read_csv(file_path_4, skiprows=1, header=None, usecols=[0, 1])
    data_5 = pd.read_csv(file_path_5, skiprows=1, header=None, usecols=[0, 1])
    # Concatenate the two dataframes
    combined_data = pd.concat([data_1, data_2, data_3, data_4, data_5], ignore_index=True)

    # Define new header
    new_header = ['fasta_id', 'best_hit_id']

    # Save the combined data to a new CSV file without adding an index column
    combined_data.to_csv(output_file_path, index=False, header=new_header)

if __name__ == "__main__":
    # Replace the file paths with the actual paths to your files
    file_path_1 = '/home/ec2-user/hhr_parse_1.out'
    file_path_2 = '/home/ec2-user/hhr_parse_2.out'
    file_path_3 = '/home/ec2-user/hhr_parse_3.out'
    file_path_4 = '/home/ec2-user/hhr_parse_4.out'
    file_path_5 = '/home/ec2-user/hhr_parse_5.out'
    output_file_path = '/home/ec2-user/hits_output.csv'

    # Call the function with the file paths
    process_files(file_path_1, file_path_2, file_path_3, file_path_4, file_path_5, output_file_path)
