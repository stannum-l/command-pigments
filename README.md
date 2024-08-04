# Command Pygments

This provides a different lexer and parser for command like code blocks in Pygments for mkdocs use.

## Installation

```console
pip install -U .
```

## Usage

~~~console
  ``` cmd
     az command --paramter1 value1 \
        --parameter2 value2 \
        -h "Test"
  ``` 
~~~

## Testing

A sample is contained in `/test/docs/index.md`. You can run this by running `make` and within the Docker container, run `mkdocs serve -a 0.0.0.0:8000`. You can view the mkdocs page using:

```
http://127.0.0.1:8010
```