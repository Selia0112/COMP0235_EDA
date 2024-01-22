import sys
from Bio import SeqIO

"""
usage: python select_ids.py INPUT.fasta 2000
"""

def read_ids(file_path):
    with open(file_path, 'r') as file:
        return set(line.strip().split('|')[1] for line in file)

def select_ids(id_file, fasta_file, output_file):

    ids = read_ids(id_file)
    selected_records = []

    for record in SeqIO.parse(fasta_file, "fasta"):
        uniprot_id = record.id.split('|')[1]

        if uniprot_id in ids:
            selected_records.append(record)

    SeqIO.write(selected_records, output_file, "fasta")


if __name__ == "__main__":
    # List of file pairs: (input_id_file, output_fasta_file)
    file_pairs = [
        ('experiment_ids.aa', 'experiment(1).fasta'),
        ('experiment_ids.aa', 'experiment(2).fasta'),
        ('experiment_ids.ab', 'experiment(3).fasta'),
        ('experiment_ids.ac', 'experiment(4).fasta'),
        ('experiment_ids.ae', 'experiment(5).fasta'),
        ('experiment_ids.af', 'experiment(6).fasta'),
    ]

    fasta_file = 'uniprotkb_proteome_UP000005640_2023_10_05.fasta'

    for id_file, output_file in file_pairs:
        select_ids(id_file, fasta_file, output_file)