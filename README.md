## Repo Intro
This repository contains the code used to generate videos
uploaded by 蓝叉戟 / Bluevect.

The code used the library [ManimGL](https://github.com/3b1b/manim) by [3Blue1Brown](https://github.com/3b1b).
Appreciations for [3Blue1Brown](https://github.com/3b1b)'s great development!

Feel free to read the code and regenerate the original videos if you are interested.
However, **re-uploading the generated videos without permission is strictly prohibited**.

## Reproduce videos
Note: make sure you have [ManimGL](https://github.com/3b1b/manim) installed and a suitable python environment
(3.8) to get the best performance.

Before running manimgl, set PythonPath to the path of this repo first to avoid the error
`ModuleNotFoundError: No module named 'manim_imports_ext'`.

```commandline
set PYTHONPATH=path\to\this\repo
```

Then you can run scenes with manimgl.
Make sure you use the config in the root folder or errors may occur.

```commandline
manimgl --config_file [Path to custom_config.yml] [Path to the scene] [SceneName]
```

You may get the warning `WARNING  Unsupported element type: <class 'svgelements.svgelements.Use'>` when running the scenes.
This is due to an issue with the version 1.6.1. Do a temporary hack to solve this issue.
Check this issue [here](https://github.com/3b1b/manim/issues/1904).

Solution by YishiMichael:
Change the line
```python
if isinstance(shape, se.Group):
```

into
```python
if isinstance(shape, (se.Group, se.Use)):
```

at https://github.com/3b1b/manim/blob/v1.6.1/manimlib/mobject/svg/svg_mobject.py#L153.

## List of files used to generate videos
- _2022/lines_slope_theory.py => [\[Manim\]\[初中\]垂直的直线斜率相乘等于-1的证明](https://www.bilibili.com/video/BV1rr4y1h7H1)
- _2022/properties_of_a_function.py => [\[Manim\]\[初中\]探究一类函数的性质](https://www.bilibili.com/video/BV1ri4y1S7Qt)
