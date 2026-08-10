Parallelism in HPC
----------------------------

.. admonition:: Overview
   :class: Overview

    * **Time:** 20 min

    #. Understand the concept of parallelism in High-Performance Computing (HPC).
    #. Learn about different levels of parallelism, including vector parallelism, multi-core parallelism, distributed parallelism, and GPU parallelism.

In this section, we will explore the concept of parallelism in High-Performance Computing (HPC). Parallelism 
is the ability to perform multiple computations simultaneously, which is essential for achieving high performance 
in HPC applications. Parallelism can be achieved through various means, including the use of multiple threads, 
processes, and distributed systems.

You will hear the word ``concurrency`` and ``parallelism`` used interchangeably, but they are not the same. 
Concurrency refers to the ability of a system to handle multiple tasks at once, but not necessarily 
simultaneously. Parallelism, on the other hand, refers to the simultaneous execution of multiple tasks. 

.. important::

    All parallel tasks are concurrent, but not all concurrent tasks are parallel.


Threads and Processes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In parallel computing, a ``thread`` is the smallest unit of processing that can be scheduled by an operating system.
A ``process`` is a program in execution, which can contain multiple threads. Threads within a process share the 
same memory space, allowing for efficient communication and data sharing.


``Threads`` are lightweight compared to ``processes``, as they share the same memory space and resources of the parent 
``process``. This allows for faster context switching and communication between ``threads``. ``Processes``, on the other 
hand, are independent entities with their own memory space. 



.. list-table:: Difference Between Process and Thread
   :widths: 25 35 40
   :header-rows: 1

   * - Feature
     - Process
     - Thread
   * - Definition
     - Independent program with its own memory space and resources.
     - Lightweight unit of execution within a process.
   * - Memory
     - Has separate memory space.
     - Shares memory space with other threads in the same process.
   * - Communication
     - Uses Inter-Process Communication (IPC), which is slower.
     - Communicates through shared memory, which is faster.
   * - Overhead
     - Higher overhead due to resource duplication.
     - Lower overhead since resources are shared.
   * - Isolation
     - Fully isolated from other processes.
     - Not isolated; one thread can affect others in the same process.
   * - Creation Time
     - Slower to create and manage.
     - Faster and more efficient to create.
   * - Context Switching
     - More expensive due to isolated memory.
     - Cheaper since threads share the same address space.


.. admonition:: Explanation
   :class: attention

    * Context switching is a process where the CPU switches from one thread or process to another.
    * This involves saving the state of the current thread or process and loading the state of the next one.
    * Context switching is more efficient for threads than processes because threads share the same memory space, allowing for faster access to shared data and resources.
    * Context switching allows OS to have more threads than CPU cores, enabling better resource utilization.


Parallelism in HPC works at four different levels, each covered in turn below:

1. ``Vector Parallelism`` — within a single core.
2. ``Multi-core Parallelism`` — across the cores of one node.
3. ``Distributed Parallelism`` — across many nodes.
4. ``GPU Parallelism`` — across the thousands of threads of a GPU.

These levels combine rather than compete: a large HPC application typically uses several of them at once.

Vector Parallelism
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vector parallelism is a type of parallel computing where the same operation is applied to multiple data 
points simultaneously. This is often achieved using SIMD (Single Instruction, Multiple Data) instructions.

.. image:: ./figs/simd.png
   :width: 600px
   :align: center
   :alt: SIMD 

SIMD allows a single instruction to operate on multiple data elements at once.

A scalar instruction processes one pair of values per operation. A vector instruction of the same width
processes several pairs at once, so the loop below finishes in a fraction of the iterations:

.. image:: ./figs/vector.png
   :width: 600px
   :align: center
   :alt: A vector unit applying one operation across several array elements at once

This happens inside a single core, and the compiler usually arranges it for you.

Multi-core Parallelism
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Multi-core parallelism involves using multiple cores within a single processor to execute different threads or 
processes concurrently. Each core can handle its own thread, allowing for efficient multitasking.

.. image:: ./figs/multicore.png
   :width: 600px
   :align: center
   :alt: Multi-core Parallelism

Distributed Parallelism
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Distributed parallelism involves spreading tasks across multiple machines or nodes in a cluster. Each node works 
on a portion of the task, and they communicate to share results.

.. image:: ./figs/multinode.png
   :width: 600px
   :align: center
   :alt: Distributed Parallelism

GPU Parallelism
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Graphics Processing Units (GPUs) are designed to handle parallel tasks efficiently. They can execute thousands 
of threads simultaneously, making them ideal for tasks like image processing, machine learning, and 
scientific simulations.

A GPU is built from **Streaming Multiprocessors (SMs)**, each holding many simple cores that run the same
instruction across different data. The diagram below shows the layout of one SM:

.. image:: ./figs/SM.png
   :width: 600px
   :align: center
   :alt: The layout of a GPU streaming multiprocessor

GPU parallelism is covered in detail in Session 5.

Parallelism on Gadi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These levels map onto the resources you ask PBS for:

* **Vector** parallelism needs nothing from PBS — it happens inside each core.
* **Multi-core** parallelism is what ``#PBS -l ncpus=`` buys you, up to 48 on a standard node. A threaded
  program such as the Numba example in this session's exercise spreads across exactly these cores.
* **Distributed** parallelism is what you get by requesting more than 48 cores, which spans nodes. Because
  separate nodes do not share memory, the program must pass messages explicitly — usually with MPI, which
  Session 5 covers.
* **GPU** parallelism requires the ``gpuvolta`` queue and ``#PBS -l ngpus=``.

.. important::

   Requesting cores does not make a program parallel. If the code itself is serial, ``ncpus=48`` leaves 47
   cores idle — and you are still charged for all of them.


.. admonition:: Key Points
   :class: hint

   1. Parallelism is the ability to perform multiple computations simultaneously.
   2. Concurrency and parallelism are not the same: all parallel tasks are concurrent, but not all
      concurrent tasks are parallel.
   3. Threads are lightweight units of execution within a process, while processes are independent programs.
   4. Different levels of parallelism include vector parallelism, multi-core parallelism, distributed parallelism, and GPU parallelism.
   5. The level you use determines what you request from PBS, and requesting cores does not by itself make
      a program parallel.