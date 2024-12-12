# legged_sim
## 1. conda
### 常用命令
1. 激活环境：
```bash
conda activate myenv
```
2. 退出环境：
```bash
conda deactivate
```
3. 查看所有conda环境：
```bash
conda env list
```
4. 创建conda虚拟环境：
```bash
conda create -n isaac_gym_env python=3.10 -y
```
5. 激活虚拟环境：
```bash
conda activate isaac_gym_env
```
6. 删除建立的环境：
```bash
rm -rf isaac_gym_env
```
### 安装 Isaac Sim 包(适用于ubuntu20)

1. Install pytorch 1.10 with cuda-12:
```bash
pip install torch==2.4.0 --index-url https://download.pytorch.org/whl/cu121
```
2. 验证pytorch是否成功
```bash
python -c "import torch; print(torch.cuda.is_available())"
```

3. 然后，安装 Isaac Sim 包(适用于ubuntu20)
先在omniverse中安装Isaac Sim，然后将以下环境变量导出到您的终端
```bash
# Isaac Sim root directory
export ISAACSIM_PATH="${HOME}/.local/share/ov/pkg/isaac-sim-4.2.0"
# Isaac Sim python executable
export ISAACSIM_PYTHON_EXE="${ISAACSIM_PATH}/python.sh"
```
- 检查模拟器是否按预期运行：
```bash
# note: you can pass the argument "--help" to see all arguments possible.
${ISAACSIM_PATH}/isaac-sim.sh
```
- 检查模拟器是否从独立的 Python 脚本运行：
```bash
# checks that python path is set correctly
${ISAACSIM_PYTHON_EXE} -c "print('Isaac Sim configuration is now complete.')"
# checks that Isaac Sim can be launched from python
${ISAACSIM_PYTHON_EXE} ${ISAACSIM_PATH}/standalone_examples/api/omni.isaac.core/add_cubes.py
```
4. 如果您一直在使用以前版本的 Isaac Sim，则需要在安装后首次运行以下命令 以删除所有旧用户数据和缓存变量：
```bash
${ISAACSIM_PATH}/isaac-sim.sh --reset-user
```
5. 将 Isaac Lab 存储库克隆到您的工作区：
```bash
git clone git@github.com:isaac-sim/IsaacLab.git
```
6. 创建 Isaac Sim 符号
```bash
# enter the cloned repository
cd IsaacLab
# create a symbolic link
ln -s /home/cobot-t2-vision/.local/share/ov/pkg/isaac-sim-4.2.0 /home/cobot-t2-vision/IsaacLab/_isaac_sim
# For example: ln -s /home/nvidia/.local/share/ov/pkg/isaac-sim-4.2.0 _isaac_sim
```
7. 进入conda环境
8. 安装依赖项apt
```bash
sudo apt install cmake build-essential
```
9. 运行安装命令
```bash
cd IsaacLab
./isaaclab.sh --install # or "./isaaclab.sh -i"
```
安装所有学习框架

10. 