"""Replace one @icon(...) block inside a pack module. Usage: import and call."""
import re, sys


def patch(module_path, name, new_source):
    src = open(module_path).read()
    pat = re.compile(r'@icon\("%s"\)\ndef \w+\(\):\n(?:.*?\n)*?(?=\n\n@icon|\Z)' % re.escape(name))
    if not pat.search(src):
        raise SystemExit(f"icon {name} not found in {module_path}")
    open(module_path, "w").write(pat.sub(new_source.rstrip() + "\n", src, count=1))
