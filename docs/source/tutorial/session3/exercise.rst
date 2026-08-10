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
     speedup it achieves — they are not the same number, and the gap is what Exercise 7 is about.
   * The program breaks its speedup into two parts. Only the second is due to threads: the first comes
     from ``parallel=True`` changing the code Numba generates, which happens even on one core.

Exercise 7
^^^^^^^^^^^^^^^^^

.. admonition:: Exercise
   :class: todo

   **Time:** 20 min

   Exercise 6 gave you a speedup on 48 cores that was much smaller than 48. This exercise measures where
   it goes.

   * Run the job ``scaling.pbs`` in ``hpc101/session_3``. It runs ``scaling.py``, which times the same
     parallel function on 1, 2, 4, 8, 16, 24 and 48 threads with the problem size held fixed.

   * Sketch the speedup column against the thread count. Where does the curve start to bend away from the
     straight line you would get if speedup equalled the number of threads?

   * At 48 threads, what fraction of the ideal 48x did you actually achieve?

   * Now look at the resource summary at the end of the ``.o`` file. Compare ``CPU Time Used`` against
     ``NCPUs Requested`` multiplied by ``Walltime Used``. What fraction of the CPU time you were charged
     for did the job actually use?

.. admonition:: Hints
   :class: hint

   * Holding the problem size fixed while adding cores is **strong scaling** — the regime Amdahl's Law
     describes. The efficiency column is the speedup divided by the thread count.
   * Every row runs the identical function, so this table measures threading alone, with no compiler
     effect mixed in.
   * The last question is the important one. The parallel loop takes a fraction of a second, but the job
     also spends time loading modules, activating the virtual environment, starting Python and compiling
     the functions — and all of that is serial. Amdahl's Law applies to the whole job, not just the loop
     you were timing.
   * A loop that runs 6x faster inside a job that is mostly serial startup makes almost no difference to
     how long the job takes, or to what it costs you.
