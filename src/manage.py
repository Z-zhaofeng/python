#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """运行管理任务."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "无法导入Django,是否确实已安装并在您的PYTHONPATH环境变量上可用？是吗？忘记激活虚拟环境了吗？"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
