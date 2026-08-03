Modules
----------

.. admonition:: Overview
   :class: Overview

    * **Time:** 15 min

    #. Learn how to use modules to manage software on HPC systems.
    #. Understand how to load and unload modules.

.. note::

   These are the modules used over the course of this tutorial:

   1.  ``python3/3.11.0``
   2.  ``papi/7.0.1``
   3.  ``openmpi/4.0.1``
   4.  ``cuda/12.3.2``
   5.  ``gcc/14.2.0``

Finding Modules
^^^^^^^^^^^^^^^^^^^^^^^

Modules are how we manage software in most HPC machines. We can see all the available modules using the command

.. code-block:: bash
   :linenos:

    module avail

That is a long list. To narrow it down, give ``module avail`` the beginning of a module name and it will
list only the modules that start with those characters — here, everything starting with the letter "p":

.. code-block:: bash
   :linenos:

    module avail p

.. warning::

   Do not write ``module avail p*``. The ``*`` is a wildcard your **shell** expands before ``module`` ever
   sees it, so if the current directory happens to contain files beginning with ``p`` those filenames get
   passed to ``module`` instead. Use the plain prefix, or quote it as ``module avail 'p*'``.


Loading Modules
^^^^^^^^^^^^^^^^^^^^^^^

If we want to load a module ``python3/3.11.0`` we can use the command

.. code-block:: bash
   :linenos:

    module load python3/3.11.0


We can also load multiple modules at once.


.. code-block:: bash
   :linenos:

    module load papi/7.0.1 openmpi/4.0.1

.. tip::

   Always name the version you want, as we do here. If you write ``module load python3`` you get whichever
   version the system currently considers the default, and that can change underneath you — which makes
   results hard to reproduce.

Listing Loaded Modules
^^^^^^^^^^^^^^^^^^^^^^^

To see what you currently have loaded:

.. code-block:: bash
   :linenos:

    module list

This is the first thing to check when a command is not found, or when a module refuses to load because it
conflicts with something already in your environment.


Unloading Modules
^^^^^^^^^^^^^^^^^^^^^^^

If we want to unload the module use the command

.. code-block:: bash
   :linenos:

    module unload python3/3.11.0

We can unload all the modules using the command

.. code-block:: bash
   :linenos:

    module purge


.. admonition:: Key Points
   :class: hint

   * ``module avail``: This command lists all the available modules on the system; follow it with a prefix
     to filter the list.
   * ``module load <module_name>``: This command loads a specific module, making its software available for use.
   * ``module list``: This command shows the modules currently loaded in your environment.
   * ``module unload <module_name>``: This command unloads a specific module, removing its software from the environment.
   * ``module purge``: This command unloads every module at once.
   * Always load a specific version so your environment is reproducible.