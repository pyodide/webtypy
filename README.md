# webtypy

Webtypy is a library created with the aim of enhancing the capabilities of your IDE during web development. This module contains the DOM types for a majority of the web APIs commonly used in a web browser, allowing developers to gain insights about the Web API.

With webtypy, developers can receive hints from their IDE about available functions, classes, function parameters, and their associated types. These features are intended to assist in the development process and potentially improve code accuracy.

The APIs within webtypy are generated from the specifications for CSS, HTML, and JavaScript, providing developers with a resource that keeps up with current web standards.

## Installation

To install webtypy, you can use the following command:

`pip install webtypy`


**Remark**: Webtypy is primarily a development-time library. It is designed to assist developers during the development process by providing insights about the Web API. As such, it is not typically required in a production environment or at runtime. Its main function is to enhance the development experience and is not needed once the application is deployed.

## Usage

Webtypy is designed to enhance your IDE's capabilities and streamline your development process. It integrates directly into your development environment and can be utilized in various ways. Here are a couple of examples:

**Code Completion**: One way to leverage webtypy is through code completion. As you type, your IDE can suggest possible completions based on webtypy's API data. This feature can be typically invoked by pressing 'Control+Space'. 

**Hovering Information**: Another example is the detailed information provided when you hover over an element in your code. By placing your mouse pointer over an element, you can view additional details like associated types and the definition of the element.

These are just a couple of examples, and the exact usage might vary based on the IDE you're using. Be sure to check your IDE's documentation for more specific instructions on utilizing features like code completion and hovering information.

## Generation

A few details about the generation process of the .pyi (Python Interface file) can be found [here](GENERATION.md).

## License

webtypy uses the [Mozilla Public License Version
2.0](https://choosealicense.com/licenses/mpl-2.0/).