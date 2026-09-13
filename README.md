<h1 align="center">Aspire-EtherCAT-Lab</h1>

> 基于 HPM5E31IPB1 MCU 的 EtherCAT 学习板软硬件资料仓库。
>
> Software and hardware resources for an EtherCAT learning board based on the HPM5E31IPB1 MCU.

<p align="center">
  <a href="https://github.com/AspireROS/Aspire-EtherCAT-Lab"><img src="https://img.shields.io/badge/MCU-HPM5E31IPB1-0091D5?style=flat-square" alt="MCU: HPM5E31IPB1"></a>
  <a href="https://www.ethercat.org/"><img src="https://img.shields.io/badge/Bus-EtherCAT-16a34a?style=flat-square" alt="Bus: EtherCAT"></a>
  <a href="https://github.com/AspireROS/Aspire-EtherCAT-Lab/tree/Hardware"><img src="https://img.shields.io/badge/Design-Learning%20Board-0ea5e9?style=flat-square" alt="Design: Learning Board"></a>
  <a href="https://github.com/AspireROS/Aspire-EtherCAT-Lab/tree/Software"><img src="https://img.shields.io/badge/Status-Development-2da44e?style=flat-square" alt="Status: Development"></a>
</p>

## 📖 项目简介

本项目用于维护 Aspire EtherCAT 学习板的硬件设计资料和软件应用示例。硬件和软件分别维护在独立分支中，便于模块化开发、评审和后续合并。

当前分支职责如下：

- `Hardware`：学习板原理图、BOM、器件数据手册、引脚分配、Pinmux 和硬件规格。
- `Software`：基于 HPM SDK 的外设示例和 EtherCAT 相关应用。
- `main`：项目级说明、分支约定和集成信息。

## 📁 目录结构

| 分支/路径 | 内容 |
| --- | --- |
| [`Hardware`](https://github.com/AspireROS/Aspire-EtherCAT-Lab/tree/Hardware) | EtherCAT 学习板硬件设计和验证资料。 |
| [`Software`](https://github.com/AspireROS/Aspire-EtherCAT-Lab/tree/Software) | 软件应用、外设示例和构建工程。 |
| [`Software/App/`](./Software/App/) | GPIO、PWM 等可独立构建和运行的示例工程。 |

`main` 分支不放置具体硬件或软件实现文件。使用对应资料前，请切换到目标分支：

```bash
git switch Hardware   # 查看或开发硬件资料
git switch Software   # 查看或开发软件资料
```

## 💻 软件示例

`Software/App` 当前包含：

- `gpio/gpio_toggle`：GPIO 输出翻转示例。
- `pwmv2/count_matching`：PWM 计数匹配示例。
- `pwmv2/fix_duty_cycle`：固定占空比 PWM 输出示例。
- `pwmv2/hrpwm_calibrate`：高分辨率 PWM 校准示例。
- `pwmv2/phase_shifting`：PWM 相位移示例。
- `pwmv2/pwm_output`：基础 PWM 输出示例。
- `pwmv2/sync_output`：同步 PWM 输出示例。

每个示例目录通常包含 `CMakeLists.txt`、`app.yaml`（如适用）、`src/` 源码以及中英文 README。构建和下载步骤以示例目录说明及所使用的 HPM SDK 版本为准。

## 🔧 硬件资料

硬件设计文件和规格文档位于 `Hardware` 分支，主要包括：

- 原理图、BOM 和制造相关资料。
- HPM5E31IPB1 数据手册及外围器件资料。
- 引脚分配表、Pinmux 配置和接口定义。
- 电源、EtherCAT、CAN、USB、PWM、ADC、编码器等功能说明。
- 设计约束、验收标准和硬件测试记录。

硬件接口、电源限制、引脚复用和验收要求请以 `Hardware` 分支规格文档为准，不要仅依据软件示例推断电气能力。

## 🚀 建议使用流程

1. 根据任务切换 `Hardware` 或 `Software` 分支。
2. 确认 HPM SDK、交叉编译工具链和 EtherCAT 学习板连接正常。
3. 阅读对应目录中的中英文 README，了解硬件连接、编译和下载步骤。
4. 使用示例工程的 `CMakeLists.txt` 构建并下载程序。
5. 进行功能验证时记录硬件版本、SDK、工具链、固件版本和测试结果。

## 🌿 分支开发规范

- 硬件变更提交到 `Hardware` 分支，软件变更提交到 `Software` 分支。
- 新功能先从对应分支创建特性分支，完成验证后再提交合并请求。
- 修改接口、引脚或配置时，必须同步更新相关 README 和规格文档。
- 提交前检查当前分支，避免将硬件资料或软件文件误提交到 `main`。
- 未经实测验证的电气参数、实时性能和 EtherCAT 功能，不得作为已验收能力对外使用。

本项目用于 EtherCAT 学习、实验和原型验证，不能替代量产产品所需的安全、EMC、可靠性和法规认证。

## 📄 许可证

本项目遵循仓库中 [LICENSE](./LICENSE) 文件所声明的许可证。
