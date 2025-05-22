# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-01-22

### Added
- Modern `pyproject.toml` configuration for project metadata and dependencies
- Optional dependency groups for development, machine learning, and visualization
- Support for Python 3.9-3.12

### Changed
- **BREAKING**: Updated minimum Python version from 3.8 to 3.9
- **BREAKING**: Replaced deprecated `rtdl` package with `rtdl_revisiting_models`
- Updated all core dependencies to modern versions:
  - numpy: `==1.23.5` → `>=1.24.0`
  - ray: `==2.2` → `>=2.5.0`
  - torch: unversioned → `>=2.0.0`
  - torchvision: unversioned → `>=0.15.0`
  - scikit-learn: unversioned → `>=1.3.0`
  - pandas: unversioned → `>=2.0.0`
  - pytorch-lightning: `==1.9.4` → `>=2.0.0`
  - rtdl: `>=0.0.13` → `rtdl_revisiting_models` (improved API)
- Relaxed strict version pins to minimum version requirements
- Updated environment.yml to use modern dependency specifications

### Fixed
- Replaced deprecated `np.int` with `np.int32` throughout codebase
- Replaced deprecated `train.torch.get_device()` with modern `torch.device()` API
- Updated Ray initialization to use modern `runtime_env` parameter instead of deprecated `_temp_dir`
- Fixed setuptools import to use modern setuptools instead of distutils
- Updated rtdl imports and API calls to use `rtdl_revisiting_models` package

### Deprecated
- Legacy exact version pinning in requirements.txt
- Old `rtdl` package (replaced with `rtdl_revisiting_models`)

### Technical Details
- Fixed compatibility issues with:
  - NumPy 1.24+ (removed deprecated scalar types)
  - PyTorch 2.0+ (updated device handling)
  - Ray 2.5+ (updated initialization API)
  - Python 3.9+ (modern syntax and typing)
  - rtdl_revisiting_models (updated imports and API usage)

## [0.1.0] - Original Release

### Added
- Initial TableShift implementation
- Support for distribution shift benchmarking on tabular data
- Integration with Ray for distributed training
- Multiple model support including XGBoost, LightGBM, and PyTorch models