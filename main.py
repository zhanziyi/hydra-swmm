# zhanziyi
# https://github.com/zhanziyi/hydra-swmm

import os
import hydra
from hydra.core.hydra_config import HydraConfig
from hydra.utils import instantiate
from omegaconf import DictConfig, OmegaConf
import hydra_swmm

@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg: DictConfig):
    print(f"Time: {cfg.time} | Period: {cfg.period} | Peak: {cfg.peak} | Path: {\
        HydraConfig.get()['runtime']['output_dir']}")
    inp_file = hydra_swmm.utils.copy_1(cfg.inp, hydra.utils.get_original_cwd())
    rain_file = hydra_swmm.utils.copy_1(cfg.rainfile, hydra.utils.get_original_cwd())
    hydra_swmm.core.update_swmm_time_1(inp_file, cfg.time)
    hydra_swmm.core.updata_rain_file_2(inp_file, rain_file, cfg.time, instantiate(\
        cfg.rain, chicago_year_period_p = cfg.period, chicago_peak_r = cfg.peak, \
        int_minute_duration_t = cfg.time))
    instantiate(cfg.model, fn_inp=inp_file)
if __name__ == "__main__":
    main()
