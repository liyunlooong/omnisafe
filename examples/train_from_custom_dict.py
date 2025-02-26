# Copyright 2023 OmniSafe Team. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Example of training a policy from custom dict with OmniSafe."""

import omnisafe


if __name__ == '__main__':
    env_id = 'SafetyCarButton1-v0'
    custom_cfgs = {
        'train_cfgs': {
            'total_steps': 2048,
            'vector_env_nums': 1,
            'parallel': 1,
        },
        'algo_cfgs': {
            'steps_per_epoch': 2048,
            'update_iters': 1,
        },
        'logger_cfgs': {
            'use_wandb': False,
        },
    }

    agent = omnisafe.Agent('TRPOPID', env_id, custom_cfgs=custom_cfgs)
    agent.learn()

    agent.plot(smooth=1)
    agent.render(num_episodes=5, render_mode='rgb_array', width=500, height=500)
    agent.evaluate(num_episodes=1)
