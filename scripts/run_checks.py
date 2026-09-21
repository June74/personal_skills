"""Preview explicit checks; --run executes reviewed argument lists without a shell."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

def load_checks(config):
    obj=json.loads(Path(config).read_text(encoding='utf-8'))
    if not isinstance(obj,dict) or set(obj)!={'checks'} or not isinstance(obj['checks'],list) or not 1 <= len(obj['checks']) <= 100:
        raise ValueError('Expected an object with 1–100 checks.')
    for item in obj['checks']:
        if not isinstance(item,dict) or set(item)!={'name','argv','timeout_seconds'}:
            raise ValueError('Each check needs name, argv, timeout_seconds.')
        if not isinstance(item['name'],str) or not item['name'].strip():
            raise ValueError('Check name must be nonempty.')
        args=item['argv']
        if not isinstance(args,list) or not args or not all(isinstance(v,str) and v and '\0' not in v for v in args):
            raise ValueError('argv must be a nonempty list of nonempty strings.')
        timeout=item['timeout_seconds']
        if isinstance(timeout,bool) or not isinstance(timeout,int) or not 1<=timeout<=3600:
            raise ValueError('timeout_seconds must be an integer from 1 to 3600.')
    return obj['checks']

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project',required=True)
    parser.add_argument('--config',required=True)
    parser.add_argument('--run',action='store_true')
    args=parser.parse_args()
    try:
        root=Path(args.project).expanduser().resolve(strict=True)
        if not root.is_dir(): raise ValueError('Project must be a directory.')
        checks=load_checks(args.config)
        for check in checks:
            print(f"{check['name']}: {json.dumps(check['argv'])}",flush=True)
        if not args.run:
            print('PREVIEW ONLY: no commands executed. Review config before adding --run.')
            return 0
        for check in checks:
            print(f"RUN {check['name']}",flush=True)
            result=subprocess.run(check['argv'],cwd=root,shell=False,timeout=check['timeout_seconds'],check=False)
            if result.returncode != 0:
                print(f"FAIL {check['name']}: exit {result.returncode}",file=sys.stderr)
                return 1
            print(f"PASS {check['name']}")
        return 0
    except subprocess.TimeoutExpired:
        print('FAIL: check timed out; investigate any child processes.',file=sys.stderr)
        return 1
    except (ValueError,OSError) as exc:
        print(f'STOP: {exc}',file=sys.stderr)
        return 2

if __name__=='__main__':
    raise SystemExit(main())
