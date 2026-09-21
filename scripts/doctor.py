"""Read-only inventory. Does not execute found programs or display secrets."""
import json
from pathlib import Path
import platform
import shutil
import sys

def main():
    tools=['git','rg','uv','node','npm','gitleaks','osv-scanner']
    print(json.dumps({'os':platform.system(),'python_version':platform.python_version(),
        'python_executable':sys.executable,'kit':str(Path(__file__).resolve().parents[1]),
        'program_locations':{t:shutil.which(t) for t in tools},
        'note':'null means not on this process PATH, not proof of absence. No version, network, client or service tests performed.'},indent=2))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
