"""
    ____          ____                __               __
   / __ \\ __  __ / __ \\ _____ ____   / /_ ___   _____ / /_
  / /_/ // / / // /_/ // ___// __ \\ / __// _ \\ / ___// __/
 / ____// /_/ // ____// /   / /_/ // /_ /  __// /__ / /_
/_/     \\__, //_/    /_/    \\____/ \\__/ \\___/ \\___/ \\__/
	/____/

Made With ❤️ By Ghoul & Marci
"""

import sys
import hashlib


def getchecksum() -> str:
    """Get's Current File Hash

    Returns:
        str: File Hash
    """
    md5_hash = hashlib.md5()
    with open("".join(sys.argv), "rb") as file:
        md5_hash.update(file.read())
    return md5_hash.hexdigest()
