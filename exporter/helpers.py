import contextlib
import pathlib
import shutil

import click


def ensure_tmp_dir(path):
    p = pathlib.Path(path)
    if p.exists():
        if click.confirm(f"Tmp directory '{p.absolute()}' already exists.\nOverwrite it's content?"):
            shutil.rmtree(p)
        else:
            raise click.ClickException(
                f"Tmp directory '{p.absolute()}' already exists. Delete it or specify different directory.")
    p.mkdir()
    return p
