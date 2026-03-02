# Learning Objectives

After studying this topic, you should be able to:

1.  Explain the purpose and functionality of the `fork()` system call, including its return value semantics.
2.  Differentiate between the various `exec()` functions and choose the appropriate one based on how arguments are provided and whether a PATH search is needed.
3.  Describe the combined `fork()`-`exec()` pattern and explain why it is necessary for executing new programs.
4.  Identify potential race conditions after a `fork()` and explain how `wait()`/`waitpid()` are used to synchronize parent and child processes.
5.  Analyze simple code snippets involving `fork()` and `exec()` and predict their output and behavior.
6.  Explain the problem of zombie processes and how proper use of `wait()` prevents them.
