# PkgLic

The purpose of this helper app is to make it fast and easy to get an understanding of which open source licenses you are using in your application.

This is done by querying the respective package manager for the meta data rather than what is installed locally, as your build machines may not want/need all the packages installed and you'll also save time by not having to download the bulk of the packages.

The intention is to run it in your build pipeline, and at least you get a list of the components you use (as per your requirements files) and their licenses. With a small bit of trickery you can update some wiki page to keep an up to date list of packages.

The script handles `requirements.txt` (python), `package.json` (javascript), `*.csproj` (C#/nuget) and `packages.config` (C#/nuget).

Basic operation is to invoke the script with some file

    pkglic -f requirements.txt

and get an output with package names and their license. There are some more switches supported.

```
pkglic - (c) Jesper Hogstrom 2021.

usage: pkglic [-h] -f file [file ...] [-o {0,1,2,3}] [-t {py,js,cs,nu}]
              [-u [UNWANTED [UNWANTED ...]]] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -f file [file ...], --files file [file ...]
                        input files to scan.
  -o {0,1,2,3}, --order {0,1,2,3}
                        Which fields to use to sort output; 0 - type, name, 1:
                        license, name, 2: type, license, 3: group by license.
  -t {py,js,cs,nu}, --type {py,js,cs,nu}
                        Assume <type> for all <files> if not guessable.
  -u [UNWANTED [UNWANTED ...]], --unwanted [UNWANTED [UNWANTED ...]]
                        Exit with errorlevel on these license types.
  -v, --verbose         Increase verbosity.
  ```

## Supported formats
### Python
Any file path containing "requirements.txt" will be analyzed as a requirements file as supported by [pip](https://pip.pypa.io/en/stable/cli/pip_install/).

http://pypi.org is used to fetch the meta data.

### Javascript
Any file path containing "package.json" will be analyzed as a package.json file. Only the "dependencies" block will be checked!

https://npmjs.org is used to fetch the meta data.

### Nuget

Any file containing ".csproj" will be analyzed as a C# project and the nuget packages extracted for analysis.

Any file containing "packages.config" will be analyzed as a nuget packages file.


https://nuget.org is used to fetch the meta data.


# Hard check on licenses

Some projects prefer to avoid certain OSS licenses. This was actually the main reason for writing the tool. There are many ways to accomplish such a verification, including using the switch `-u` or `--unwanted` - for instance `-u GPL` or `-unwanted "MIT License"`.

Adding the `-u` switch will first print all packages and their licenses, then print out all packages that match any unwanted license and finally *terminate with an error code, breaking the build*.


# Updating wiki pages

All output is written to `stdout`, so something like
```
pkglic -f requirements.txt | tee /tmp/licenses_in_use
wikiupdater --host wiki.intranet --target-page licenses --upload /tmp/licenses_in_use
```
will do the trick (assuming you have a tool called wikiupdater etc etc).


# License types

The license type will be set to whatever the package specifies. However, in some cases the license cannot be determined. If so, the following applies:

* The meta data could not be downloaded: 404_NOT_FOUND
* The license node not present: NOT_SPECIFIED

