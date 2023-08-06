# RUNCRAWLER

**Runcrawler** is a monitoring tool on software-usage based on data extraction.

Parallel computing program such as CFD-solver often run on different clusters, by different users. It is hard for managers to get a big picture on how the program is used. **run crawler** is a tool to monitor their usage and allow managers to get a various type of useful information by extracting data related to the execution of the program.

Here are some examples of questions which managers often have. </br>
- What are the typical errors repeated by the users of my team ? </br>
- Are our runs efficient in terms of CPU time ? </br>
- If so, are they related to a certain parameter setting ? </br>

As an example, this chart pie shows the percentage of runs that are converged versus the runs
that did not converge and on the side, the code associated to the reason it 
crashed (0 if it exited fine, 300 if not in that case)


<p align="center"> 
    <img src=https://cerfacs.fr/coop/images/runcrawler/error_log.png width=300>
</p>



**Runcrawler** can return the error codes associated to crashes and improve 
your understanding.


## Installation
**runcrawler** is available by simple execution of

pip install runcrawler

## How to use

Use the CLI 

**runcrawler scan-log path/to-your-file**.

This will return a code corresponding to the reason why your run crashed.

## To go further

Read [further](https://cerfacs.fr/coop/runcrawler)


