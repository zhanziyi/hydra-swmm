import os
import shutil

def copy_inp_1(source_inp: str, original_cwd: str) -> str:
    if not os.path.isabs(source_inp):
        source_inp = os.path.join(original_cwd, source_inp)
    destination = os.path.basename(source_inp)
    print(source_inp, destination)
    shutil.copy2(source_inp, destination)
    return os.path.basename(destination)

def copy_1(source_inp: str, original_cwd: str) -> str:
    if not os.path.isabs(source_inp):
        source_inp = os.path.join(original_cwd, source_inp)
    destination = os.path.basename(source_inp)
    shutil.copy2(source_inp, destination)
    return os.path.basename(destination)

