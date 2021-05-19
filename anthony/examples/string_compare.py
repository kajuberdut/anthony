from time import perf_counter_ns

from anthony.utility.distance import compare, compare_info
from icecream import ic

start = perf_counter_ns()
ic(compare("tranpsosed", "transposed"))
print(f"Example Time: {(perf_counter_ns() - start)/1e+9}  Seconds")

ic(compare_info("momther", "mother"))
