# author: Chuang Wang
# date: 2020-11-19

"""Downloads data from the web to a local filepath as a csv file format.

Usage: src/data_wrangling/down_data.py --url=<url> --out_file_path=<out_file_path>

Options:
--url=<url>              URL from where to download the data (must be in standard csv format)
--out_file=<out_file>    Path (including filename) of where to locally write the file
"""

from docopt import docopt
import urllib.request as urllib

opt = docopt(__doc__)


def main(url, out_file_path):
    try:
        urllib.urlretrieve(url, out_file_path)
    except Exception as req:
        print("The provided url or the designated filepath does not exist!")
        print(req)


if __name__ == "__main__":
    main(opt["--url"], opt["--out_file_path"])

