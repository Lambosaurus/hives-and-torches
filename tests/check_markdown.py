import re
import os
from sys import call_tracing

LINK_REGEX = re.compile(r'\[(.*?)\]\((.*?)\)')
ANCHOR_REGEX = re.compile(r'\s*\#+\s*(.*)')

# Checks if the markdown URI is valid
# Returns a tuple of (valid, comment)
def check_link(uri, source_path):

    if uri.startswith("https"):
        return True, "http link assumed valid."
    
    # Split out the file and the anchor
    anchor_tokens = uri.count('#')
    if anchor_tokens == 0:
        path, anchor = uri, None
    elif anchor_tokens == 1:
        path, anchor = uri.split('#')
    else:
        return False, "Too many '#' in link."

    if path == "":
        # An unspecified file is the current file
        path = source_path
    else:
        # It must point to a markdown file
        if not path.endswith(".md"):
            return False, "File must end with .md"

        # Otherwise it is relative to the current file
        path = os.path.normpath(os.path.join(os.path.dirname(source_path), path))

        # It must exist
        if not os.path.exists(path):
            return False, "File does not exist"

    # If there is an anchor, it must exist
    if anchor is not None:
        anchor = anchor.replace('-', ' ').lower()
        for candidate in all_anchors(path):
            if anchor == candidate.lower():
                return True, ""
        return False, "Anchor does not exist"

    # Looks fine so far
    return True, "No anchor"

# Iterates over all anchors in a markdown file
def all_anchors(path):
    with open(path, 'r', encoding="utf8") as f:
        for line in f.readlines():
            match = ANCHOR_REGEX.match(line)
            if match:
                yield match.group(1).strip()

# Returns a string of the emoji to use for a test result
def pass_emoji(passed):
    return "✔️  " if passed else "❌ "

# Checks the contents of a markdown file for links
def check_links(path):
    print("Scanning '{}':".format(path))
    errors = 0
    line_number = 0
    with open(path, 'r', encoding="utf8") as f:
        for line in f.readlines():
            line_number += 1
            for match in LINK_REGEX.finditer(line):
                name, uri = match.groups()
                valid, comment = check_link(uri, path)
                if not valid:
                    errors += 1
                print("\t[{}] line {: 3}: '{}' => {}. {}".format(pass_emoji(valid), line_number, name, uri, comment))
    print("{} errors in '{}'".format(errors, path))
    return errors

# iterates over all markdown files in a directory
def all_markdown_files(directory):
        for root, dirs, files in os.walk(directory):
            for path in files:
                if path.endswith(".md"):
                    yield os.path.join(root, path)

def run_all_checks():
    return sum(check_links(path) for path in all_markdown_files("."))

if __name__ == "__main__":
    exit(1 if run_all_checks() > 0 else 0)