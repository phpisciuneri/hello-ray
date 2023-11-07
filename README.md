# hello-ray

Demo of RLLib from [Ray](https://github.com/ray-project/ray).

## Prerequisites

- Python 3.10
- virtualenv

## Environment Setup

```bat
virtualenv.exe venv
.\venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

## Build

```
bazel build //:cartpole
```

## Run

```bat
.\bazel-bin\cartpole.exe
```