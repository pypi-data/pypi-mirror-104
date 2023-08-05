from contextlib import contextmanager
import sys, os


@contextmanager
def cd(path=None):
    from .config import Config
    path = path or Config.iot49_dir()
    cwd = os.getcwd()
    os.chdir(os.path.expandvars(os.path.expanduser(path)))
    try:
        yield
    finally:
        os.chdir(cwd)


@contextmanager
def redirect_stdout_stderr(out, err):
    # temporarily redirect stdout, stderr
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = out
    sys.stderr = err
    try:
        yield
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
