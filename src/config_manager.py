#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/28 09:43
# @Author  : taknife
# @Project : ConfigManager
# @File    : config_manager.py


import yaml
from pathlib import Path
from typing import Any, Dict


class ConfigManager:
    def __init__(self, config_path: str = "../config/config.yaml"):
        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """加载配置文件，如果不存在则创建默认配置"""
        if not self.config_path.exists():
            # print(f"配置文件不存在，创建默认配置: {self.config_path}")
            default_config = self._get_default_config()
            self._save_config(default_config)
            return default_config

        try:
            with open(self.config_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file) or {}
        except Exception as e:
            print(f"加载配置文件失败: {e}")
            return self._get_default_config()

    @staticmethod
    def _get_default_config() -> Dict[str, Any]:
        """获取默认配置"""
        return {
            'config_name': {
                'value_1': '',
                'value_2': '',
                'value_3': ''
            }
        }

    def _save_config(self, config: Dict[str, Any]) -> None:
        """保存配置到文件"""
        try:
            # 确保目录存在
            self.config_path.parent.mkdir(parents=True, exist_ok=True)

            with open(self.config_path, 'w', encoding='utf-8') as file:
                yaml.dump(
                    config,
                    file,
                    default_flow_style=False,
                    allow_unicode=True,
                    sort_keys=False  # 保持键的顺序
                )
            # print("配置保存成功")
        except Exception as e:
            print(f"保存配置失败: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """获取配置值，支持点符号：config.get('network.default_ip')"""
        try:
            keys = key.split('.')
            value = self.config
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default

    def set(self, key: str, value: Any) -> None:
        """设置配置值，支持点符号：config.set('network.timeout', 60)"""
        keys = key.split('.')
        config = self.config

        # 遍历到最后一个键的前一个
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]

        # 设置最终的值
        config[keys[-1]] = value
        self._save_config(self.config)

    def save(self) -> None:
        """保存当前配置"""
        self._save_config(self.config)

    def reload(self) -> None:
        """重新加载配置文件"""
        self.config = self._load_config()

    # 获取配置文件
    def get_custom_config(self) -> Dict[str, Any]:
        return self.get('config_name', {})
    # def get_modules(self) -> List[str]:
    #     """获取启用的模块列表"""
    #     return self.get('modules.enabled', [])
    #
    #
    # def get_auth_config(self) -> Dict[str, Any]:
    #     """获取认证配置"""
    #     return self.get('authentication', {})
