Interactive Jobs
--------------------

.. admonition:: Overview
   :class: Overview

    * **Time:** 20 min

    #. Learn how to run interactive jobs on Gadi.
    #. Understand the benefits of interactive jobs compared to batch jobs.

Interactive jobs allow you to run commands directly on the compute nodes, providing a more interactive experience
compared to batch jobs. This is particularly useful for tasks that require user input or real-time feedback.
To start an interactive job on Gadi, you can use the ``qsub`` command with the ``-I`` option. This will allocate 
resources for an interactive session.

.. code-block:: bash
   :linenos:

    qsub -I -q normal -P vp91 -l walltime=00:10:00,ncpus=1,mem=4GB,storage=scratch/vp91

In this command:
    * ``-I``: This option indicates that you want to start an interactive job.
    * ``-q normal``: Specifies the queue to use for the job, in this case, the ``normal`` queue.
    * ``-P vp91``: Specifies the project code for the job.
    * ``-l walltime=00:10:00,ncpus=1,mem=4GB,storage=scratch/vp91``: Requests the resources for the job —
      10 minutes of wall time, 1 CPU core, 4 GB of memory, and access to the project's ``/scratch`` storage.
      Several resources can be given to a single ``-l`` option as a comma-separated list, which is what we
      do here; you could equally write them as separate ``-l`` options.

.. warning::

   Replace ``vp91`` with your own project code in both ``-P`` and ``storage=``. Without the ``storage``
   resource your interactive session cannot read ``/scratch``, which is where the course material lives.

After submitting the command you will wait in the queue, and then be dropped into a shell on one of the
compute nodes. Only once you see that new prompt do you start typing your own commands — for example:

.. code-block:: bash
   :linenos:

    module load python3/3.11.0
    which python3

To exit the interactive session, simply type ``exit`` or press ``Ctrl+D``. This will terminate the interactive
job and return you to your original shell.

Interactive or Batch?
^^^^^^^^^^^^^^^^^^^^^^

Interactive jobs are convenient, but they are not the right tool for everything:

* Use an **interactive** job when you are developing, debugging, or exploring — anything where you need to
  see a result before deciding what to do next.
* Use a **batch** job for work you already know how to run, for anything long, and for anything you want to
  queue up and forget about.

.. important::

   An interactive job is tied to your terminal. If your SSH connection drops, the job is killed and any
   unsaved work in it is lost. You are also charged for the whole time you hold the allocation, including
   the time you spend thinking at the prompt — so do not leave an idle interactive session open.



.. admonition:: Key Points
   :class: hint

   * Interactive jobs allow you to run commands directly on the compute nodes, providing a more interactive experience compared to batch jobs.
   * Interactive jobs are useful for tasks that require user input or real-time feedback.
   * Start one with ``qsub -I``, and leave it with ``exit`` or ``Ctrl+D``.
   * Request ``storage=`` for any filesystem you need, just as you would in a batch job.
   * An interactive job dies with your SSH connection, and bills you while it sits idle.
