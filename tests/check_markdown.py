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


def parse_links_file(path):
    if os.path.exists(path):
        with open(path, 'r', encoding="utf8") as f:
            for line in f.readlines():
                key, uri = line.split("//")[0].strip().split(",")
                if key:
                    yield key, uri


LINK_URIS = { k:v for k,v in parse_links_file("tests/links.txt") }
IGNORE_URIS = [ k for k in parse_ignore_file("tests/uri.ignore") ]
MARKDOWN_FILES = [ ]

TEST_OK = 0
TEST_WARN = 1
TEST_ERROR = 2

TEST_EMOJI = {
    TEST_OK: "✔️ ",
    TEST_WARN: "⚠️ ",
    TEST_ERROR: "❌ "
}


# Splits a uri into the path and anchor
def split_uri(uri):
    if uri.count('#') == 0:
        return uri, None
    else:
        return uri.split('#', 1)

# Rejoins a path and anchor into a uri
def join_uri(path, anchor):
    if anchor is None:
        return path
    else:
        return path + "#" + anchor


# Checks if the markdown URI is valid
# Returns a tuple of (valid, comment)
def check_link(uri, source_path):

    if uri in IGNORE_URIS:
        return TEST_WARN, "URI in ignore list."

    if uri.startswith("https"):
        return TEST_OK, "Web url assumed valid."
    
    path, anchor = split_uri(uri)

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

def relative_path(src_file, path):
    return os.path.relpath(path, os.path.dirname(src_file))

# Returns the relative uri of a path to another path
def relative_uri(src_file, uri):

    # split out the file and the anchor
    path, anchor = split_uri(uri)

    # If the path is the file, then we can just return the anchor
    if path == src_file:
        return join_uri("", anchor)

    # Otherwise we need to return the relative path
    return join_uri(relative_path(src_file, path) , anchor)

# Check if this uri is just incorrectly rooted
def try_relative_link(src_path, uri):
    path, anchor = split_uri(uri)
    for file in MARKDOWN_FILES:
        if file.endswith(path):
            return join_uri(relative_path(src_path, file), anchor)
    return None

# Returns the appropriate link if it exists
def find_link(src_path, name, uri):
    if name in LINK_URIS:
        candidate = relative_uri(src_path, LINK_URIS[name])
    else:
        candidate = try_relative_link(src_path, uri)
    if candidate is not None:
        code, comment = check_link(candidate, src_path)
        if code == TEST_OK:
            return candidate
    return None

# Iterates over all anchors in a markdown file
def all_anchors(path):
    with open(path, 'r', encoding="utf8") as f:
        for line in f.readlines():
            match = ANCHOR_REGEX.match(line)
            if match:
                yield match.group(1).strip()

# Checks the contents of a markdown file for links
def check_links(path, verbosity = TEST_OK, fix_links = False):
    print("Scanning '{}':".format(path))
    errors = 0
    line_number = 0

    if fix_links:
        lines = []

    with open(path, 'r', encoding="utf8") as f:
        for line in f.readlines():
            line_number += 1
            for match in LINK_REGEX.finditer(line):
                name, uri = match.groups()
                code, comment = check_link(uri, path)

                if code == TEST_ERROR:
                    new_uri = find_link(path, name, uri)

                    if new_uri is not None:

                        if fix_links:
                            line = line.replace(uri, new_uri, 1)
                            code = TEST_WARN
                            uri = new_uri
                            comment = "Substituted link."
                        else:
                            comment = "Substitution available: \"{}\"".format(new_uri)

                if code == TEST_ERROR:
                    errors += 1

                line_ref = "{}:{}".format(path, line_number)
                if code >= verbosity:
                    print("\t[{}] {} '{}' => {}. {}".format(TEST_EMOJI[code], line_ref, name, uri, comment))

            if fix_links:
                lines.append(line)

    if fix_links:
        with open(path, 'w', encoding="utf8", newline="\n") as f:
            f.writelines(lines)

    print("{} errors in '{}'".format(errors, path))
    return errors

# Rewrites the links in a markdown file with the appropriate links
def fix_links(path, verbosity = TEST_OK):
    print("Fixing '{}':".format(path))
    with open(path, 'r', encoding="utf8") as f:
        lines = f.readlines()
    errors = 0
    line_number = 0
    with open(path, 'w', encoding="utf8") as f:
        for line in lines:
            line_number += 1
            for match in LINK_REGEX.finditer(line):
                name, uri = match.groups()
                new_uri = find_link(path, name, uri)
                if new_uri is not None:
                    line = line.replace(uri, new_uri)
                    errors += 1
            f.write(line)
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
def run_all_checks(directory, verbosity, fix):
    checked = 0
    passed = 0
    MARKDOWN_FILES.clear()
    MARKDOWN_FILES.extend(all_markdown_files(directory))
    for path in MARKDOWN_FILES:
        if check_links(path, verbosity, fix) == 0:
            passed += 1
        checked += 1
    print("{} files checked, {} passing.".format(checked, passed))
    return checked == passed

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="Level of errors to display. (0: All, 1: Warn, 2: Errors)", type=int, default=TEST_OK)
    parser.add_argument("--directory", help="Directory to scan for markdown files.", default=".")
    parser.add_argument("--fix", help="Fix links in markdown files.", action="store_true")
    args = parser.parse_args()
    exit(0 if run_all_checks(**vars(args)) else 1)