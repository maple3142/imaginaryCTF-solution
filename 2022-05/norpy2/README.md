# NorPy Documentation
### Syntax
The syntax of NorPy is very simple. First, comments are any line that starts with a `#`, and are ignored. Second, list the NOR gates being used (one per line) in the following format:
```
input_wirename_1 input_wirename_2 output_wirename
```
NorPy will treat this as one NOR gate, NORing `input_wirename_1` and `input_wirename_2`, and putting the output in `output_wirename`.

Once you've finished listing gates, leave a blank line, followed by a space separated list of inputs that start as True. On the next line, leave a space-separated list of inputs that start as False. See `sample.nor` for a short example of a .nor file, and `sample_no_comments.nor` for the same file with all comments removed.

### Technical Notes
* A wire can take three states: True, False, and None. None is the same as False, except `None NOR None == None`.
    * NOTE: this is different than NorPy 1!
* Every gate output is intialized to None, EVEN if defined in the last two lines of the .nor file.
* All gate inputs not specified as True or False at the end of the .nor file are initialized to None
* All gates are updated at the same time and take one timestep to update, so the order of gates in the .nor file doesn't matter.