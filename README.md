This module contains the DOM types for the majority of the web APIs used in a web browser.
These can be used by an IDE to provide type hinting and completion during the development cycle.
The APIs within webtypy are generated from the specifications for CSS, HTML, and JavaScript.


# Generation process

The generator has three main phases:

- ingest
- merge
- stringify

The data-model classes represent a bridge between the webidl files and the final output: their
shape and structure serve to facilitate the ingest phase and the stringify phase.

## Ingest

This phase parses the `.webidl/.idl` files using the [webidl parser]([https://github.com/plinss/widlparser).
The output this phase produces is the instances of the data-model dataclasses; these classes represent webidl entities
and attributes in a more convenient way for further manipulation in the following phases.

## Merge

Webidl can declare entities like 'partial interface', so it is possible to have multiple instances of the data-model related to the same type.
This phase merges multiple instances of the same type into a single instance.

## Stringify

This phase takes data-model instances and turns them into pieces of Python source code strings.
This is the Python code that will be written to the `.pyi` file.
Note that stringify is implemented on the data-model dataclass (through the method `to_python`), which is why the ingest tests also contain the stringify tests.
