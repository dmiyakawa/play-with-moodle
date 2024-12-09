#!/usr/bin/env python3

import csv

""""""

import time
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from logging import DEBUG, INFO, Formatter, StreamHandler, getLogger
import platform
import sys
from typing import Tuple


def format_elapsed_time(seconds: float) -> Tuple[int, int, int]:
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return int(hours), int(minutes), int(seconds)


def main():
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("csv")
    parser.add_argument("-d", "--debug", action="store_true", help="Show debug log")
    args = parser.parse_args()

    logger = getLogger(__name__)
    handler = StreamHandler()
    logger.addHandler(handler)
    if args.debug:
        logger.setLevel(DEBUG)
        handler.setLevel(DEBUG)
    else:
        logger.setLevel(INFO)
        handler.setLevel(INFO)
    handler.setFormatter(Formatter("%(asctime)s %(levelname)7s %(message)s"))
    logger.debug("Start Running (Python {})".format(platform.python_version()))
    start_time = time.time()
    with open(args.csv) as f:
        csv_reader = csv.DictReader(f)
        for d in csv_reader:
            
            title = d["問題番号"]
            description = d["問題内容"]
            answer_1 = d["選択肢ア"]
            answer_2 = d["選択肢イ"]
            answer_3 = d["選択肢ウ"]
            answer_4 = d["選択肢エ"]
            is_correct_1 = "=" if d["正解"] == "ア" else "~"
            is_correct_2 = "=" if d["正解"] == "イ" else "~"
            is_correct_3 = "=" if d["正解"] == "ウ" else "~"
            is_correct_4 = "=" if d["正解"] == "エ" else "~"
        
            print("""\
::{title}::[html]<p>{description}</p>{{
	{is_correct_1}<p><span data-sheets-root\\="1">{answer_1}</span></p>
	{is_correct_2}<p><span data-sheets-root\\="1">{answer_2}</span></p>
	{is_correct_3}<p><span data-sheets-root\\="1">{answer_3}</span></p>
	{is_correct_4}<p><span data-sheets-root\\="1">{answer_4}</span></p>
}}
""".format(title=title,
           description=description,
           answer_1=answer_1, answer_2=answer_2, answer_3=answer_3, answer_4=answer_4,
           is_correct_1=is_correct_1, is_correct_2=is_correct_2, is_correct_3=is_correct_3, is_correct_4=is_correct_4))


    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time > 60:
        hours, minutes, seconds = format_elapsed_time(elapsed_time)
        logger.info(f"Finished running (elapsed: {hours:02d}:{minutes:02d}:{seconds:02d})")
    else:
        logger.info(f"Finished running (elapsed: {elapsed_time:.3f} sec)")
    return 0


if __name__ == "__main__":
    sys.exit(main())