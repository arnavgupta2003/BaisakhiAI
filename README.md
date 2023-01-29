
<H1 align = "center"> Baisakhi AI </H1>

This project aims to assist farmers in selecting the most suitable crop for their land by analyzing soil parameters and providing recommendations. 
By inputting data such as soil pH, nutrient levels, and climate conditions, the project will generate a list of crops that are best suited to those 
conditions, taking into account factors such as water requirements, temperature tolerance, and potential yield. This will help farmers to optimize 
their crop selection and improve the chances of a successful harvest, ultimately increasing their profitability and sustainability.

## `Tech Stack`
<ul>
  <li>Scikit-learn</li>
  <li>django</li>
  <li>Python</li>
  <li>Pandas</li>
  <li>Numpy</li>
  <li>HTML</li>
  <li>CSS</li>
  <li>BootStrap</li>
  <li>Tailwind CSS</li>
  <li>Javascript</li>
  <li>ReactJS</li>
  
</ul>  


## `Installation`

```console
# Clone the project
$> make -f Makefile
       OR
$> make
```
`Load the Module with PID as parameter`
```console
$> sudo insmod main.ko pid=(PID)

```
`Check Output`

```console
$> sudo tail -n 50 /var/log/syslog

```
`Unload the Module`

```console
$> sudo rmmod main

```
#### Implementation

For this Implementation the ```task_struct``` of the given ```PID``` is fetched using the ```pid_task(find_pid_ns(id, &init_pid_ns), PIDTYPE_PID);``` then the ```task_struct``` is read for the specific  ```PID``` and the output is dumped to the ```SYSLOG``` using the ```printk``` and read to the user space using the ```dmesg``` call.


<p align=center> --- EOF --- </p>
