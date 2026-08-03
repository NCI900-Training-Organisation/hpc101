Exercise 1
-----------------

.. admonition:: Exercise
   :class: todo

   **Time: 20 min**

    Write a shell script called ``myscript.sh`` that automates the following tasks:

    1. Create a directory named ``mydir`` inside your scratch directory, ``/scratch/$PROJECT/$USER``.

    2. Change into ``mydir``.

    3. Write the message "Hello, World!" into a file named ``myfile.txt`` using
       ``echo "your text" > myfile.txt``.

    4. List the contents of ``mydir`` to verify that ``myfile.txt`` was created successfully, and
       print the contents of the file.

    Then give the script execute permission with ``chmod +x myscript.sh`` and run it with
    ``./myscript.sh``.

.. admonition:: Hints
   :class: hint

   * ``mkdir -p`` will not complain if the directory already exists, so the script can be run twice.
   * Step 3 writes to a relative path, so it only lands in the right place if step 2 succeeded — this
     is why the ``cd`` comes first.
   * You do not need ``touch``: the ``>`` redirection creates the file if it does not exist.
   * Remember the shebang, ``#!/bin/bash``, on the first line — you are running the script directly.

   Expected output::

       myfile.txt
       Hello, World!
