Job Scheduler
-----------------


.. admonition:: Overview
   :class: Overview

    * **Time:** 15 min

    #. Learn about the job scheduler used in HPC clusters.
    #. Understand the concept of batch scheduling and how it works.

HPC clusters like Gadi use a job scheduler to manage the execution of jobs. The job scheduler is responsible for 
queuing, scheduling, and executing jobs on the cluster. It ensures that resources are allocated efficiently 
and that jobs are executed in a timely manner.

.. image:: ./figs/jobsub.png
   :width: 600px
   :align: center
   :alt: Job Scheduler

The job scheduler in Gadi is called ``PBS (Portable Batch System) Pro``. It is a widely used job scheduler in HPC environments.
PBS allows users to submit jobs, monitor their status, and manage job queues. It provides a command-line interface 
for job submission and management.

There are several other job schedulers available, such as ``SLURM``, ``LSF``, and ``Grid Engine``. Each scheduler has its own features
and capabilities, but they all serve the same purpose of managing job execution on HPC clusters.

All the job schedulers use a concept called batch scheduling. In batch scheduling, jobs are submitted to a queue, 
and the scheduler allocates resources based on the job's requirements and the available resources in the cluster.
The scheduler prioritizes jobs based on various factors, such as job size, resource requirements, and 
user-defined priorities. 

.. admonition:: Key Points
   :class: hint

   * **Job Scheduler**: A system that manages the execution of jobs on an HPC cluster, allocating resources and scheduling jobs based on priority.
   * **Batch Scheduling**: A method of job scheduling where jobs are submitted to a queue and executed based on resource availability and job priority.
