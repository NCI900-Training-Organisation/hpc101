
Directories and Environment Variables
---------------------------------------


.. admonition:: Overview
   :class: Overview

    * **Time:** 15 min

    #. Learn about the directories you will need to work with on Gadi.
    #. Understand the environment variables that are set automatically when you log in to the system.

In this section, we will explore the directories you will need to work with on Gadi. Understanding these 
directories is crucial for managing your files and data effectively.

Home directory is unique to each user and is where you can store your personal files, scripts, and data.


.. code-block:: bash
   :linenos:

    echo $HOME


.. admonition:: Explanation
   :class: attention

   Here ``$HOME`` is an environment variable that points to the user's home directory.
   The value in ``$HOME`` is set automatically when you log in to the system, and it is unique to each user.


.. code-block:: bash
   :linenos:

    cd $HOME


`$USER` is an environment variable that contains the username of the currently logged-in user.
This is also unique to each user and is set automatically when you log in to the system.

.. code-block:: bash
   :linenos:

    echo $USER


Each user belongs to one or more projects on Gadi. You can only access the files and directories that belong to
your project(s). ``$PROJECT`` holds your **default** project — the one your jobs are charged to unless you say
otherwise:

.. code-block:: bash
   :linenos:

    echo $PROJECT

.. admonition:: Explanation
   :class: attention

   ``$PROJECT`` is a single value, so it does **not** list every project you belong to. To see all of them,
   list your group memberships instead:

   .. code-block:: bash

       groups

   Each project you are a member of appears as one group code.

Scratch directory is a high-performance storage area designed for temporary data storage during computations.
It is typically used for storing intermediate results, large datasets, or files that are not needed long-term.
Each project has its own sub directory in the scratch area, which is accessible to all members of the project.

.. code-block:: bash
   :linenos:

    cd  /scratch/$PROJECT
    pwd

Inside the scratch directory you have your own subdirectory for your files. It is normally created for you
already, so ``mkdir -p`` here simply succeeds without doing anything.

.. code-block:: bash
   :linenos:

    mkdir -p $USER
    cd $USER
    pwd

.. warning::

   ``/scratch`` is **temporary** storage. Files that have not been accessed for 100 days are automatically
   purged. Never leave data you care about on ``/scratch`` — move it to ``/g/data`` or off the system.

Project data directory (``/g/data``) is persistent storage for data your project needs to keep. Unlike
``/scratch`` it is not purged, so this is where curated datasets and results belong. Not every project has a
``/g/data`` allocation.

.. code-block:: bash
   :linenos:

    ls -d /g/data/$PROJECT

You can check how much space and compute your project has used with:

.. code-block:: bash
   :linenos:

    nci_account -P $PROJECT
    lquota


You can also set your own environment variable.

.. code-block:: bash
   :linenos:

    export MYDIR=$HOME/mydir
    echo $MYDIR
    mkdir -p $MYDIR
    cd $MYDIR
    pwd

and also clear it when you are done.

.. code-block:: bash
   :linenos:

    unset MYDIR
    echo $MYDIR


Now you can clone the course repository to your home directory or scratch directory.

.. code-block:: bash
   :linenos:

    cd  /scratch/$PROJECT/$USER
    pwd
    git clone https://github.com/NCI900-Training-Organisation/hpc101.git


.. admonition:: Key Points
   :class: hint
   
   * The home directory is unique to each user and is where you can store your personal files, scripts, and data.
   * The ``$HOME`` environment variable points to the user's home directory, and it is set automatically when you log in.
   * The ``$USER`` environment variable contains the username of the currently logged-in user.
   * The ``$PROJECT`` environment variable contains your **default** project only; use ``groups`` to list
     every project you belong to.
   * The scratch directory is a high-performance storage area for temporary data storage during computations,
     and files untouched for 100 days are purged from it.
   * ``/g/data`` is persistent project storage and is not purged — keep data you need there.