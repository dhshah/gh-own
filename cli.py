import argparse


def parse_args():
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser(description="Github Codeowners Helper CLI.")

    crud = parser.add_mutually_exclusive_group()

    # Add default file or folder argument
    parser.add_argument("path", help="Path to the file or folder to be processed.")

    # If -v is passed in always show the version and do nothing else
    parser.add_argument(
        "-v",
        "--version",
        help="Show the version and exit.",
        action="version",
        version="%(prog)s 0.1.0",
    )

    crud.add_argument(
        "-g",
        "--get",
        action="store_true",
        help="(Default) Get the owner of the file or folder.",
    )

    force_group = crud.add_argument_group()
    set_remove_group = force_group.add_mutually_exclusive_group()
    set_remove_group.add_argument(
        "-s",
        "--set",
        type=str,
        help="Set the owner of the file or folder.",
    )
    set_remove_group.add_argument(
        "-r",
        "--remove",
        type=str,
        help="Remove the owner of the file or folder.",
    )

    force_group.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Force the owner of the file or folder.",
    )

    args = parser.parse_args()

    if args.force and not (args.set or args.remove):
        parser.error("--force requires --set or --remove.")

    if not args.set and not args.remove:
        args.get = True

    return args
