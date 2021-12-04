import re
import os
import argparse

LINK_REGEX = re.compile(r'\[(.*?)\]\((.*?)\)')
ANCHOR_REGEX = re.compile(r'\s*\#+\s*(.*)')

def parse_ignore_file(path):
    if os.path.exists(path):
        with open(path, 'r', encoding="utf8") as f:
            for line in f.readlines():
                key = line.split("//")[0].strip()
                if key:
                    yield key

IGNORE_URIS = [k for k in parse_ignore_file("tests/uri.ignore")]

TEST_OK = 0
TEST_WARN = 1
TEST_ERROR = 2

TEST_EMOJI = {
    TEST_OK: "✔️ ",
    TEST_WARN: "⚠️ ",
    TEST_ERROR: "❌ "
}

# Checks if the markdown URI is valid
# Returns a tuple of (valid, comment)
def check_link(uri, source_path):

    if uri in IGNORE_URIS:
        return TEST_WARN, "URI in ignore list."

    if uri.startswith("https"):
        return TEST_OK, "Web url assumed valid."
    
    # Split out the file and the anchor
    anchor_tokens = uri.count('#')
    if anchor_tokens == 0:
        path, anchor = uri, None
    elif anchor_tokens == 1:
        path, anchor = uri.split('#')
    else:
        return TEST_ERROR, "Too many '#' in uri."

    if path == "":
        # An unspecified file is the current file
        path = source_path
    else:
        # It must point to a markdown file
        if not path.endswith(".md"):
            return TEST_ERROR, "File must end with .md"

        # Otherwise it is relative to the current file
        path = os.path.normpath(os.path.join(os.path.dirname(source_path), path))

        # It must exist
        if not os.path.exists(path):
            return TEST_ERROR, "File does not exist."

    # If there is an anchor, it must exist
    if anchor is not None:

        if anchor.lower() != anchor:
            return TEST_ERROR, "Anchor must be lowercase."

        anchor = anchor.replace('-', ' ')
        for candidate in all_anchors(path):
            if anchor == candidate.lower():
                return TEST_OK, ""
        return TEST_ERROR, "Anchor does not exist."

    # Looks fine so far
    return TEST_OK, "No anchor."

# Iterates over all anchors in a markdown file
def all_anchors(path):
    with open(path, 'r', encoding="utf8") as f:
        for line in f.readlines():
            match = ANCHOR_REGEX.match(line)
            if match:
                yield match.group(1).strip()

# Checks the contents of a markdown file for links
def check_links(path, verbosity = TEST_OK):
    print("Scanning '{}':".format(path))
    errors = 0
    line_number = 0
    with open(path, 'r', encoding="utf8") as f:
        for line in f.readlines():
            line_number += 1
            for match in LINK_REGEX.finditer(line):
                name, uri = match.groups()
                code, comment = check_link(uri, path)
                if code == TEST_ERROR:
                    errors += 1
                line_ref = "{}:{}".format(path, line_number)
                if code >= verbosity:
                    print("\t[{}] {} '{}' => {}. {}".format(TEST_EMOJI[code], line_ref, name, uri, comment))
    print("{} errors in '{}'".format(errors, path))
    return errors

# iterates over all markdown files in a directory
def all_markdown_files(directory):
    for root, dirs, files in os.walk(directory):
        for path in files:
            if path.endswith(".md"):
                yield os.path.join(root, path)

# Runs the checker on all markdown files in a directory
# Return True if passing
def run_all_checks(verbosity):
    checked = 0
    passed = 0
    for path in all_markdown_files("."):
        if check_links(path, verbosity) == 0:
            passed += 1
        checked += 1
    print("{} files checked, {} passing.".format(checked, passed))
    return checked == passed

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="Level of errors to display. (0: All, 1: Warn, 2: Errors)", type=int, default=TEST_OK)
    args = parser.parse_args()
    exit(0 if run_all_checks(**vars(args)) else 1)