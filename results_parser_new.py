from Bio import SearchIO
import numpy as np
from scipy.stats import gmean
import os

# Initialize variables
best_hit = []
best_score = 0
good_hit_scores  = []
query_id = ''

# Parse the results
for result in SearchIO.parse('tmp.hhr', 'hhsuite3-text'):
    query_id = result.id
    for hit in result.hits:
        if hit.score >= best_score:
            best_score = hit.score
            best_hit = [hit.id, hit.evalue, hit.score]
        if hit.evalue < 1.e-5:
            good_hit_scores.append(hit.score)

# Prepare to write the results
output_file = "hhr_parse.out"
# Check if the file exists and write the header if the file is new
if not os.path.isfile(output_file):
    with open(output_file, "w") as fhOut:
        fhOut.write("query_id,best_hit,best_evalue,best_score,score_mean,score_std,score_gmean\n")

# Append the results to the file
with open(output_file, "a") as fhOut:
    mean = format(np.mean(good_hit_scores), ".2f")
    std = format(np.std(good_hit_scores), ".2f")
    g_mean = format(gmean(good_hit_scores), ".2f")
    fhOut.write(f"{query_id},{best_hit[0]},{best_hit[1]},{best_hit[2]},{mean},{std},{g_mean}\n")
