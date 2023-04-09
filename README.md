This module contains the DOM types for the majority of the web APIs used in a web browser.
These can be used by an IDE to give type hinting and completion during the development cycle.
The APIs inside `webtypy` are generated from the specifications for CSS, HTML and JavaScript. 



# Generation process

The generator has three main phases:

- ingest
- merge
- stringify

The data-model classes represents a bridge between the `webidl` files and the final output: their 
shape and structure serve to facilitate the ingest phase and the stringify phase. 

## Ingest

This phase parses the`.webidl/.idl` files using [webidl parser]([https://github.com/plinss/widlparser).
The output this phase produces is the instances of the data-model dataclasses; these classes represents webidl entities 
and attributes in a more convenient way for further manipulation in the following phases. 

## Merge

Webidl can declare entities like 'partial interface' so it is possible to have multiple instances of the data-model related to the same type.
This phase merge multiple instances of the same type to a single instance.

## Stringify

It takes data-model instances and turns them in pieces of python source code strings.
This is the python code that will be written to the `.pyi` file.
Notice that the stringify is implemented on the data-model dataclass (through the method `to_python`), this is why the ingest tests contains also the stringify tests.

