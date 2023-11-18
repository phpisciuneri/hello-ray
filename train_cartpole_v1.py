import os
from ray.rllib.algorithms.ppo import PPOConfig
from ray.tune.logger import pretty_print
from ray.rllib.algorithms.algorithm import Algorithm

restore = False

if restore:
    algo = Algorithm.from_checkpoint(
        os.path.join("output", "checkpoint_30"))
else:
    algo = (
        PPOConfig()
        .rollouts(num_rollout_workers=1)
        .resources(num_gpus=0)
        .environment(env="CartPole-v1")
        .build()
    )

for i in range(10):
    result = algo.train()

    iter = result["training_iteration"]
    mean = result["episode_reward_mean"]
    print(iter, mean)
    #print(pretty_print(result))

    if (i + 1) % 5 == 0:
        checkpoint_dir = os.path.join("output", f"checkpoint_{iter}")
        algo.save(checkpoint_dir)
        print(f"Checkpoint saved in directory {checkpoint_dir}")
