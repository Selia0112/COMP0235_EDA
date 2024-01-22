# COMP0235_EDA

# Building a distributed analysis system for human proteome analysis

This assignment requires us to create a distributed analysis system for protein analysis. This system will use a pre-written data analysis pipeline and distribute tasks to five workhorses to speed up processing time for the biochemistry research team.

Key Generation:

In your own computer
``` bash
ssh-keygen -t rsa -b 2048 -f ~/.ssh/new_key
``` 
``` bash
scp -i /path/to/lecturer_key ~/.ssh/new_key.pub ec2-user@18.168.125.113
``` 
``` bash
scp -i /path/to/lecturer_key ~/.ssh/new_key.pub ec2-user@13.41.118.62
``` 
``` bash
scp -i /path/to/lecturer_key ~/.ssh/new_key.pub ec2-user@13.42.80.179
``` 
``` bash
scp -i /path/to/lecturer_key ~/.ssh/new_key.pub ec2-user@18.135.57.168
``` 
``` bash
scp -i /path/to/lecturer_key ~/.ssh/new_key.pub ec2-user@ 35.176.255.87
``` 
When you are in client machines
``` bash
cat ~/.ssh/new_key.pub >> ~/.ssh/authorized_keys
``` 
``` bash
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~/.ssh
``` 
Back to your computer to test if the connection is done or not
``` bash
ssh -i ~/.ssh/lecturer_key ec2-user@ec2-18-130-243-34.eu-west-2.compute.amazonaws.com
``` 
Back to host to test if the connection is done or not
``` bash
ssh -i ~/.ssh/new_key ec2-user@ec2-18-168-125-113.eu-west-2.compute.amazonaws.com
ssh -i ~/.ssh/new_key ec2-user@ec2-13-41-118-62.eu-west-2.compute.amazonaws.com
ssh -i ~/.ssh/new_key ec2-user@ec2-13-42-80-179.eu-west-2.compute.amazonaws.com
ssh -i ~/.ssh/new_key ec2-user@ec2-18-135-57-168.eu-west-2.compute.amazonaws.com
ssh -i ~/.ssh/new_key ec2-user@ec2-35-176-255-87.eu-west-2.compute.amazonaws.com
``` 
Configure Inventory File (in host)
``` bash
touch hosts
vi hosts
```
Define the control node

In the inventory file (hosts), add the IP address of host
``` bash
[client]
# Client (Scheduler) IP or hostname
client1 ansible_host=XX.XX.XX.XX
``` 
Define the client node (clusters)
``` bash
[cluster]
# Cluster (slaver) IP or hostnames
slaver1 ansible_host=XX.XX.XX.XX
slaver2 ansible_host=XX.XX.XX.XX
slaver3 ansible_host=XX.XX.XX.XX
slaver4 ansible_host=XX.XX.XX.XX
slaver5 ansible_host=XX.XX.XX.XX
slaver6 ansible_host=XX.XX.XX.XX
``` 
Mount the data volume:
``` bash
ansible-playbook -i /home/ec2-user/hosts /home/ec2-user/mount.yml
``` 
Software Installs via yum, dnf or pip:
``` bash
ansible-playbook -i /home/ec2-user/hosts /home/ec2-user/install_software_and_dependencies.yml
``` 
Download two machine learning models:
``` bash
ansible-playbook -i /home/ec2-user/hosts /home/ec2-user/download_s4pred_and_hhsuite.yml
``` 
Service Configuration
``` bash
ansible-playbook -i /home/ec2-user/hosts /home/ec2-user/firewalld.yml
``` 
Download data from the web

There are two existing data files stored in the host: experiment_ids.txt and uniprotkb_proteome_UP000005640_2023_10_05.fasta

And you need to download pdb70 from web
``` bash
ansible-playbook -i /home/ec2-user/hosts /home/ec2-user/download_and_unpack_pdb70.yml
``` 
Breaking up data into pieces for each node
``` bash
split -l 1000 experiment_ids.txt experiment_ids.
``` 
Then you will see 6 files in the host machine: experiment_ids.aa, experiment_ids.ab, experiment_ids.ac, experiment_ids.ad, experiment_ids.ae, experiment_ids.af.

Then using select_ids_new.py for protein-specific information extraction
``` bash
ansible-playbook -i /home/ec2-user/hosts /home/ec2-user/select_ids_new.py
``` 

Change experiment_ids.aa to experiment(1).fasta

Change experiment_ids.ab to experiment(2).fasta

Change experiment_ids.ac to experiment(3).fasta

Change experiment_ids.ad to experiment(4).fasta

Change experiment_ids.af to experiment(5).fasta

Change experiment_ids.ae to experiment(6).fasta

Using distribute_experiment_fasta_files.yml to distribute 6 fasta files to 6 different client machines

``` bash
ansible-playbook -i /home/ec2-user/hosts /home/ec2-user/distribute_experiment_fasta_files.yml
``` 
Running pipeline in parallel to perform large computations
``` bash
ansible-playbook -i /home/ec2-user/hosts /home/ec2-user/run_pipeline.yml
``` 
Monitor:

Using new relic

When all processes are done, copy 6 hhr_parse.out files to host.
``` bash
ansible-playbook -i /home/ec2-user/hosts /home/ec2-user/copy_hhr_parse_to_host.yml
``` 
Execute hits_output.py to generate best_hits for each data

``` bash
python /home/ec2-user/hits_output.py
``` 
Execute profile_output.py to generate ave_std, ave_gmean in total
``` bash
python /home/ec2-user/profile_output.py
``` 