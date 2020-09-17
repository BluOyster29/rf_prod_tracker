# rf_prod_tracker
Script for tracking annotation progress

## Description 
Just a little code i made to track my progress whilst annotating a dataset. You just enter in some information and it will calculate some averages etc and print it out. 

### Args 
`start_tag`     : How much of the dataset is tagged when you begin

`end_tag`       : How much of the dataset is tagged when you are finished 

`sesh_hours`    : How many hours you have spent this session 

`hours`         : Total hours spent on dataset 

`--data_path`   : Where you want to save a csv file

`--total_frags` : Total number of examples in the dataset

### Example Output
The program can output a csv file with some basic statistics as well as print it to terminal

`python3 prod_tracker.py 4949 5250 24 2`

> 301 tagged

> 150 tagged an hour this sesh

> 219 tagged an hour overall on average

> 5731 fragments left to tag

> 26 hours to go on dataset


