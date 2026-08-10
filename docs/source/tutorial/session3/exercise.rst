Exercises
-----------------

Exercise 4
^^^^^^^^^^^^^^^^^

.. admonition:: Exercise
   :class: todo

   **Time:** 15 min

   These use the ``file.txt`` and ``my_directory`` you copied up to Gadi in the File Transfer section, so
   run that first if you have not already.

   * Copy the file ``file.txt`` from Gadi back to your local machine using ``scp``.
   * Copy the directory ``my_directory`` from Gadi back to your local machine using ``scp``.

.. admonition:: Hints
   :class: hint

   * Copying *from* Gadi is the same command with the two arguments swapped: the remote path comes first,
     the local destination second.
   * ``.`` is a valid destination, meaning "the directory I am currently in".
   * Remember ``-r`` for the directory, and connect to ``gadi-dm.nci.org.au``.

Exercise 5
^^^^^^^^^^^^^^^^^

.. admonition:: Exercise
   :class: todo

   **Time:** 20 min

   I have a program that is 30% parallel and 70% sequential. Use Amdahl's Law to calculate the speedup I
   can expect if I run it on:

   * 4 cores
   * 8 cores

.. admonition:: Answer
   :class: hint

   Amdahl's Law with :math:`P = 0.3`:

   .. math::

       S = \frac{1}{(1 - 0.3) + \frac{0.3}{N}} = \frac{1}{0.7 + \frac{0.3}{N}}

   * 4 cores: :math:`S = 1 / (0.7 + 0.075) = 1.29`
   * 8 cores: :math:`S = 1 / (0.7 + 0.0375) = 1.36`

   Doubling the cores bought only 5% more speed. Even with infinite cores this program cannot exceed
   :math:`1 / 0.7 = 1.43`, so the 70% sequential portion — not the core count — is what limits it.

Exercise 6
^^^^^^^^^^^^^^^^^

.. admonition:: Exercise
   :class: todo

   **Time:** 10 min

   * Run the job ``parallel.pbs`` in ``hpc101/session_3``. It runs the program ``parallel.py``.

   * What is the output of the job?

.. admonition:: Hints
   :class: hint

   * Edit ``-P`` and ``-l storage=`` to name your own project first, as you did in Session 2.
   * The output is not printed to your terminal. Look for ``parallel.o<jobid>`` in the directory you
     submitted from.
   * The job requests ``ncpus=48``. Compare that with the thread count the program reports, and with the
     speedup it achieves — they are not the same number, and the gap is what the rest of this session
     is about.
