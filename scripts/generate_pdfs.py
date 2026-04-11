#!/usr/bin/env python3

import os
import sys
import json
import subprocess

def convert_md_to_pdf(md_file, pdf_file):

    os.makedirs(os.path.dirname(pdf_file), exist_ok=True)

    cmd = [
        'pandoc',
        md_file,
        '-o',
        pdf_file,
        '--from=gfm',
        '--pdf-engine=xelatex',
        '-V', 'geometry:margin=1in',
        '-V', 'fontsize=11pt',
        '--toc',
        '--toc-depth=3'
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(result.stderr)
        return False

    return True


def main():

    files = json.loads(sys.argv[1])
    watermark = sys.argv[2]

    for md_file in files:

        base = os.path.basename(md_file).replace(".md", ".pdf")
        pdf = f"generated-pdfs/{base}"

        if not convert_md_to_pdf(md_file, pdf):
            continue

        subprocess.run([
            sys.executable,
            "scripts/watermark.py",
            pdf,
            pdf,
            watermark
        ])


if __name__ == "__main__":
    main()