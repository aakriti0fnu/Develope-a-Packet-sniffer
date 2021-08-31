

------

## We ran project in 2 ways:
### 1. with Virtual Box - Ubuntu 18.04 LTS. Steps are follow:

Initial Setup - Scapy module installation
Scapy is a tool which uses the sniffer functionality to capture the packets using Python based code.
`sniffer.py` is the packet sniffer tool written in Python.

1) Steps to install scapy - Run the command: 
   
   `sudo python3 -m pip install --pre scapy[complete]`
   
   **Note-1: To check the interface of your machine, run the command: ifconfig(will be used as an input later!)**

2) After scapy installation, the next step is to run the packet sniffer tool - Run the command: 
   
   `sudo ./sniffer.py`

3) Enter the systems interface (Example: `enp0s3`)

4) Enter the experiment number to be performed (Example: `1` for Exp-1, `2` for Exp-2 and `3` for Exp-3)

   **Note-2: Experiment number will give the respective experiment csv files.**

5) Now, perform the experiment corresponding to the number entered.

6) The tool exits gracefully after 30 seconds and generate one of these CSV files (sniffer_aakriti_exp_1.csv/sniffer_aakriti_exp_2.csv/sniffer_aakriti_exp_3.csv) -- for respective experiment.

   **Note-3: Only the file named "sniffer_aakriti_exp_2.csv" is being submitted as per the requirement.**


**The important Modules used in the code which helped in the successful run are as follows:**

1) `subprocess` - It helped to establish the network interface to promiscuous mode which helps in capturing all the packets without discarding any unnecessary packets.
2) `sys` - used to exit the tool gracefully
3) `csv` - used to create CSV file
4) `scapy.all` - used to import necessary functions of the scapy module

------
### 2. On any Operating system using a simple virtual environment manager(no need of virtual box!). Steps are follow:

Requirements to run the code:
1. To clone this repo(it's private!), add github_username, github_password and remove `<>`.
   
   `git clone https://<github_username>:<github_password>@github.com/<github_username>/packet-manipulation-project.git`

2. You need Anaconda to create virtual environment,
   [please download the anaconda as per you OS](https://www.anaconda.com/products/individual)
   
Once you have Anaconda(virtual environment manager), you can follow the below steps:

1. To build virtual environment from scratch:
   and installing scapy python library in it!
   
    ```
    conda create --name packet_manipulation_env python=3.8
    conda activate packet_manipulation_env
    pip install scapy matplotlib
    ```
    or (**Note: avoid running below command of used above, it's simply another way to create virtual environment.)**
    to build virtual environment from generated requirement.txt file(`pip3 freeze > requirements.txt`)
   
    ```
    conda create --name <your_env_name> python=3.8
    conda activate <your_env_name>
    pip install -r ./requirements.txt
    ```

2. how run the `sniffer.py` code.
   - make sure the conda environment is activate
   `(packet_manipulation_env)...$`
   - run the python interpreter with sudo access from [packet-manipulation-project directory](packet-manipulation-project/)
     
      `sudo python src/sniffer.py`
   
   ------------------------------------
      
      *** Please check the data/sniffer_aakriti_exp_2.csv file to see the results.
      Packet Sniffer program exits.
   ```

   credits: project done in a group of two with AshwinKumarMuniswamy
