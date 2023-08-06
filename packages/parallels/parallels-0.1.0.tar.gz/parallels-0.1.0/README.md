# parallels
Parallels is a [literary](https://github.com/agoose77/literary) powered library. 
It provides an async API that mimics concurrent.futures, with support for task-graph executors.

These notebooks can be viewed using [nbviewer](https://nbviewer.jupyter.org/github/agoose77/parallels/tree/main/) until the documentation generator is complete.

## What?
In Python there are several standard APIs for interacting with `executors`. AsyncIO has the `run_in_executor` API, `concurrent.futures` has the `Executor` API, and other
libraries like Dask and Ray have equivalent approaches. `concurrent.futures` is often available within other libraries, but its reduced features-set prevents the underlying
library from implementing useful optimisations like Dask's deferred computation or task graph building.

Parallels implements a standard `Executor` interface which defines a synchronous `submit` method, and an asynchronous `retrieve` method. 
These methods operate upon value-less `asyncio.Future` handles which yield `True` upon task success, and raise an `Exception` otherwise. 
The Dask and Ray implementations accept these handles as arguments to future `submit()` calls, which can be used to build task graphs
and avoid copying data to the local machine.
