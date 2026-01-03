import math

def hour_intensity_formula_float_1(float_parameter_a: float, float_parameter_b: float, float_parameter_c: float, \
            float_parameter_n: float, float_year_period_p: float, int_minute_t: int) -> float:
        a = float_parameter_a*0.36*(1+float_parameter_c*math.log(float_year_period_p,10))
        b = float_parameter_b
        c = float_parameter_n
        minute_intensity = a*((1-c)*int_minute_t+b)/math.pow(int_minute_t+b,c+1)
        hour_intensity = minute_intensity 
        return hour_intensity

def chicago_list_1(chicago_parameter_a: float, chicago_parameter_b: float, chicago_parameter_c: float, \
            chicago_parameter_n: float, chicago_year_period_p: float, chicago_peak_r: float, int_minute_duration_t: int) -> list[float]: 
    peak_time = round(int_minute_duration_t * chicago_peak_r)
    rainfall_data = []
    for i in range(peak_time+1):
        rainfall_data.append(hour_intensity_formula_float_1(chicago_parameter_a, chicago_parameter_b, chicago_parameter_c, \
            chicago_parameter_n, chicago_year_period_p, (peak_time-i)/chicago_peak_r))
    for i in range(peak_time+1, int_minute_duration_t+1):
        rainfall_data.append(hour_intensity_formula_float_1(chicago_parameter_a, chicago_parameter_b, chicago_parameter_c, \
            chicago_parameter_n, chicago_year_period_p, (i-peak_time)/chicago_peak_r))
    return [item / 60 for item in rainfall_data]

def chicago_list_2(a: float, b: float, c: float, n: float, \
    chicago_year_period_p: float, chicago_peak_r: float, int_minute_duration_t: int) -> list[float]: 
    peak_time = round(int_minute_duration_t * chicago_peak_r)
    rainfall_data = []
    for i in range(peak_time+1):
        rainfall_data.append(hour_intensity_formula_float_1(a, b, c, \
            n, chicago_year_period_p, (peak_time-i)/chicago_peak_r))
    for i in range(peak_time+1, int_minute_duration_t+1):
        rainfall_data.append(hour_intensity_formula_float_1(a, b, c, \
            n, chicago_year_period_p, (i-peak_time)/chicago_peak_r))
    return [item / 60 for item in rainfall_data]