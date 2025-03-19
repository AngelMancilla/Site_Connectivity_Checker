import pathlib
import sys

from Site_Checker.cli import read_user_cli_args, display_check_result
from Site_Checker.checker import site_is_online

def _get_websites_urls(user_args):
    urls = user_args.urls
    if user_args.file:
        urls += _read_urls_from_file(user_args.file)
    return urls

def _read_urls_from_file(file):
    file_path = pathlib.Path(file)
    if file_path.is_file():
        try:
            with file_path.open() as urls_file:
                urls = [url.strip() for url in urls_file if url.strip()]
                if urls:
                    return urls
                print(f"Error: empty input file, {file}", file=sys.stderr)
        except Exception as e:
            print(f"Error reading file {file}: {e}", file=sys.stderr)
    else:
        print(f"Error: input file not found - {file}", file=sys.stderr)
    return []


def _synchronous_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

def main():
    """Run RP Checker"""
    user_args = read_user_cli_args()
    if not user_args:
        print("Error: Failed to read CLI arguments", file=sys.stderr)
        sys.exit(1)

    urls = _get_websites_urls(user_args)
    if not urls:
        print("Error: No URLs to check", file=sys.stderr)
        sys.exit(1)

    _synchronous_check(urls)



if __name__ == '__main__':
    main()

