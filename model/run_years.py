"""
Sequential multi-year dispatch solver: 2035 → 2045 → 2055
Usage: python run_years.py
"""

import subprocess, sys, time, traceback
import numpy as np
from pathlib import Path

YEARS     = [2035, 2045, 2055]
BASE_YEAR = 2025
SCRIPT = Path(__file__).parent / "prepare_solve_network_YEAR.py"

summary = {}

for year in YEARS:
    print(f"\n{'='*55}")
    print(f"  Solving YEAR = {year}  (base = {BASE_YEAR})")
    print(f"{'='*55}")
    t0 = time.time()
    try:
        subprocess.run(
            [sys.executable, SCRIPT, str(year), str(BASE_YEAR)],
            check=True,          # raises if script exits with non-zero
        )
        elapsed = (time.time() - t0) / 3600
        print(f"\n  ✓ Year {year} completed in {elapsed:.2f} h")
        summary[year] = f"OK  ({elapsed:.2f} h)"
    except subprocess.CalledProcessError as e:
        print(f"\n  ✗ Year {year} FAILED (exit code {e.returncode}), continuing...")
        summary[year] = "FAILED"
    except Exception:
        traceback.print_exc()
        summary[year] = "ERROR"

print(f"\n{'='*55}")
print("  Summary")
print(f"{'='*55}")
for y, status in summary.items():
    mark = "✓" if status.startswith("OK") else "✗"
    print(f"  {mark}  {y}: {status}")