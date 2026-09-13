# Aspire-EtherCAT-Lab

> 基于 HPM5E31IPB1 MCU 的 EtherCAT 实验平台硬件设计项目。
>
> Hardware design project for an EtherCAT test platform based on the HPM5E31IPB1 MCU.

<p align="center">
  <img src="https://img.shields.io/badge/MCU-HPM5E31IPB1-0091D5?style=flat-square" alt="MCU">
  <img src="https://img.shields.io/badge/Bus-EtherCAT-16a34a?style=flat-square" alt="EtherCAT">
  <img src="https://img.shields.io/badge/Design-Hardware-0ea5e9?style=flat-square" alt="Hardware design">
  <img src="https://img.shields.io/badge/Status-Design%20Complete-2da44e?style=flat-square" alt="Design complete">
</p>

## 项目简介

本项目包含 HPM5E31IPB1 硬件样板的原理图、BOM、器件数据手册、引脚分配、pinmux 配置和硬件规格文档。

当前硬件交付基线为 2026-09-13 版本：

- 原理图：[`Hardware/Schematic/SCH_HPM5E31IPB1_2026-09-13.pdf`](./Hardware/Schematic/SCH_HPM5E31IPB1_2026-09-13.pdf)
- BOM：[`Hardware/BOM/BOM_HPM5E31IPB1_HPM5E31IPB1_2026-09-13.xlsx`](./Hardware/BOM/BOM_HPM5E31IPB1_HPM5E31IPB1_2026-09-13.xlsx)
- 引脚分配：[`Hardware/Doc/Pin Assignment/HPM5E31IPB1.csv`](./Hardware/Doc/Pin%20Assignment/HPM5E31IPB1.csv)
- Pinmux：[`Hardware/Doc/Pin Assignment/pinmux.c`](./Hardware/Doc/Pin%20Assignment/pinmux.c)

硬件设计资料已经完成并按上述文件冻结。上电、接口、温升、EMC/ESD 等结果需要按照验收标准实际测试后填写，不能仅依据设计文件判定通过。

## 目录结构

| 路径 | 内容 |
| --- | --- |
| [`Hardware/BOM/`](./Hardware/BOM/) | 物料清单及器件采购信息。 |
| [`Hardware/Schematic/`](./Hardware/Schematic/) | 已导出的硬件原理图。 |
| [`Hardware/Doc/Datasheet/`](./Hardware/Doc/Datasheet/) | MCU、电源、CAN、USB 和接口保护器件数据手册。 |
| [`Hardware/Doc/Images/`](./Hardware/Doc/Images/) | PCB 样板正反面及颜色版本图片。 |
| [`Hardware/Doc/Pin Assignment/`](./Hardware/Doc/Pin%20Assignment/) | 引脚分配表、pinmux 源码和引脚分配图。 |
| [`Hardware/Doc/Specs/`](./Hardware/Doc/Specs/) | 硬件设计规格、接口定义、设计约束和验收标准。 |

## 主要硬件资源

依据 `HPM5E31IPB1.csv` 和当前原理图，板卡包含以下主要资源：

- `ESC0`：EtherCAT ESC P0/P1 数据、管理和控制信号。
- `ETH0`：以太网相关复用资源。
- `MCAN0`：CAN 收发器接口及待机控制。
- `UART0`：调试串口 TX/RX。
- `JTAG`：程序下载和硬件调试接口。
- `SPI1`：SPI 扩展总线。
- `PWM0/PWM1`：电机控制 PWM 输出。
- `ADC0`：PF 端口模拟量采样输入。
- `QEI1`：编码器 A/B/Z 输入。
- `USB0`：ID、VBUS 电源控制和过流检测。

## 关键文档

- [硬件设计规格](./Hardware/Doc/Specs/Hardware%20Design%20Specification.md)
- [接口定义要求](./Hardware/Doc/Specs/Interface%20Definition%20Requirements.md)
- [设计约束](./Hardware/Doc/Specs/Constraint%20Design.md)
- [验收测试标准](./Hardware/Doc/Specs/Acceptance%20Test%20Criteria.md)
- [HPM5E31IPB1 引脚分配表](./Hardware/Doc/Pin%20Assignment/HPM5E31IPB1.csv)
- [Pinmux 源码](./Hardware/Doc/Pin%20Assignment/pinmux.c)
- [HPM5E31IPB1 数据手册](./Hardware/Doc/Datasheet/HPM5E31IPB1.pdf)

## Pinmux 使用说明

`pinmux.c` 已按外设模块拆分，每个函数只负责对应 IOC 复用配置：

```c
Usb_Init();
Uart0_Init();
Mcan0_Init();
Jtag_Init();
Esc_P0_Init();
Esc_P1_Init();
Esc_Management_Init();
Qei1_Init();
Spi1_Init();
Pwm_Init();
Adc_Init();
```

`pinmux.c` 不再提供统一的 `init_pins()` 入口。外设时钟、通信参数、PWM 安全状态和 ADC 采样参数由各自驱动配置。

## 建议使用流程

1. 阅读[硬件设计规格](./Hardware/Doc/Specs/Hardware%20Design%20Specification.md)，了解板卡组成和设计边界。
2. 阅读[接口定义要求](./Hardware/Doc/Specs/Interface%20Definition%20Requirements.md)，确认信号和连接器定义。
3. 对照引脚分配表、原理图和数据手册检查引脚及电气连接。
4. 在软件启动阶段按模块调用 `pinmux.c` 中的初始化函数。
5. 按[验收测试标准](./Hardware/Doc/Specs/Acceptance%20Test%20Criteria.md)完成样板上电、接口和安全测试，并记录版本及结果。

## 安全注意事项

- 上电前确认电源极性、接地、连接器方向和板上是否存在异常短路。
- 首次上电从低压、限流条件开始，逐步确认各电源轨和复位时序。
- 上电后不得触碰裸露导体、功率器件和运动机构。
- 连接外部 CAN、EtherCAT、USB 或电机设备前，先确认电平、终端和保护措施。
- PWM 输出、硬件使能和故障关断逻辑验证通过前，不要连接实际负载。

本项目用于实验、学习和原型验证，不能替代量产产品所需的安全、EMC、可靠性和法规认证。

## 文档维护

- 原理图、PCB、BOM、引脚分配、pinmux 和规格文档必须同步更新。
- 器件替代需重新核对封装、引脚、电气参数、热性能和供应状态。
- 发布新硬件版本时，应记录版本号、变更内容、测试结果和遗留问题。
- 未经实测验证的电气参数和功能，不得作为已通过的产品能力对外使用。
