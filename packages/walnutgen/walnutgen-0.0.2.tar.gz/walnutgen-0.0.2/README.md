# walnutgen

A dead simple, configurable static site generator.


## Documentation

WalnutGen works in a very simple way: you have the `wgconfig.py` at the root of the project, and walnut auto-generates the `wgbuild` directory, which can be served with a HTTP server.

#### Configuration Format

The configuration file exports a variable called `config`, which is a dictionary, which exports the following fields:

- "headers": an array of strings. Defines the headers to be copied at the beginning of the files, in order, relative to the current directory.
- "footers": an array of strings. Defines the footers to be copied at the end of the files, in order, relative to the current directory.
- "files": an array of strings. Defines the files to be used. These are the ones which get the headers and footers, and these get copied inside the build directory. If they're in a subdirectory, the subdirectory gets copied as well.
- "to_copy": an array of strings. This defines the files and directories to be copied as-is in the build directory. Useful for resources which you would need on the website.
- "functions": an array of objects that inherit from `walnutgen.function.Function`

The simplest possible `wgconfig.py` is this:

```python
config = {
    "headers": [
    ],
    "footers": [
    ],
    "files": [
        "index.html",
    ],
    "to_copy": [
    ],
    
    "functions": {
    }
}
```


#### Functions

Functions are used to add logic to the website. For example, you might want to have a list of pages displayed. Instead of manually editing it everywhere, you can use functions.

A function is a class that inherits from `walnutgen.function.Function`. Functions are very simple, they have an `invoke` method which returns a string that gets inserted instead of the function "call" in the file.

Here's an example function:

```python
class MyFunction(Function):
    def invoke(self):
        return "something"
```

This function would replace the call with "something".

To make a function usable from HTML, you need to register it in the configuration file, by constructing it and assigning it to an index in the `config.functions` dictionary. So, if you have this in the config

```python
"functions": {
    [...]
    "my_function": MyFunction(),
    [...]
}
```

then, in an HTML file, this

```
{{ my_function }}
```

will get replaced with the output of `MyFunction.invoke`.

By default, functions return `<!-- FUNCTION NOT IMPLEMENTED -->`.
