Shell Scripting
-----------------


.. admonition:: Overview
   :class: Overview

    * **Time:** 30 min

    #. Learn about shell scripts and how to create them.
    #. Learn the differences between ``source`` and ``sh`` commands.

A shell script is a file containing a series of commands that can be executed in the terminal.
Instead of typing the same commands every time you log in, you can put them in a script and run that.

The script ``env.sh`` in the course repository prints some of the environment variables you met in the
previous section, and sets one of its own.

.. code-block:: bash
   :linenos:

    cd  /scratch/$PROJECT/$USER/hpc101
    ls
    cd session_1
    cat env.sh

You can run the shell script using the following command:

.. code-block:: bash
   :linenos:

   sh env.sh

or

.. code-block:: bash
   :linenos:

   source env.sh

or

.. code-block:: bash
   :linenos:

   . env.sh

.. list-table:: Comparison between ``source`` and ``sh``
   :header-rows: 1
   :widths: 25 37 37

   * - Feature
     - ``source`` (or ``.``)
     - ``sh``
   * - Shell Environment
     - Runs script **in the current shell**
     - Runs script **in a new sub-shell**
   * - Persistence
     - Changes (e.g., variables, ``cd``) **persist**
     - Changes **do not persist** after exit
   * - Typical Use
     - Load config files, environment variables, functions
     - Run standalone shell scripts
   * - Syntax
     - ``source script.sh`` or ``. script.sh``
     - ``sh script.sh``
   * - Shebang Ignored?
     - Yes — runs in the shell you are already in
     - Yes — ``sh`` is named explicitly, so the shebang is just a comment
   * - Performance
     - Slightly faster (no new process)
     - Slower (spawns a new shell process)

Seeing the difference
^^^^^^^^^^^^^^^^^^^^^^

``env.sh`` sets a variable called ``MYSCRATCH``. Run it both ways and check afterwards whether that
variable still exists in your shell:

.. code-block:: bash
   :linenos:

   unset MYSCRATCH
   sh env.sh
   echo "after sh: $MYSCRATCH"

   unset MYSCRATCH
   source env.sh
   echo "after source: $MYSCRATCH"

After ``sh`` the variable is empty — the script ran in a sub-shell that has since exited, taking its
environment with it. After ``source`` the variable is set, because the script ran in your current shell.
This is why module and environment setup scripts must always be **sourced**.

Running a script directly
^^^^^^^^^^^^^^^^^^^^^^^^^^

There is a third way to run a script: execute the file itself. For this the file needs the **execute
permission**, which you grant with ``chmod``:

.. code-block:: bash
   :linenos:

   chmod +x env.sh
   ./env.sh

Run this way, the first line of the file decides which interpreter is used. That line is called the
**shebang**:

.. code-block:: bash

   #!/bin/bash

.. important::

   The shebang only matters when you execute the script directly with ``./env.sh``. If you run
   ``sh env.sh`` you have already named the interpreter yourself, so the shebang is ignored and treated
   as an ordinary comment. This is worth remembering, because ``sh`` is not always ``bash`` — on many
   systems it is a more limited shell, and a script written for ``bash`` can fail under it.


.. admonition:: Key Points
   :class: hint

   * A shell script is a file containing a series of commands that can be executed in the terminal.
   * You can run the shell script using the ``sh``, ``source``, or ``.`` commands, or directly as
     ``./script.sh`` once it has execute permission.
   * ``source`` runs the script in your current shell, so its variables and directory changes persist.
   * ``sh`` runs the script in a sub-shell, so its changes are lost when the script finishes.
   * The shebang line is only honoured when the script is executed directly.
