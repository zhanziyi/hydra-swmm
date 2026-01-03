import datetime
from swmm_api import swmm5_run
from swmm_api import SwmmInput
from swmm_api.input_file import read_inp_file, section_labels as sections
from swmm_api.input_file.sections import TimeseriesFile
from swmm_api.input_file.helpers import InpSection

def update_swmm_time_1(inp_file: str, int_minute_of_times: int) -> None:
    inp = SwmmInput(inp_file)
    datetime_end = datetime.datetime.combine(inp.OPTIONS["START_DATE"], inp.OPTIONS["START_TIME"]) +\
        datetime.timedelta(minutes = int_minute_of_times)
    inp.OPTIONS['END_DATE'] = datetime_end.strftime("%m/%d/%Y")
    inp.OPTIONS['END_TIME'] = datetime_end.strftime("%H:%M")
    inp.write_file(inp_file)

def update_swmm_time_minute_str_1(datetime_star_time: datetime.datetime, int_time_interval: int, int_number_of_times: int) -> str:
    datetime_end = datetime_star_time + datetime.timedelta(minutes = int_time_interval * int_number_of_times)
    return datetime_end.strftime("%m/%d/%Y"), datetime_end.strftime("%H:%M")

def update_end_time_1(str_inp: str, str_end_time: str) -> None:
    inp = SwmmInput(str_inp)
    inp.OPTIONS['END_TIME'] = str_end_time
    inp.write_file(str_inp)

def update_end_date_1(str_inp: str, str_end_date: str) -> None:
    inp = SwmmInput(str_inp)
    inp.OPTIONS['END_DATE'] = str_end_date
    inp.write_file(str_inp)

def run_swmm_1(str_inp: str, swmm_work_root: str) -> None:
    swmm5_run(str_inp, working_dir=swmm_work_root)

def update_swmm_time_minute_str_1(datetime_star_time: datetime.datetime, int_time_interval: int, int_number_of_times: int) -> str:
    datetime_end = datetime_star_time + datetime.timedelta(minutes = int_time_interval * int_number_of_times)
    return datetime_end.strftime("%m/%d/%Y"), datetime_end.strftime("%H:%M")

def updata_rain_file_1(str_rain_file_name: str, star_time: str, time_interval: int, rain_list: list[float]) -> None:
    rain_number = len(rain_list)
    str_data = ""
    for number_of_times in range(rain_number):
        now_date, now_time = update_swmm_time_minute_str_1(star_time, time_interval, number_of_times)
        str_data = str_data + now_date + "\t" + now_time + "\t" + str(rain_list[number_of_times]) + "\n"
    with open(str_rain_file_name, "w") as f:
        f.write(str_data)

def updata_rain_file_2(inp_file: str ,str_rain_file_name: str, int_minute_of_times: int, rain_list: list[float]) -> None:
    rain_number = len(rain_list)
    str_data = ""
    inp = SwmmInput(inp_file)
    star_time = datetime.datetime.combine(inp.OPTIONS["START_DATE"], inp.OPTIONS["START_TIME"])
    for number_of_times in range(rain_number):
        now_date, now_time = update_swmm_time_minute_str_1(star_time, 1, number_of_times)
        str_data += f"{now_date}\t{now_time}\t{rain_list[number_of_times]}\n"
    with open(str_rain_file_name, "w") as f:
        f.write(str_data)

def create_swmm_time_series_file_1(swmm_root: str, str_initial: str, list_dir_node: list[dict]) -> None:
    for node in list_dir_node:
        file_name = swmm_root + "/" +"inflow_" + node["P"] + ".dat"
        f = open(file_name, "w")
        f.write(str_initial)
        f.close()

def add_time_series_file_1(str_inp: str, list_dir_node: list[dict], list_other_series: list[list[str] ]= [[]]) -> None:
    inp = read_inp_file(str_inp)
    inp[sections.TIMESERIES] = InpSection(TimeseriesFile)
    if list_other_series != [[]]:
        for other_series in list_other_series:
            inp[sections.TIMESERIES].add_obj(\
                TimeseriesFile(name=other_series[0], kind='FILE', filename=other_series[1]))
    for node in list_dir_node:
        series_name = "inflow_" + node["P"]
        file_name = "inflow_" + node["P"] + ".dat"
        inp[sections.TIMESERIES].add_obj(\
            TimeseriesFile(name=series_name, kind='FILE', filename=file_name))
    inp.write_file(str_inp)