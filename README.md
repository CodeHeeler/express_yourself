# Express Yourself

This package contains a series of regular expressions as well as a test suite for ensuring they cover a wide range of possibilities.

## Requirements

Please install this along with the necessary packages listed in requirements.txt, which includes, among other things, pytest.

## How It Works

Call on the function you'd like to try and pass it some text.
If it's an extractor, it will pull the expected text from your passage.
If it's a validator, it will check the expected pattern against your text.
If it's a separator, it will create a dictionary of the expected pattern.

## Running Tests

As long as you keep the structure intact, from the same location as this README file, you can check the tests for yourself by entering:
```
pytest
```
or, for more verbose output:
```
pytest -v
```
### Author

The extractor, validator, and separator:
Dana Walker

### Acknowledgements

The test suites were provided in our assignment.
