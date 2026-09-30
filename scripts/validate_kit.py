"""Check this kit's controlled frontmatter, resources and optional integrity manifest."""
import hashlib
import json
from pathlib import Path
import re
import sys
import tomllib
from validate_memory import validate

KIT=Path(__file__).resolve().parents[1]

def validate_kit(root=KIT):
    errors=[]
    counts={}
    for group,expected in [('skills',17),('specialist-library',13)]:
        paths=sorted((root/group).glob('*/SKILL.md'))
        counts[group]=len(paths)
        if len(paths)!=expected: errors.append(f'{group}: expected {expected}, found {len(paths)}')
        for p in paths:
            text=p.read_text(encoding='utf-8')
            match=re.match(r'\A---\nname: ([a-z0-9-]+)\ndescription: ("[^\n]+")\n---\n\n(.+)\Z',text,re.S)
            if not match:
                errors.append(f'{p.relative_to(root)}: invalid controlled frontmatter');continue
            name,description,body=match.groups()
            try:
                desc=json.loads(description)
                if not isinstance(desc,str) or not desc or len(desc)>1024: raise ValueError()
            except ValueError: errors.append(f'{name}: invalid description')
            if name!=p.parent.name or len(name)>64: errors.append(f'{name}: name/folder mismatch')
            if '[TODO:' in text or not body.strip(): errors.append(f'{name}: unfinished scaffold')
    for p in root.rglob('*.json'):
        try: json.loads(p.read_text(encoding='utf-8'))
        except (ValueError,OSError) as exc: errors.append(f'{p.relative_to(root)}: {exc}')
    for p in root.rglob('*.toml'):
        try: tomllib.loads(p.read_text(encoding='utf-8'))
        except (ValueError,OSError) as exc: errors.append(f'{p.relative_to(root)}: {exc}')
    for p in (root/'memory/examples').glob('*.json'):
        try:
            record=json.loads(p.read_text(encoding='utf-8'))
            for err in validate(record): errors.append(f'{p.name}: {err}')
        except (ValueError,OSError):
            pass  # Already reported by the JSON syntax pass above.
    manifest=root/'kit-manifest.json'
    if manifest.exists():
        for relative,digest in json.loads(manifest.read_text(encoding='utf-8'))['files'].items():
            target=(root/relative).resolve()
            if not target.is_relative_to(root.resolve()) or not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest()!=digest:
                errors.append(f'Missing/changed delivered file: {relative}')
    return errors,counts

if __name__=='__main__':
    failures,counts=validate_kit()
    print(json.dumps({'counts':counts,'errors':failures,'note':'Structure/integrity only; no AI behavior or installed-client compatibility claim.'},indent=2))
    raise SystemExit(1 if failures else 0)
