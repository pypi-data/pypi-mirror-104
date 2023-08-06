# ActuationDelay

Description

Notes: need to add it before switching control mode!

| `lib_name`       | `class_name`          |
| ---------------- | --------------------- |
| `ActuationDelay` | `gsp::ActuationDelay` |

## Context

| Name    | Optional | Type | Default | Description                                                 |
| ------- | -------- | ---- | ------- | ----------------------------------------------------------- |
| `delay` | No       | int  | -       | The number of physics step all joint references get delayed |

## SDF

```xml
<plugin filename="ActuationDelay" name="gsp::ActuationDelay">
    <!-- Context -->
    <delay>10</delay>
</plugin>
```

## Python

```python
from gazebo_scenario_plugins import plugins
from scenario import gazebo as scenario_gazebo

# [...] Create the simulation and insert the model 'my_model'

# Create the plugin context
actuation_delay = plugins.ActuationDelay(delay=10)

# Insert the plugin to the model
ok = scenario_gazebo.insert_plugin_to_gazebo_entity(
    my_model.to_gazebo(), *actuation_delay.args())
assert ok, "Failed to insert the plugin"
```

