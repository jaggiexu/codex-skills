#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

ALLOWED_PRIORITIES = {"P0", "P1", "P2", "P3"}
ALLOWED_METHODS = {"EP", "BVA", "ST", "EG"}
ALLOWED_CLASSES = {"核心用例", "衍生用例", "待确认"}
ALLOWED_TAGS = {"APP", "Android", "iOS"}


def validate(cases):
    errors, warnings = [], []
    if not isinstance(cases, list) or not cases:
        return ["输入必须是非空 JSON 数组"], warnings
    for index, case in enumerate(cases, 1):
        label = f"用例 {index}"
        if not isinstance(case, dict):
            errors.append(f"{label}: 必须是对象")
            continue
        modules = case.get("模块")
        if not isinstance(modules, list) or not 2 <= len(modules) <= 8:
            errors.append(f"{label}: 模块必须为 2-8 层数组")
        elif modules[0] not in ALLOWED_CLASSES:
            errors.append(f"{label}: 首层模块必须是核心用例、衍生用例或待确认")
        for field in ("用例标题", "需求ID"):
            if not str(case.get(field, "")).strip():
                errors.append(f"{label}: 缺少{field}")
        if case.get("优先级") not in ALLOWED_PRIORITIES:
            errors.append(f"{label}: 优先级无效")
        methods = case.get("设计方法")
        if not isinstance(methods, list) or not methods or set(methods) - ALLOWED_METHODS:
            errors.append(f"{label}: 设计方法必须为 EP/BVA/ST/EG 数组")
        if case.get("标签") not in ALLOWED_TAGS:
            errors.append(f"{label}: 标签必须为 APP、Android 或 iOS")
        steps = case.get("步骤")
        if not isinstance(steps, list) or not steps:
            errors.append(f"{label}: 至少需要一个步骤")
            continue
        for number, step in enumerate(steps, 1):
            if not isinstance(step, dict):
                errors.append(f"{label} 步骤 {number}: 必须是对象")
                continue
            action, expected = str(step.get("操作", "")), str(step.get("预期", ""))
            if not re.match(rf"^{number}\.\s+\S", action):
                errors.append(f"{label} 步骤 {number}: 操作编号错误")
            if not re.match(rf"^{number}\.\s+\S", expected):
                errors.append(f"{label} 步骤 {number}: 预期编号错误")
        if modules and modules[0] == "待确认" and not str(case.get("备注", "")).startswith("待确认："):
            warnings.append(f"{label}: 待确认用例建议添加待确认备注")
    return errors, warnings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    try:
        cases = json.loads(Path(args.file).read_text(encoding="utf-8"))
        errors, warnings = validate(cases)
        for item in warnings:
            print(f"警告: {item}")
        for item in errors:
            print(f"错误: {item}", file=sys.stderr)
        if errors:
            sys.exit(1)
        print(f"校验通过: {len(cases)} 条用例")
    except Exception as exc:
        print(f"校验失败: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
