import argparse

def read_user_cli_args():
    """Handle the CLI argument and options."""
    parser = argparse.ArgumentParser(
        prog='Site Connectivity Checker', description='Check the availability of websites'
    )
    parser.add_argument(
        '-a',
        '--asynchronous',
        action='store_true',
        help='run the connectivity check asynchronously',
    )
    parser.add_argument(
        '-u',
        '--urls',
        metavar='URLs',
        nargs='+',
        type=str,
        default=[],
        help='Enter one or more URLs to check',
    )
    parser.add_argument(
        '-f',
        '--file',
        metavar='FILE',
        type=str,
        default='',
        help='Read URLs from a file',
    )
    return parser.parse_args()

def display_check_result(result, url, error=''):
    """Display the result of the check."""
    print(f'The status of "{url}" is:', end=" ")
    if result:
        print(f'"Online!, time response: {round(result[1], 2)} Seconds." 👍')
    else:
        print(f'"Offline?" ❌ \n  Error: "{error}"')