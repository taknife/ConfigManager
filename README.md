# ConfigManager
工具本地配置文件管理器，本地为yaml配置文件



## 支持环境

*   Windows/Linux/MacOS
*   Python项目



## 部署方式

*   直接下载源码放入自己的项目中



## 使用方法

1.   导入项目源码到自己项目中

     ```python
     import config_manager
     ```

2.   默认配置文件路径`../config/config.yaml`

     ```python
     def __init__(self, config_path: str = "../config/config.yaml"):
         self.config_path = Path(config_path)
         self.config = self._load_config()
     ```

3.   配置默认配置文件结构

     使用键值对方式配置

     ```python
     def _get_default_config(self) -> Dict[str, Any]:
         """获取默认配置"""
         return {
             'config_name': {
                 'value_1': '',
                 'value_2': '',
                 'value_3': ''
             }
         }
     ```

     举例如下：

     ```python
     def _get_default_config(self) -> Dict[str, Any]:
         """获取默认配置"""
         return {
             'app': {
                 'name': 'CommandInjector',
                 'version': '1.0.0'
             },
             'config_file': {
                 'path': '',
                 'statu': False
             },
             'network': {
                 'default_ip': '',
                 'default_port': ''
             },
             'authentication': {
                 'username': '',
                 'password': ''
             }
         }
     ```

     在加载配置文件时，会自动检查配置文件是否存在，如果不存在，自动生成yaml配置文件

     ```yaml
     app:
       name: CommandInjector
       version: 1.0.0
     config_file:
       path: ''
       statu: false
     network:
       default_ip: ''
       default_port: ''
     authentication:
       username: ''
       password: ''
     ```

4.   实例化配置文件对象

     ```python
     config = ConfigManager('../config/config.yaml')
     ```

5.   获取配置

     ```python
     config.get('config_name.value_1')
     ```

6.   设置配置

     ```python
     config.set('config_new_name.value_new_1', 'xxxx')
     ```

     注意：设备不需要`config_new_name`配置依旧可以添加

     ```yaml
     config_new_name:
       value_new_1: 'xxxx'
     ```

7.   保存配置文件

     ```python
     config.save()
     ```

8.   重新加载配置文件

     ```python
     config.reload()
     ```

9.   获取自定义配置

     代码：

     ```python
     def get_custom_config(self) -> Dict[str, Any]:
         return self.get('config_name', {})
     ```

     使用：

     ```python
     config.get_custom_config()
     ```
