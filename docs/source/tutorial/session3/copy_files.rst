File Transfer
------------------

.. admonition:: Overview
   :class: Overview

    * **Time:** 20 min

      #. Learn how to copy files between your local machine and the HPC cluster.
      #. Understand how to use Secure Copy Protocol (SCP) for file transfers.

In this section, we will learn how to copy files between your local machine and the HPC cluster. 
This is essential for transferring data, scripts, and results. 

Secure Copy Protocol (SCP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SCP is a secure method for transferring files between your local machine and the HPC cluster.
It uses SSH for data transfer, ensuring that your files are encrypted during the transfer process.

To copy a file from your local machine to the HPC cluster, use the following command:

.. code-block:: bash
   :linenos:

   scp /path/to/local/file username@hpc-cluster:/path/to/remote/directory

To copy a file from the HPC cluster to your local machine, use:

.. code-block:: bash
   :linenos:

   scp username@hpc-cluster:/path/to/remote/file /path/to/local/directory

.. admonition:: Explanation
   :class: attention

   * Replace ``/path/to/local/file`` with the path to the file on your local machine.
   * Replace ``username@hpc-cluster`` with your username and the address of the HPC cluster.
   * Replace ``/path/to/remote/directory`` with the path to the directory on the HPC cluster where you want to copy the file.
   * Similarly, adjust paths for copying files from the HPC cluster to your local machine.


For Linix and MacOS users, the ``scp`` command is available by default in the terminal.

.. code-block:: bash
   :linenos:

    # Change to Downloads directory     
    cd $HOME/downloads

    # Create a test file
    touch file.txt

    # Securely copy the file to Gadi
    scp file.txt <username>@gadi.nci.org.au:/scratch/<project>>/<username>/

This copies a file named ``file.txt`` from your local ``downloads`` directory to your scratch directory on Gadi.


For Windows users, you can use tools like PuTTY or WinSCP to perform SCP operations. All the latest versions of
Windows also support the ``scp`` command in the Command Prompt or PowerShell.

.. code-block:: bash
   :linenos:

    # Change to Downloads directory
    cd C:\Users\<username>\Downloads

    # Create a test file
    echo "This is a test file." > file.txt

    # Securely copy the file to Gadi
    scp file.txt <username>@gadi.nci.org.au:/scratch/<project>>/<username>/


To copy a directory and its contents, use the ``-r`` option with ``scp``:

.. code-block:: bash
   :linenos:

    scp -r /path/to/local/directory username@hpc-cluster:/path/to/remote/directory

In Linux and MacOS, do this:

.. code-block:: bash
   :linenos:

    # Change to Downloads directory
    cd $HOME/downloads

    # Create a new directory
    mkdir my_directory

    # Navigate into it
    cd my_directory

    # Create multiple empty files
    touch file1.txt file2.txt

    # Go back to Downloads directory
    cd ..

    # Securely copy the directory to Gadi
    scp -r my_directory <username>@gadi.nci.org.au:/scratch/<project>>/<username>/

In Windows, you can do the same with:


.. code-block:: bash
   :linenos:

    # Change to Downloads directory
    cd "$env:USERPROFILE\Downloads"

    # Create a new directory
    mkdir my_directory

    # Navigate into it
    cd my_directory

    # Create multiple empty files
    echo "This is a test file1." > file1.txt
    echo "This is a test file2." > file2.txt

    # Go back to Downloads directory
    cd ..

    # Securely copy the directory to Gadi
    scp -r my_directory <username>@gadi.nci.org.au:/scratch/<project>/<username>/

.. important::
    Ensure that you have the necessary permissions to read/write files in the specified directories on both 
    your local machine and the HPC cluster.

.. admonition:: Key Points
   :class: hint

   * Use ``scp`` to securely copy files between your local machine and the HPC cluster.
   * The ``-r`` option allows you to copy directories recursively.
