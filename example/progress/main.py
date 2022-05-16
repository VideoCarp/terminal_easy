from terminal_easy import *
from asyncio import sleep as async_sleep
async def main():
    for _ in range(100):
        update_progress(1)
        await async_sleep(0.01)

progress(
    task=main,
    loadmessage=f'Loading...\n{colours["red"]}{text["bold"]}',
    afterwards=f'{reset}\n{cursor["show"]}'
)
