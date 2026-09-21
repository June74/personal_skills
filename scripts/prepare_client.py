"""Preview/project-scope copy of selected kit files. No installs or overwrites."""
import argparse
import hashlib
import json
from pathlib import Path
import stat
import sys

KIT = Path(__file__).resolve().parents[1]

def checked_target(root, relative):
    target = root / relative
    if not target.resolve().is_relative_to(root):
        raise ValueError(f'Target escapes project: {relative}')
    cursor = target
    while cursor != root:
        if cursor.exists() or cursor.is_symlink():
            info = cursor.lstat()
            if cursor.is_symlink() or getattr(info, 'st_file_attributes', 0) & getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 1024):
                raise ValueError(f'Refusing linked/reparse target: {cursor}')
        cursor = cursor.parent
    return target

def make_plan(project, client, specialists=(), allow_duplicates=False):
    project = Path(project).expanduser().resolve(strict=True)
    if not project.is_dir() or project.is_relative_to(KIT):
        raise ValueError('Choose an existing project directory outside the kit.')
    skills = sorted(p for p in (KIT/'skills').iterdir() if p.is_dir())
    for name in sorted(set(specialists)):
        if not name or any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789-' for c in name):
            raise ValueError('Invalid specialist name')
        source = KIT/'specialist-library'/name
        if not (source/'SKILL.md').is_file():
            raise ValueError(f'Unknown specialist: {name}')
        skills.append(source)
    target_root = '.claude/skills' if client == 'claude' else '.agents/skills'
    peer_root = '.agents/skills' if client == 'claude' else '.claude/skills'
    duplicates = [p.name for p in skills if (project/peer_root/p.name/'SKILL.md').exists()]
    if duplicates and not allow_duplicates:
        raise ValueError('Potential duplicate discovery across .agents/.claude: '+', '.join(duplicates)+'. Read setup/CLIENTS.md before using --allow-duplicate-discovery.')
    content = {'AGENTS.md':(KIT/'rules/core.md').read_bytes()}
    if client == 'claude':
        content['CLAUDE.md'] = (KIT/'adapters/claude/CLAUDE.md').read_bytes()
    for skill in skills:
        for source in sorted(skill.rglob('*')):
            if source.is_symlink():
                raise ValueError(f'Refusing linked source: {source}')
            if source.is_file():
                rel = f'{target_root}/{skill.name}/{source.relative_to(skill).as_posix()}'
                content[rel] = source.read_bytes()
    receipt = {'kit_version':(KIT/'VERSION').read_text().strip(),'client':client,'kind':'project snapshot; refresh manually with reviewed diffs','files':{k:hashlib.sha256(v).hexdigest() for k,v in content.items()}}
    content[f'.ai-dev-system/{client}.json'] = (json.dumps(receipt,indent=2)+'\n').encode()
    plan = []
    for relative, payload in content.items():
        target = checked_target(project, relative)
        if target.exists():
            if not target.is_file() or target.read_bytes() != payload:
                raise ValueError(f'Existing content differs; no files written. Review/merge manually: {target}')
            action = 'unchanged'
        else:
            action = 'create'
        plan.append((target,payload,action))
    return project, plan

def apply_plan(project, plan):
    for target,payload,action in plan:
        checked_target(project,target.relative_to(project))
        if action == 'unchanged':
            if not target.is_file() or target.read_bytes() != payload:
                raise ValueError(f'Project changed since preview: {target}')
            continue
        target.parent.mkdir(parents=True,exist_ok=True)
        checked_target(project,target.relative_to(project))
        # Exclusive creation also refuses a file appearing after preflight.
        with target.open('xb') as stream:
            stream.write(payload)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--client',choices=['codex','cursor','claude'],required=True)
    parser.add_argument('--project',required=True)
    parser.add_argument('--specialist',action='append',default=[])
    parser.add_argument('--allow-duplicate-discovery',action='store_true')
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    try:
        root,plan=make_plan(args.project,args.client,args.specialist,args.allow_duplicate_discovery)
        for target,_,action in plan:
            print(f'{action:9} {target.relative_to(root)}')
        if args.apply:
            apply_plan(root,plan)
            print('Project snapshot prepared. Check actual client discovery; no software or service installed.')
        else:
            print('PREVIEW ONLY: no files written. Review, then repeat with --apply if intended.')
        return 0
    except (ValueError,OSError) as exc:
        print(f'STOP: {exc}',file=sys.stderr)
        return 2

if __name__=='__main__':
    raise SystemExit(main())
