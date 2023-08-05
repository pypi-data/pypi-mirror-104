# FinMesh
---
FinMesh is a python-based package that brings together financial data from various sources in one place for ease of use and distribution. The four main sections of FinMesh are (1) the [IEX REST API][1], (2) data from the [US treasury][2], data from the [US Federal Reserve Economic Data][3], and (4) data from the [SECs EDGAR][4] system.

[1]: https://iexcloud.io/docs/api/
[2]: https://www.treasury.gov/resource-center/data-chart-center/digitalstrategy/pages/developer.aspx
[3]: https://fred.stlouisfed.org/
[4]: https://www.sec.gov/edgar/searchedgar/companysearch.html

## Purpose
---
The purpose of this package and its sub-packages is to make accessing API data easier and simpler. With third-party API packages there is always the risk of outages or bugs, so I decided to build my own. In building the original IEX wrapper we sought to build something easy to understand and use, that can be updated quickly and accurately.

With the addition of the US Federal data the opportunity arose to create a package that could deliver all sorts of economic and security data from one place. In doing so we hope to create a low-barrier way for beginners to play with large and very useful data sets.

In the future, this package will be updated with new financial and economic APIs. If you know of a low or no cost API that could be incorporated please raise it as an issue and we will work to have it done ASAP.

## Installation
---
The following dependencies are used in FinMesh:
- OS
- CSV
- JSON
- Requests
- xmltodict
- xml.etree.ElementTree
- webbrowser
- shutil
- BeautifulSoup4
- datetime
- types
- pickle

Most of these are fairly typical and are already included in the Python standard library and they are not all used in all the modules. For those that are not included, they may be installed using pip.

Some APIs require authentication through the use of tokens. These tokens should be set up as environment variables in the bash profile. A great article on how to do this on Mac is available here:

[My Mac OSX Bash Profile](https://natelandau.com/my-mac-osx-bash_profile/)

Click [HERE](https://iexcloud.io/) for your free IEX token.
This token must be stored as IEX_TOKEN in your environment variables.

Click [HERE](https://fred.stlouisfed.org/) for your free FRED token. This token must be stored as FRED_TOKEN in your environment variables.

Finally, once your dependencies and your environment variables are set up, you can install FinMesh.

FinMesh is available as a pip install. Due to the nature of FinMesh as a personal project, version updates can be sporadic meaning months at the same version followed by several version updates within the course of a few weeks. Commit history should be a good indicator of whether there will be version updates, and you can always check your version using pip. The PyPi source is [HERE][8].
[8]: https://pypi.org/project/FinMesh/

## How to Use FinMesh
---
FinMesh has three main modules:
iex -> Access to the IEX Cloud API. This module contains basically all the stock information you could need.
usgov -> Access to the US government's FRED database. From here you can access various economic data as well as an easy-to-use treasury yield function.
edgar -> Essentially experimental at this point. This can be used to download SEC filings and eventually the hope is to be able to parse and format the data for free access.

The iex module contains sub-modules for the various types of data available on IEX Cloud. For the most common endpoints (stock and market data), the iex __init__ file has classes that make gathering, storing, and accessing the data much easier. The IEXStock class can gather any stock information, save and load class states, and output any data to a csv file.

A walk-through of accessing all the modules and using them in your code is in the making.

## Contact
---
If you would like to reach out, feel free to connect with me one of four ways:

1. [On GitHub][5]

2. [On LinkedIn][6]

3. [On Twitter][9]

4. [Via Email][7]

If there are issues, be it major or semantic, please open an issue on GitHub.


[5]: https://github.com/MichaelPHartmann
[6]: https://www.linkedin.com/in/michael-hartmann/
[7]: MichaelPeterHartmann94@gmail.com
[9]: https://twitter.com/m_p_hartmann
