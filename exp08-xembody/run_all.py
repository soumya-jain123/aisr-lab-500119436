"""Run every experiment headless and regenerate everything in results/.

    python run_all.py            # full run (about 10-20 minutes on a laptop)
    python run_all.py --quick    # small numbers, about 3-5 minutes (use this in class)
"""

import argparse
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))


def run(script, *args):
    cmd = [sys.executable, os.path.join(HERE, "experiments", script), *map(str, args)]
    print("\n" + "=" * 78 + f"\n$ python experiments/{script} {' '.join(map(str, args))}\n" + "=" * 78, flush=True)
    t0 = time.time()
    subprocess.run(cmd, check=True)
    print(f"[{script} finished in {time.time() - t0:.0f} s]", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    q = ap.parse_args().quick
    run("00_check_setup.py")
    run("01_explore_embodiments.py", "--samples", 1500 if q else 3000)
    run("02_joint_space_transfer.py", "--episodes", 4 if q else 10)
    run("03_task_space_transfer.py", "--episodes", 8 if q else 20)
    run("04_learn_once_deploy_many.py", "--demos", 40 if q else 60, "--episodes", 8 if q else 20)
    run("05_multi_embodiment.py", "--demos", 40 if q else 60, "--episodes", 8 if q else 20)
    run("06_side_by_side_demo.py", "--gif", "--episodes", 3)
    print("\nAll experiments done. Open the results/ folder.")


if __name__ == "__main__":
    main()
