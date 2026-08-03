Exercises
-----------------

Exercise 2
^^^^^^^^^^^^^^^^^

.. admonition:: Exercise
   :class: todo

   **Time**: 10 min

   1. Check if there is a module named ``python3/3.12.1`` available on Gadi.

   2. If available, load the module ``python3/3.12.1``.

   3. What happens when you try to load ``intel-mkl/2019.3.199`` after loading ``python3/3.12.1``?

.. admonition:: Hints
   :class: hint

   * ``module avail python3`` will narrow the list for step 1.
   * Run ``module list`` after each step to see what actually changed in your environment — a ``load`` does
     not always leave you with what you asked for.
   * Read the message from step 3 carefully rather than just noting that it failed. The module system knows
     which two modules are in conflict and will tell you.

Exercise 3
^^^^^^^^^^^^^^^^^

.. admonition:: Exercise
   :class: todo

   **Time**: 15 min

   Work on your **own copy** of the job script, so that the original stays intact:

   .. code-block:: bash

       cd /scratch/$PROJECT/$USER/hpc101/session_2
       cp test_job.pbs my_job.pbs

   Edit ``my_job.pbs`` so that ``-P`` and ``-l storage=`` name **your** project, and check that it submits
   successfully before you change anything else. Then:

   1. What happens if you request ``ncpus=50`` in the job script?
   2. What happens if you request ``mem=200GB`` in the job script?

.. admonition:: Hints
   :class: hint

   * Both requests are refused by ``qsub`` straight away, so you will not have to wait in the queue to see
     the result. Read the error message in each case.
   * Recall from the previous section that a standard Gadi node has **48 cores** and **192 GB of memory**,
     and that requests spanning more than one node must be a whole number of nodes.
   * Fix your project code first. A rejection for an invalid project looks nothing like a rejection for an
     invalid resource request, and it is easy to mistake one for the other.
