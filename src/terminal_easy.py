from asyncio import run as async_run
from subprocess import run
from sys import platform, stdout
from dicts import *
import private

async_function = None

reset = '\033[0m'
def clear(system: bool=False) -> None | Exception:
    '''Clears the terminal.
    `system: bool` whether or not to clear the terminal using shell commands `cls` or `clear`.
    Returns `None` if clearing has been successful. Otherwise, an exception is returned.
    '''
    if system:
        if platform != 'win32':
            try: 
                run(['clear'])
            except Exception as e:
                return e
            return
        else:
            run(['cls'])
            return
    print(cursor['clear'], end='')


replacer = '\u001b[1000D'

def write(text: str):
    '''`print`s a string without a newline. Behaviour more predictable than `stdout.write`'''
    print(text, end='')

def emptyln(line: str='\n'):
    '''Empties the current line, given its contents.
    For example,
    ```py
    from time import sleep
    msg = 'This should get deleted in one second.'
    print(msg) # This should get deleted in one second.
    sleep(1) # String should show for another second.
    emptyln(msg) # The string has been deleted. No output.
    ```
    '''
    line_len = len(line)
    write('\b' * line_len)


def update_progress(by: int=1):
    '''Use this to update progress, when working with `progress`.
    For example,
    ```py
    async def main():
    for _ in range(100):
        update_progress()
        await async_sleep(0.01)
    ```
    The `by` parameter can be read as 'by how much is this progressing?'
    '''
    private.progress += by
    msg = f'{private.progress}{private.suffix}'
    write(msg)
    emptyln(msg)
    stdout.flush()


def progress(task: async_function, loadmessage: str='Loading...\n', suffix: str='%', afterwards: str='\n'):
    '''Use this to create a progress tracker for your users.
    `task: async_function`: what function does the task you want to track the progression of,
    and what function updates the progress?
    `loadmessage: str`: what should be displayed before your progression is tracked?
    `suffix: str`: what should be displayed after the progression number? For example, if given '%', you'll see *x*%.
    `afterwards: str`: what should be shown after the progression has been shown?

    Please note that only `task` is a required argument. The default values are:
    ```
    loadmessage='Loading..\\n'
    suffix='%'
    afterwards='\\n'
    ```
    '''
    private.progress = 0
    private.suffix = suffix
    print(loadmessage, end='')
    write(cursor['hide'])
    async_run(task())
    write(afterwards)
