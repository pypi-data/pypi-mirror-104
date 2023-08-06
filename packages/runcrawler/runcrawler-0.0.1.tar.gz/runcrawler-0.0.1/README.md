# RUNCRAWLER

**Runcrawler** is a monitoring tool on software-usage based on data extraction.

Parallel computing program such as CFD-solver often run on different clusters, by different users. It is hard for managers to get a big picture on how the program is used. **run crawler** is a tool to monitor their usage and allow managers to get a various type of useful information by extracting data related to the execution of the program.

Here are some examples of questions which managers often have. </br>
- What are the typical errors repeated by the users of my team ? </br>
- Are our runs efficient in terms of CPU time ? </br>
- If so, are they related to a certain parameter setting ? </br>

**Runcrawler** can answer those questions.


## How it works
Here are the major steps of the functioning.

1/ Retrieve files related to the execution of the program (ex. parameter-configuration/result/log files) from the cluster where users run the program. Stock this raw databases in the sever of monitoring. This should be done by users outside of **runcrawler**.

2/ On the sever of monitroing, **runcrawler** reads the raw databases, then parses them and take only interesting infomation to monitor (ex. creation-time, CPU-time, version of the program). Then it stocks that parsed data as *JSON* format.

3/ Transform the data from *JSON* format into *pandas*. 

5/ Aggregate the data of your interest by a simple coding of *MongoDB*/*pandas* command depending on your choice. This can be done directly using the *MongoDB Compass GUI* on end clients too (e.g. your personal computer). <span style="color:red">(à réflechir)</span>

## Installation
**runcrawler** is available by simple execution of

```
git clone git@nitrox.cerfacs.fr:open-source/runcrawler.git
```

Then, go into ```runcrawler``` directory to install *runcrawler* :

```
python setup.py install
```

## How to use

Specify the path to the directry to mine data in ```runcrawler.py```.

```
root = "/archive/cfd/user_name"
```
Run the script ```runcrawler.py```. This corresponds to the step 2 and 3 of the functioning in the "How it works" section.

```
python runcrawler.py
```



## Use case - Error categorization of AVBP's run
An error categorization of AVBP's run will be explained as an example here.
So far two options are possible.

#### Pymongo (mongoDB API on python) ####
A series of piplines to show run error categorization is already coded in ```error_rate.py``` via API *pymongo*. Just execute it.

```python error_rate.py```

You should get a pie-chart (```err_type.png```) as below.

<p align="center">
    <img  width="50%" src="./images/err_type.png" alt>
    <br />
    <em>Error categorization of AVBP's run</em>
</p>

#### Jupyter Notebook ####
```HPC_statistics_nb.ipynb``` is available to execute the same operations as above. This notebook is based on *pandas* library. It allows to get statistics on the runs, such as the user habits and HPC statistics.

### Exploratory data analysis on the data

The jupyter notebook takes all json files in the DATABASE folder and creates a pandas dataframe where each line corresponds to a run.


<p align="center">
    <img  width="80%" src="./images/pandas_dataframe.png" alt>
    <br />
</p>  

Then it performs some treatment on the data such as dealing with the NaN values by replacing them by 0 when it is relevant for example or by dropping lines that will not be possible to use. Lines that contain a few occurences of NaN data are droppped, others are filled with 0.0.

<p align="center">
    <img  width="30%" src="./images/isnan.png" alt>
    <br />
</p>  

We divide the dataframe into two separate dataframes, the first one containing data that were setup by the user, shown here:

<p align="center">
    <img  width="30%" src="./images/setup_params.png" alt>
    <br />
</p>

the other one gathers parameters read from the log file from the code, and give more info about the run itself, how long it lasted, how many iterations were run.


<p align="center">
    <img  width="20%" src="./images/log_params.png" alt>
    <br />
</p>

### Results

The runs can be classified by user and time when they were created, they can be classified by year, month but also hour to determine when the user launches most runs.

<p align="center">
    <
mg  width="60%" src="./images/when_month_user.png" alt>
    <br />
</p>

We can easily see on this pie chart the repartition of runs gathered from each user in the json files we got from the Database folder.

<p align="center">
    <img  width="30%" src="./images/runs_by_user.png" alt>
    <br />
</p>

Then we can output how many runs per kind of mixture, LES model, artificial viscosity model, mesh nodes were launched: for example here, the runs are classified by dimension and mixture name, to see if all mixtures were tested on both dimensions for example for better run management.

<p align="center">
    <img  width="50%" src="./images/mixture_dimension.png" alt>
    <br />
</p>

Here we see the HPC user habits, by having a glance at how many processors were run on and what ncgroup parameters were chosen. For an HPC expert, this is prior information to help the user optimize runs.

<p align="center">
    <img  width="50%" src="./images/MPI_ncell.png" alt>
    <br />
</p>



We compute the efficiency of the run which is defined by the time spent by one processor to compute one mesh node. This metric is used to compare the performance between machines. The figure below shows the efficiency for 2D and 3D runs, we can see the efficiency gets better in both dimensions by raising the number of MPI processors.

<p align="center">
    <img  width="50%" src="./images/efficiency.png" alt>
    <br />
</p>


