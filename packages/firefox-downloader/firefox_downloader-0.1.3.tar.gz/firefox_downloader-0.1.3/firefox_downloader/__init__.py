"""
Script entry point.
"""
import os
import sys
import shutil
import getpass
import argparse
from pathlib import Path
from . import info
from . import config
from .config import get_config as C
from . import remote
from . import current
from . import utils


def cli_options():
    """Set cli options and return user inputs"""
    parser = argparse.ArgumentParser(description=info.DESCRIPTION)
    parser.add_argument('--version', action='version', version=f'%(prog)s {info.VERSION}')
    parser.add_argument('--verbose', help="increase output verbosity",
                        action="store_true", dest="VERBOSE")
    parser.add_argument('--lang', nargs='?', help="language to be installed (default to en_US)",
                        default="en_US", dest="LANG")
    parser.add_argument('--user', nargs='?', help="User under which to install firefox. "
                        "Use root for system wide installation. If not provided, the "
                        "user which is running the programm will be used.",
                        default=getpass.getuser())
    parser.add_argument('--firefoxuser', nargs='?',
                        help='If running as root, specify the user under which to run firefox',
                        dest='FUSER')
    parser.add_argument('--desktop-file', action="store_true", dest="INIDESKTOP",
                        help="Install desktop ini file")
    parser.add_argument('--desktop-profile-file', action="store_true", dest="INIPROFILEDESKTOP",
                        help="Install desktop ini file to run profile selector")
    return parser.parse_args()


def main():
    """Run script"""
    config.Default(**vars(cli_options()))
    version = current.installed_version()
    if not version:
        print("Local binary not found, going to install")
        version = "0.0"
    latest_version = remote.get_latest_version()
    if utils.cast_version(version) >= utils.cast_version(latest_version):
        print("Latest already installed")
        sys.exit(0)
    os.chdir(C().tmp_folder)
    tar_path, hash_ = remote.download_with_hash(latest_version)
    if hash_ != remote.get_hash_control(latest_version):
        raise ValueError("Hash mismatch!")
    shutil.unpack_archive(tar_path)
    Path(tar_path).unlink()
    bk_folder = Path(f"{C().binaries_path}_old")
    install_folder = Path(C().binaries_path)
    if bk_folder.exists():
        bk_folder.unlink()
    if install_folder.exists():
        install_folder.rename(bk_folder)
    Path('./firefox').rename(C().binaries_path)
    utils.write_desktop_file()
    utils.write_profile_desktop_file()


if __name__ == '__main__':
    main()
