"""A group of functions to help Python 2 act like Python 3"""
import sys


def run_script(path, globals=None, locals=None):
    # In Python 2, we can use execfile(...), but in Python 3 that function
    # doesn't exist, and we instead use exec(open(...)).  Since the latter
    # approach always works, just use that.  Also, make sure to handle global
    # and local namespace, otherwise imports don't seem to work.
    if globals is None:
        globals = sys._getframe(1).f_globals
    if locals is None:
        locals = sys._getframe(1).f_locals
    with open(path, "r") as fh:
        exec(fh.read()+"\n", globals, locals)


def print_stdout(msg):
    """Print to standard output"""
    # In Python 3, the write(...) function returns a value, so store that value
    # in a dummy variable so that it doesn't print.
    dummy = sys.stdout.write(msg + '\n')


def print_stderr(msg):
    """Print to standard error"""
    # In Python 3, the write(...) function returns a value, so store that value
    # in a dummy variable so that it doesn't print.
    dummy = sys.stderr.write(msg + '\n')


def print_msg(msg, output_channel='stdout'):
    """Print a string to standard output or standard error"""
    if output_channel.upper() == 'STDOUT':
        print_stdout(msg)
    elif output_channel.upper() == 'STDERR':
        print_stderr(msg)
    else:
        raise ValueError(
            'Invalid output channel.  Choose from the strings STDOUT, STDERR.')


# If running Python 2, make the range function act like xrange.  That is
# essentially what Python 3 does.
try:
    xrange
    range = xrange

# For Python 3, use the built-in range function, which acts like Python 2's
# xrange.
except NameError:
    range = range

# Use this to check that modules are using the custom range function
'''
def range(*args):
    print('Using custom range function')
    return range(*args)
'''
