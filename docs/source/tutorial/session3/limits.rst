Limits of Parallelism
----------------------

.. admonition:: Overview
   :class: Overview

    * **Time:** 30 min

    #. Understand the limits of parallelism in High-Performance Computing (HPC).
    #. Learn about Amdahl's Law and Gustafson's Law, which describe the limits of parallel processing.

In High-Performance Computing (HPC), while parallelism is a powerful tool for improving performance, it has its 
limits. Understanding these limits is crucial for effectively designing and optimizing parallel applications.
These limits can be broadly categorized into two types: **Amdahl's Law** and **Gustafson's Law**.

Amdahl's Law
^^^^^^^^^^^^^^^^^^^^^^^

Amdahl's Law states that the maximum speedup of a program using parallel processing is limited by the sequential 
portion of the program. It can be expressed mathematically as:

.. math::

    S = \frac{1}{(1 - P) + \frac{P}{N}}

where:

* :math:`S` is the maximum speedup,
* :math:`P` is the parallelizable portion of the program (between 0 and 1),
* :math:`N` is the number of processors.

This means that even with an infinite number of processors, the speedup is limited by the fraction of the 
program that cannot be parallelized. For example, if 90% of a program can be parallelized, the maximum speedup 
is:

.. math::

    S = \frac{1}{(1 - 0.9) + \frac{0.9}{N}} = \frac{1}{0.1 + \frac{0.9}{N}}

As :math:`N` approaches infinity, the speedup approaches 10x, indicating that the sequential portion limits the 
overall performance gain.

Gustafson's Law
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gustafson's Law, on the other hand, argues that as the problem size increases, the parallel portion of the 
program also increases, leading to better scalability. It can be expressed as:

.. math::

    S = N - (1 - P) \cdot (N - 1)

where:

* :math:`S` is the speedup,
* :math:`N` is the number of processors,
* :math:`P` is the parallelizable portion of the program.

.. warning::

   The symbol :math:`P` does **not** mean the same thing in the two laws, and this is the single most
   common point of confusion.

   * In **Amdahl's Law**, :math:`P` is the parallel fraction of a **fixed** problem — the same work, run on
     more processors.
   * In **Gustafson's Law**, :math:`P` is the parallel fraction measured on the **parallel machine**, where
     the problem has been scaled up to match the extra processors.

   They are answers to two different questions, which is why the same program appears to yield two
   different speedups.

This law suggests that as we increase the problem size, we can achieve better speedup with more processors.
For example, if we have 100 processors and 90% of the run on the parallel machine is parallelizable, the
speedup is:

.. math::

    S = 100 - (1 - 0.9) \cdot (100 - 1) = 100 - 0.1 \cdot 99 = 100 - 9.9 = 90.1


This indicates that as the problem size grows, the speedup can approach the number of processors, making parallel
computing more effective. Understanding these limits helps in designing efficient parallel algorithms and 
systems. 

While Amdahl's Law highlights the constraints imposed by the sequential parts of a program,
Gustafson's Law emphasizes the potential for scalability with larger problem sizes.

.. important::

    Scalability refers to a system's ability to handle increased load or growth—such as more users, data, or
    tasks—without sacrificing performance, reliability, or manageability.

Strong and Weak Scaling
^^^^^^^^^^^^^^^^^^^^^^^^^

The two laws correspond to the two ways of measuring how well a program scales, and these are the terms you
will meet in practice:

* **Strong scaling** — keep the problem size **fixed** and add processors. How much faster does it finish?
  This is the question Amdahl's Law answers, and the sequential fraction sets a hard ceiling on the result.
* **Weak scaling** — grow the problem size **in step with** the processors, so each processor keeps the same
  amount of work. Does the runtime stay constant? This is the question Gustafson's Law answers.

Many problems that scale poorly in the strong sense scale perfectly well in the weak sense, so it matters
which one you are claiming when you report that a code "scales".

Exercise 7 measures the strong scaling of a real program on Gadi, so you can see the curve bend away from
the ideal for yourself.

Other Practical Limits
^^^^^^^^^^^^^^^^^^^^^^^^

Neither law accounts for the costs that dominate real applications on real hardware:

* **Communication overhead** — processors must exchange data, and across nodes that traffic crosses the
  network. Past a certain point, adding processors adds more communication than computation.
* **Load imbalance** — a parallel step finishes only when its slowest worker does, so unevenly divided work
  leaves cores idle.
* **Memory bandwidth** — cores on a node share a path to memory. A program limited by data movement rather
  than arithmetic will stop speeding up long before it runs out of cores.
* **Synchronisation** — locks and barriers serialise parts of a program that look parallel on paper.

In practice these are usually what stops a program scaling, well before the sequential fraction does.


.. admonition:: Key Points
   :class: hint

   1. Amdahl's Law limits speedup based on the sequential portion of a fixed-size program.
   2. Gustafson's Law emphasizes scalability with larger problem sizes.
   3. :math:`P` means something different in each law, so the two are not directly comparable.
   4. Strong scaling fixes the problem size; weak scaling grows it with the processor count.
   5. Communication, load imbalance, memory bandwidth and synchronisation are usually the limits you hit
      first in practice.
