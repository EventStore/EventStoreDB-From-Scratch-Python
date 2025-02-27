# Instructions: Migrating to KURRENTDB cloud

## Overview

KurrentDB can run in the cloud. This option is a popular choice among our customers because the infrastructure is managed by Kurrent. Availability in multiple regions is built in, and processes such as scheduled backups are easy to configure. 

If you register for a cloud account and create a KurrentDB cluster, you could follow these steps and run the code in github codespaces against a KurrentDB cloud cluster.

Information on Kurrent Cloud is available at [https://kurrent.io/Kurrent-cloud](https://www.kurrent.io/kurrent-cloud)  

## Step 1: Create a Cluster with Remote Access Enabled

Kurrent Cloud allows the creation of both dedicated and shared clusters.

Note that "shared" in this case means, "running on our kubernetes infrastructure". Your cluster is isolated and can only be used by authorized accounts in your organization. 

![cluster selector](./images/create_shared_cluster.png)


### Public Access Security Notes

This cluster is secured in the following ways.

A unique username and password for the administrator account for that cluster is generated when the cluster is created.

A list of IP addresses that can access the cluster must be created, the default access list is empty.

## Step 2: Determine your codespace IP address 

GitHub codespaces are docker containers running on private networks in GitHub's datacenters. 

Web access for the codespace web interface is routed through to the internal docker containers. Running a command like `ipconfig`, that would work in most instances will not help us when ran in codespaces, as it will return the local, non publicly routable address. 

A remote request from codespaces to an external resource, such as a website, will expose the currently used public IP address. 

A shell script `find_my_IP.sh` is included. 

Run that script to return the IP address currently used by your codespace container. 

:warning: 
Your codespace IP will change, if there is no activity for a long period of time (tens of minutes), or if the codespace is stopped and restarted. This IP is assigned out of a pool of addresses by github, the IP address your codespace has today, may be in use by some other codespace tomorrow. You should remove the IP address from your cluster's access list when you terminate your codespace. 

In a terminal enter the command.
`./find_my_IP.sh`

Your IP address will be displayed to the terminal, 
`Your IP address is 11.111.111.115 enter this in the access list on Kurrent Cloud`

Your IP address will also be written to the file `my_IP.txt`

## Step 3: Enter your IP address into the Kurrent Cloud clusters IP access list

![cluster selector](./images/Edit_access_list.png)


## Step 4: Use the Kurrent Cloud Console to Generate a Connection String

Click the `connect to <cluster_name>` button.

![cluster selector](./images/Connect_step1.png)

Choose your language, in this case python.

![cluster selector](./images/Connect_step2.png)

Copy the generated connection string.

![cluster selector](./images/Connect_step3.png)

:warning: 
This connection string includes the admin password. Do not share this in public forums, or public github repositories.

## Step 5:

Comment out the line 

```
client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false")
```

And add the line copied in step 4

```
client = EventStoreDBClient(
    uri="esdb+discover://admin:6906b7791d76454bb4fae6faf590ab06@kurrentdb.curr4icgdub1aodg1sh0.cui3cs4gduba0bunfq60.sites.platform.eventstore.cloud:2113"
)
```

## Step 6: Append an event to verify

`python sample_append.py`


## Congratulations you have modified the client connection string to connect to a Kurrent Cloud cluster !!