import torch
from rsl_rl.env.vec_env import VecEnv  # 确保正确导入 VecEnv

class CustomVecEnv(VecEnv):
    def __init__(self, num_envs, num_obs=4, num_actions=2, max_episode_length=100, device="cpu"):
        self.num_envs = num_envs
        self.num_obs = num_obs
        self.num_actions = num_actions
        self.max_episode_length = max_episode_length
        self.device = torch.device(device)

        # 初始化缓冲区
        self.obs_buf = torch.zeros((num_envs, num_obs), device=self.device)
        self.rew_buf = torch.zeros(num_envs, device=self.device)
        self.reset_buf = torch.zeros(num_envs, dtype=torch.bool, device=self.device)
        self.episode_length_buf = torch.zeros(num_envs, dtype=torch.int, device=self.device)

    def get_observations(self):
        return self.obs_buf, {"observations": {"critic": self.obs_buf.clone()}}

    def reset(self):
        self.obs_buf = torch.zeros((self.num_envs, self.num_obs), device=self.device)
        self.episode_length_buf.zero_()
        self.reset_buf.fill_(False)
        return self.obs_buf, {}

    def step(self, actions):
        # 确保动作的形状正确
        assert actions.shape == (self.num_envs, self.num_actions), \
            f"Expected actions shape {(self.num_envs, self.num_actions)}, but got {actions.shape}"

        # 示例逻辑：根据动作更新观测值
        self.obs_buf += torch.randn_like(self.obs_buf)  # 模拟环境变化
        rewards = torch.sum(actions, dim=1)  # 奖励等于动作值的和
        self.episode_length_buf += 1  # 更新步数
        dones = self.episode_length_buf >= self.max_episode_length  # 是否达到最大步长

        # 重置已完成的环境
        self.obs_buf[dones] = 0
        self.episode_length_buf[dones] = 0

        # 返回 `observations` 键
        infos = {
            "observations": {
                "critic": self.obs_buf.clone()  # 假设 critic 的观测与 obs_buf 相同
            }
        }

        return self.obs_buf, rewards, dones, infos
