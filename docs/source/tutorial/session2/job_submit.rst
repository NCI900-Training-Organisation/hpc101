Job Submission
-------------------

.. admonition:: Overview
   :class: Overview

    * **Time:** 30 min

    #. Learn how to submit jobs to the job scheduler.
    #. Understand the structure of a job script and its components.
    #. Learn how to check the status of submitted jobs.

In this section, we will learn how to submit jobs to the job scheduler. The job scheduler is responsible for 
managing and executing jobs on the cluster. It allocates resources, schedules jobs based on priority, and 
ensures efficient use of the cluster's computational power. Job submission is the process of sending a job 
to the job scheduler, which then queues the job for execution on the cluster.

Jobs are submitted to the job scheduler using a job script:

.. code-block:: bash
   :linenos:

    #!/bin/bash

    #PBS -N test_job
    #PBS -P vp91
    #PBS -q normal
    #PBS -l ncpus=1
    #PBS -l storage=scratch/vp91
    #PBS -l mem=4gb
    #PBS -l walltime=00:05:00
    #PBS -l wd

    module load python3/3.11.0

    which python3


.. warning::

   ``vp91`` is the project code used in these examples. **Replace it with your own project code** — in
   both ``-P`` and ``-l storage=`` — or your job will be rejected. Note that PBS does not expand shell
   variables inside ``#PBS`` lines, so you cannot write ``#PBS -P $PROJECT``; the code must be typed out.


Let's break down the job script:

    * ``#!/bin/bash``: This is the shebang line that tells the system to use the Bash shell to execute the
      script. It must be the **very first line** of the file — a blank line above it turns it into an
      ordinary comment.
    * ``#PBS -N test_job``: This line sets the name of the job to ``test_job``. This name will be used to identify the job in the queue.
    * ``#PBS -P vp91``: This line specifies the project code (in this case, ``vp91``) that the job belongs to.
    * ``#PBS -q normal``: This line specifies the queue to which the job will be submitted. The ``normal`` queue is typically used for standard jobs.
    * ``#PBS -l ncpus=1``: This line requests 1 CPU core for the job.
    * ``#PBS -l storage=scratch/vp91``: This line requests access to the project's ``/scratch`` storage. Without it the job cannot read or write ``/scratch``, even though you can from the login node. Use ``gdata/vp91`` for ``/g/data``, and separate multiple entries with ``+``.
    * ``#PBS -l mem=4gb``: This line requests 4 GB of memory for the job.
    * ``#PBS -l walltime=00:05:00``: This line specifies the maximum wall time for the job, which is 5 minutes in this case.
    * ``#PBS -l wd``: This line sets the working directory for the job to the directory from which the job was submitted.
    * ``module load python3/3.11.0``: This line loads the Python module version 3.11.0, which is required for the job.
    * ``which python3``: This line prints the path to the Python executable that will be used in the job.



.. admonition:: Explanation
   :class: attention

   * There are various queues available on Gadi, such as ``normal``, ``express``, and ``gpuvolta``.
   * Each queue has different resource limits and priorities.
   * The ``normal`` queue is typically used for standard jobs.
   * Each job should be submitted to a specific queue through a specific project.
   * The project code is used to track resource usage and billing for the job. Compute is charged in
     **Service Units (SU)**, and the rate depends on the queue you use.


.. admonition:: Explanation
   :class: attention

   * A Gadi normal queue node (Intel Cascade Lake) has 48 cores and 192 GB of memory.
   * Requesting ``ncpus=48`` therefore asks for every core on a single node, and requests larger than 48
     must be a multiple of 48 because they span whole nodes.
   * If you request the x number of nodes you are charged for x number of nodes, whether or not you use all the cores.
   * Ask only for what you need. A small request like ``ncpus=1`` starts much sooner than a whole node,
     which matters when everyone in a workshop submits at once.


To submit the job script, you can use the ``qsub`` command:

.. code-block:: bash
   :linenos:

    cd /scratch/$PROJECT/$USER/hpc101/session_2
    cat test_job.pbs
    qsub test_job.pbs


.. admonition:: Explanation
   :class: attention

   * This command submits the job script ``test_job.pbs`` to the job scheduler.
   * The job will be queued and executed when resources become available.
   * ``qsub`` prints the **job ID** of the new job. Keep it — you need it to check on the job and to find
     its output later.


You can check the status of your job using the ``qstat`` command:


.. code-block:: bash
   :linenos:

    qstat -u $USER


.. admonition:: Explanation
   :class: attention

   * This command lists all the jobs submitted by the current user.
   * You can see the job ID, name, user, state, and other details.



The different states of a job can be:

* ``Q``: Queued - The job is waiting for resources to become available.
* ``R``: Running - The job is currently running on the cluster.
* ``E``: Exiting - The job is in the process of exiting.
* ``H``: Held - The job is held and will not run until it is released.
* ``S``: Suspended - The job has been suspended by the scheduler.
* ``F``: Finished - The job has completed, successfully or otherwise.

.. note::

   A finished job **disappears from plain** ``qstat``. If your job vanishes, it has not been lost — it has
   finished. Use ``-x`` to include finished jobs, and ``-f`` for the full detail of one job, which is what
   you need to work out why a job failed or has not started:

   .. code-block:: bash

       qstat -xu $USER
       qstat -f <jobid>

Getting the Output of Your Job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A batch job is not attached to your terminal, so anything it prints is written to files instead. When the
job finishes, PBS creates two files named after the job name and job ID:

* ``test_job.o<jobid>`` — everything the job wrote to standard output.
* ``test_job.e<jobid>`` — everything the job wrote to standard error.

Because the job script uses ``#PBS -l wd``, these appear in the directory you submitted from:

.. code-block:: bash
   :linenos:

    ls test_job.*
    cat test_job.o*

The ``.o`` file is where you will find the output of ``which python3``. The ``.e`` file is the first place
to look when a job does not do what you expected. On Gadi the ``.o`` file also ends with a resource usage
summary, showing the walltime, memory and Service Units the job actually consumed.

Cancelling a Job
^^^^^^^^^^^^^^^^^

If you submit a job by mistake, or it is queued for longer than you want to wait, delete it with ``qdel``
and the job ID from ``qstat``:

.. code-block:: bash
   :linenos:

    qdel <jobid>


.. admonition:: Key Points
   :class: hint

   * ``qsub`` is the command used to submit a job script to the job scheduler.
   * ``qstat`` is the command used to check the status of jobs in the queue; add ``-x`` to see
     finished jobs and ``-f <jobid>`` for full detail.
   * ``qdel <jobid>`` cancels a queued or running job.
   * A job's output is written to ``<jobname>.o<jobid>`` and its errors to ``<jobname>.e<jobid>``.
   * Request only the resources you need, and remember to use your own project code.
