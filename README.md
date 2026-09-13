<h1 align="center">Aspire-EtherCAT-Lab</h1>

> 基于 HPM5E31IPB1 MCU 的 EtherCAT 学习板软硬件资料仓库。
>
> Software and hardware resources for an EtherCAT learning board based on the HPM5E31IPB1 MCU.

<p align="center">
  <img src="https://img.shields.io/badge/MCU-HPM5E31IPB1-0091D5?style=flat-square" alt="MCU">
  <img src="https://img.shields.io/badge/Bus-EtherCAT-16a34a?style=flat-square" alt="EtherCAT">
  <img src="https://img.shields.io/badge/Software-HPM%20SDK-7c3aed?style=flat-square" alt="Software">
  <img src="https://img.shields.io/badge/Status-Development-2da44e?style=flat-square" alt="Development">
</p>

## 项目简介

本仓库用于维护 Aspire EtherCAT 学习板的硬件设计资料和软件示例。硬件资料位于 `Hardware` 分支，软件应用位于 `Software` 分支；分支内容相互独立，便于分别开发和后续合并。

当前仓库默认分支仅保留项目说明和基础配置。使用具体资料前，请切换到对应分支：

```bash
git switch Hardware   # 硬件设计资料
git switch Software   # 软件应用示例
```

## 分支与目录结构

| 分支/路径 | 内容 |
| --- | --- |
| [`Hardware`](https://github.com/AspireROS/Aspire-EtherCAT-Lab/tree/Hardware) | 原理图、BOM、数据手册、引脚分配、Pinmux 和硬件规格。 |
| [`Software`](https://github.com/AspireROS/Aspire-EtherCAT-Lab/tree/Software) | 基于 HPM SDK 的外设和 EtherCAT 相关应用示例。 |
| [`Software/App/`](./Software/App/) | GPIO、PWM 等可独立构建和运行的示例工程。 |

## 软件示例

当前 `Software/App` 包含以下示例：

- `gpio/gpio_toggle`：GPIO 输出翻转示例。
- `pwmv2/count_matching`：PWM 计数匹配示例。
- `pwmv2/fix_duty_cycle`：固定占空比 PWM 输出示例。
- `pwmv2/hrpwm_calibrate`：高分辨率 PWM 校准示例。
- `pwmv2/phase_shifting`：PWM 相位移示例。
- `pwmv2/pwm_output`：基础 PWM 输出示例。
- `pwmv2/sync_output`：同步 PWM 输出示例。

每个示例目录通常包含 `CMakeLists.txt`、`app.yaml`（如适用）、`src/` 源码和中英文说明文档。请以示例目录中的 README 和目标板 SDK 版本为准进行构建。

## 文档与使用流程

1. 根据任务切换 `Hardware` 或 `Software` 分支。
2. 确认 HPM SDK、交叉编译工具链和目标板连接正常。
3. 阅读对应示例的 `README_zh.md` 或 `README_en.md`，了解硬件连接、编译和下载步骤。
4. 使用示例目录中的 `CMakeLists.txt` 构建工程，并将生成的固件下载到 HPM5E31IPB1 开发板。
5. 进行 EtherCAT、PWM、GPIO 等功能验证时，记录 SDK、工具链、固件和硬件版本。

硬件接口、电源限制、引脚复用和验收要求请参考 `Hardware` 分支中的规格文档，不要仅依据软件示例推断电气能力。

## 版本与贡献

- 修改软件示例时，请同步更新对应的中英文 README 和必要的构建配置。
- 硬件变更应在 `Hardware` 分支记录版本、变更内容和测试结果。
- 提交前检查分支归属，避免将硬件资料或软件示例误提交到其他分支。
- 未经实测验证的电气参数、实时性能和 EtherCAT 功能，不得作为已验收能力对外使用。

本项目用于实验、学习和原型验证，不能替代量产产品所需的安全、EMC、可靠性和法规认证。
