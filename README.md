# Hydra_SWMM

## Overview
This project encapsulates SWMM (Storm Water Management Model) using the Hydra framework, enabling convenient simulation of SWMM models under different **Chicago rainfall patterns**. Leveraging the **Multirun** functionality of the Hydra framework, it supports batch execution of SWMM models across various Chicago rainfall patterns.

## Usage Instructions

### SWMM Configuration
1. Add a time series and bind it to an external file.
2. Modify the rain gauge time series to the time series added above.

### Configuration File Setup
1. Configure `config.yaml` in the `conf` directory
    1. The `inp` parameter specifies the path to the SWMM model `.inp` file.
    2. The `rainfile` parameter specifies the SWMM time series file.
    3. The `time` parameter specifies the SWMM simulation time in **minutes**.
    4. The `period` parameter specifies the return period of the Chicago rainfall pattern in **years**.
    5. The `peak` parameter specifies the peak shape of the Chicago rainfall pattern.
2. Configure `chicago.yaml` in the `rain` subdirectory under `conf`
    1. Rainfall pattern formula: $i=\frac{a(1+c \lg p)}{(t+b)^n}$
    2. Fill in the corresponding fields with parameters `a`, `b`, `c` and `n`.

### Program Execution
1. For a **single run**, simply execute `python main.py`. Results will be saved in the `outputs` directory at the project root.
2. For **batch runs**, refer to the Hydra Multirun parameters. Results will be saved in the `multirun` directory at the project root.
    1. Example: Run simulations with different time settings: `python main.py -m time=10,20,30`
    2. Example: Run simulations with different time and return period settings: `python main.py -m time=10,20,30 period=1,5,10`
    3. Example: Run simulations with different time, return period and peak shape settings: `python main.py -m time=10,20,30 period=1,5,10 peak=0.3,0.5,0.7`



## 简介
本项目使用Hydra框架封装SWMM，可以方便实现不同芝加哥降雨雨型下SWMM模型的模拟，依托Hydra框架的多重运行(Multirun)的功能，能够实现不同芝加哥降雨雨型SWMM模型批量运行。

## 使用方法

### SWMM设置
1. 添加时间序列，并绑定为外置文件
2. 将雨量计时间序列改为上述添加的时间序列

### 配置文件设置
1. 配置conf文件夹下`config.yaml`
    1. `inp`设置SWMM模型.inp文件路径
    2. `rainfile`设置SWMM时间序列文件
    3. `time`设置SWMM模拟时间，单位为分钟
    4. `period`设置芝加哥降雨雨型重现期，单位为年
    5. `peak`设置芝加哥降雨雨型峰形
2. 配置conf子文件夹rain下`chicago.yaml`
    1. 雨型公式$i=\frac{a(1+c \lg p)}{(t+b)^n}$
    2. `a`、`b`、`c`、`n`参数填入对应设置处

### 运行程序
1. 单次运行执行`python main.py`即可，结果保存在程序根目录`outputs`文件夹中
2. 批量运行参考Hydra多重运行(Multirun)参数，结果保存在程序根目录`multirun`文件夹中
    1. 例如，运行不同时间的模拟执行`python main.py -m time=10,20,30`，即可批量运行
    2. 例如，运行不同时间和重现期模拟执行`python main.py -m time=10,20,30 period=1,5,10`
    3. 例如，运行不同时间、重现期和峰形模拟执行`python main.py -m time=10,20,30 period=1,5,10 peak=0.3,0.5,0.7`