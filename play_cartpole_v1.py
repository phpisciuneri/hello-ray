import argparse
import gymnasium as gym
import logging
import os
from typing import Optional

from ray.rllib.algorithms.algorithm import Algorithm
from ray.rllib.algorithms.ppo import PPOConfig

logger = logging.getLogger(__name__)

def main(args):

    env_name = "CartPole-v1"
    env = gym.make(env_name)

    if args.checkpoint == None:
        algo = PPOConfig().environment(env_name).build()
    else:
        checkpoint_dir = os.path.normpath(args.checkpoint)
        algo = Algorithm.from_checkpoint(checkpoint_dir)

    average_reward = 0
    for i in range(args.num_episodes):

        episode_reward = 0
        terminated = truncated = False
        obs, info = env.reset()

        while not terminated and not truncated:
            action = algo.compute_single_action(obs)
            obs, reward, terminated, truncated, info = env.step(action)
            episode_reward += reward

        logger.info(f"Episode {i+1} reward: {episode_reward}")
        average_reward += episode_reward

    logger.info(f"Average episode reward: {average_reward / args.num_episodes}")


if __name__ == "__main__":
    logging.basicConfig(
        format="[%(levelname)s] %(filename)s:%(lineno)s:%(funcName)s %(message)s",
    )
    logging.getLogger().setLevel(logging.DEBUG)

    parser = argparse.ArgumentParser(prog="play_cartpole_v1")

    parser.add_argument("--checkpoint", type=str, default=None,
                        help="path to checkpoint to play from")
    parser.add_argument("-n", "--num_episodes", type=int, default=1,
                        help="number of episodes to play")

    args = parser.parse_args()

    main(args)
