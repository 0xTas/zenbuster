# About

*ZenBuster is a multi-threaded, multi-platform URL enumeration tool written in Python by me, Zach Griffin* ([@0xTas](https://twitter.com/0xTas)).

I wrote this tool as a way to deepen my familiarity with Python, and to help increase my understanding of Cybersecurity tooling in general.
ZenBuster may not be the fastest or most comprehensive tool of its kind. It is however, simple to use, decently flexible, and in practice only marginally slower than other "tried-and-true" tools like Gobuster.
Personally, I have been using it to help me solve CTF challenges on platforms like TryHackMe, and have found my implementation to be satisfactorily reliable.

**This software is intended for use in CTF challenges, or by security professionals to gather information on their targets:**

- *It is capable of brute-force enumerating subdomains and also URI resources (directories/files).*
- *Both methods of enumeration require use of an appropriate wordlist or dictionary file.*
- **Features Include:**
    1. Hostname format supports standard, IPv4, and IPv6.
    2. Support for logging results to a file with *-O [filename]*.
    3. Specifying custom ports for nonstandard webservers with *-p <port>*.
    4. Optional file extensions in directory mode with *-x <extensions>*.
    5. Quiet mode for less distracting output with *-Q*.
    6. Color can be disabled for less distracting output with *-nc*/*-nl*.
    7. **Tested on Python versions 3.9 and 3.10, with theoretical support for versions >= 3.6**


## CAUTION/DISCLAIMER

*ZenBuster is capable of producing a potentially unwelcome number of HTTP requests in a short amount of time.*

**The developers and contributors are not liable or responsible for any damage caused by misuse or abuse of this software.**

***Please Enumerate Responsibly!***


## License

ZenBuster is licensed under the GNU GPLv3 License, [**see here**](https://github.com/0xTas/zenbuster/blob/master/LICENSE) for more information.


## Credits

Yin-Yang ASCII art in the banners were created by [Joan G. Stark (*jgs*)](http://www.asciiworld.com/+-joan_stark_jgs-+.html) and [Hayley Jane Wakenshaw (*hjw*)](http://www.asciiworld.com/+-hayley_jane_wakenshaw_hjw-+.html).
Modifications were made by me, when specified with: '*zg*'.

---

# Showcase

![ZenBuster](https://i.imgur.com/tJgNB0S.png "ZenBuster Help Page")

More to come...

---

# Installation

Firstly, ensure that Python version **>=** 3.6 is installed, then clone the repository with:

`git clone https://github.com/0xTas/zenbuster.git`

Next, `cd zenbuster`.

### Dependencies

ZenBuster relies on 3 external libraries to function, and it is recommended to install these with:

`pip install -r requirements.txt`

The modules that will be installed and their purposes are as follows:

1. [Python requests](https://pypi.org/project/requests/) 
    - The backbone of each enumeration request. Without this, the script will not function.

2. [termcolor](https://pypi.org/project/termcolor/) 
    - Enables colored terminal output. Non-critical, the script can still run without color if this is not present.

3. [colorama (Windows only)](https://pypi.org/project/colorama/) 
    - Primes the Windows terminal to accept ANSI color codes (from Termcolor). Non-critical.

These dependencies may be installed manually, with `pip` using requirements.txt, or via interaction with the script upon first run.

---

# Usage

Once dependencies have been installed, you can run the program in the following ways:

### On Linux (+Mac?):

`./zenbuster.py [options]` **or** `python3 zenbuster.py [options]`

### On Windows:

`python zenbuster.py [options]`

### [Options]

Short Flag    |Long Flag    |Purpose
--------------|-------------|-------------
-h            |--help       |Displays the help screen and exits
-d            |--dirs       |Enables Directory Enumeration Mode
-s            |-ssl         |Forces usage of HTTPS in requests
-v            |--verbose    |Prints verbose info to terminal/log
-Q            |--quiet      |Minimal terminal output until final results
-nc           |--no-color   |Disables colored terminal output
-nl           |--no-lolcat  |Disables lolcat-printed banner (Linux only)
-u \<hostname\> |--host "     |Host to target for the scan
-w \<wordlist\> |--wordlist " |Path to wordlist/dictionary file
-x \<exts\>     |--ext "      |Comma-separated list of file extensions (Dirs only)
-p <port#>    |--port "     |Custom port option for nonstandard webservers
-O [filename] |--out-file " |Log results to a file (accepts custom name/path)

### Example Usage

`./zenbuster.py -d -w /usr/share/wordlists/dirb/common.txt -u target.thm -v`

`python3 zenbuster.py -w ../subdomains.txt --host target.thm --ssl -O myResults.log`

`zenbuster -w subdomains.txt -u target.thm --quiet` (With .bashrc alias)

---

# Planned Features/Improvements

- Increased levels of optional verbosity.
- Allow optional throttling of task thread-count.
- Allow users to modify the list of ignored status codes.
- Allow greater user control over various request headers.
- Allow optional ignoring of responses based on content-length.
- Expand subdomain enumeration to include OSINT methods instead of just brute-forcing.
- Explore a more comprehensive and source-readable solution to fancy colored output (possibly using [rich](https://pypi.org/project/rich/)).

---

# Known Issues/Limitations

- Enumerating long endpoints may result in ugly terminal output due to line-wraping on smaller console windows. *Logging to a file is recommended, especially on Windows.*
- If target host is a vHost on a shared webserver, enumeration via IP may not function as expected. *Use domain/hostname instead.*