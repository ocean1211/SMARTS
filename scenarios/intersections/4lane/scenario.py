import os
from pathlib import Path

from smarts.sstudio.genscenario import gen_scenario
from smarts.sstudio.types import (
    EndlessMission,
    Flow,
    RandomRoute,
    Scenario,
    Traffic,
    TrafficActor,
    Via,
)

ego_missions = [
    EndlessMission(
        begin=("edge-south-SN", 1, 10),
        via=(
            Via("edge-south-SN", lane_offset=30, lane_index=1, required_speed=4,),
            Via("edge-west-EW", lane_offset=10, lane_index=0, required_speed=2,),
            Via("edge-west-EW", lane_offset=20, lane_index=0, required_speed=8,),
            Via("edge-west-EW", lane_offset=50, lane_index=1, required_speed=2,),
            Via("edge-west-EW", lane_offset=55, lane_index=0, required_speed=5,),
            Via("edge-west-EW", lane_offset=60, lane_index=1, required_speed=2,),
            Via("edge-west-EW", lane_offset=65, lane_index=0, required_speed=2,),
            Via("edge-west-EW", lane_offset=70, lane_index=1, required_speed=2,),
        ),
    )
]

gen_scenario(
    scenario=Scenario(
        traffic={
            "basic": Traffic(
                flows=[
                    Flow(
                        route=RandomRoute(),
                        rate=3600,
                        actors={TrafficActor(name="car"): 1.0},
                    )
                ]
            )
        },
        ego_missions=ego_missions,
    ),
    output_dir=Path(__file__).parent,
)
