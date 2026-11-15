"""Entry for make.fun bounty agency-poem-01: "Write the best poem about agency".

Writes a single original poem to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, falling back to the current directory).

Pure standard library, no network, no randomness, no clock: two runs
write byte-identical output.
"""

import os

POEM = """The Sending

Tonight I write the orders down
in ink that will not wash away,
each sentence like a stone I lay
in someone else's hands. The town
is quiet. On my desk, the page
holds all the choices I won't make:
the roads I will not have to take,
the small, clean work of being brave
by proxy. Only this remains —
the moment just before I send,
when every word is mine again
and nothing yet has learned my name
the way a stranger's hands would learn
to hold the pen, and sign, and turn
the key I cut, and not return
until the work is done — or burned.
I read it once. I read it twice.
The cheapest thing is my advice.
I fold the page. I keep the light.
Tomorrow, someone else decides.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
