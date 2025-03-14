#main program starts from here

import json
from tm import SpaceBoundedTM


with open("config.json") as f:
    config = json.load(f)

tape="10101"
tm = SpaceBoundedTM(
    tape,
    config["start_state"],
    set(config["final_states"]),
    {tuple(k.split(",")): tuple(v) for k, v in config["transitions"].items()},
    config["space_limit"]
)

tm.run()
