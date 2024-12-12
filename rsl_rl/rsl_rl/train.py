import yaml
from rsl_rl.runners.on_policy_runner import OnPolicyRunner
from rsl_rl.env.custom_vec_env import CustomVecEnv  # 导入自定义环境
import torch
import os

# 加载配置文件
config_path = os.path.join("..", "config", "dummy_config.yaml")
if not os.path.exists(config_path):
    raise FileNotFoundError(f"Configuration file not found: {config_path}")

with open(config_path, "r") as f:
    train_cfg = yaml.safe_load(f)

# 初始化自定义环境
env = CustomVecEnv(
    num_envs=8,  # 环境数量
    num_obs=4,   # 观测维度
    num_actions=2,  # 动作维度
    max_episode_length=100,  # 最大步长
    device="cuda" if torch.cuda.is_available() else "cpu"
)

# 初始化运行器
runner = OnPolicyRunner(
    env=env,
    train_cfg=train_cfg,
    log_dir="./logs",  # 日志目录
    device="cuda" if torch.cuda.is_available() else "cpu",
)

# 启动训练
runner.learn(num_learning_iterations=train_cfg["runner"]["max_iterations"])
