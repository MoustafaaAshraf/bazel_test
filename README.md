# Bazel Playground

A simple Python project to play around with Bazel.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/MoustafaaAshraf/bazel_test.git
cd bazel_test

# Run the main application
bazel run //:main

# Run all tests
bazel test //...
```

## 📋 Prerequisites

- **Bazel**: Version 6.0 or later
- **Python**: Version 3.10 or later
- **Operating System**: macOS, Linux, or Windows

### Installing Bazel

**macOS:**
```bash
# Using Homebrew
brew install bazel
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install curl gnupg
curl -fsSL https://bazel.build/bazel-release.pub | gpg --dearmor > bazel.gpg
sudo mv bazel.gpg /etc/apt/trusted.gpg.d/
echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
sudo apt update && sudo apt install bazel
```

## 🏗️ Project Structure

```
bazel_test/
├── BUILD                 # Root build file
├── MODULE.bazel         # Workspace configuration
├── .bazelrc            # Bazel configuration
├── main.py             # Main application entry point
├── utils/
│   ├── BUILD           # Utils package build file
│   ├── math_utils.py   # Math utility functions
│   └── math_utils_test.py # Unit tests
└── README.md           # This file
```

## 🛠️ Building

### Build the main application
```bash
bazel build //:main
```

### Run the application
```bash
bazel run //:main
```

### Build everything
```bash
bazel build //...
```

## 🧪 Testing

### Run all tests
```bash
bazel test //...
```

### Run specific test
```bash
bazel test //utils:math_utils_test
```

### Run tests with detailed output
```bash
bazel test //utils:math_utils_test --test_output=all
```

### Run tests with coverage
```bash
bazel coverage //utils:math_utils_test
```

## 📦 Adding New Code

### Adding a new Python module

1. Create your Python file (e.g., `utils/string_utils.py`)
2. Update `utils/BUILD` to include the new module:

```bazel
py_library(
    name = "utils",
    srcs = [
        "math_utils.py",
        "string_utils.py",  # Add your new file here
    ],
    visibility = ["//visibility:public"],
)
```

### Adding a new test

1. Create your test file (e.g., `utils/string_utils_test.py`)
2. Add a test target to `utils/BUILD`:

```bazel
py_test(
    name = "string_utils_test",
    srcs = ["string_utils_test.py"],
    deps = [":utils"],
)
```

## 🔧 Configuration

### .bazelrc
The `.bazelrc` file contains Bazel configuration options:

- **Python version**: Set to Python PY3
- **Build caching**: Enabled for faster builds
- **Test strategy**: Configured for optimal test execution
- **Verbose failures**: Better error messages

### MODULE.bazel
Defines the workspace and dependencies:

- **Module name**: `bazel_test`
- **Python rules**: Latest version of `rules_python`
- **Python toolchain**: Configured for Python PY3

## 🚀 Bazel Commands Cheat Sheet

| Command | Description |
|---------|-------------|
| `bazel build //:target` | Build a specific target |
| `bazel build //...` | Build all targets |
| `bazel run //:target` | Build and run a target |
| `bazel test //...` | Run all tests |
| `bazel query //...` | Query the dependency graph |
| `bazel clean` | Clean build artifacts |
| `bazel info` | Show Bazel configuration |
| `bazel help` | Show help information |

## 🔍 Understanding Bazel Concepts

### Targets
- **py_binary**: Executable Python programs
- **py_library**: Reusable Python modules
- **py_test**: Python test suites

### Dependencies
- **deps**: Runtime dependencies
- **data**: Data files needed at runtime
- **srcs**: Source files for the target

### Visibility
- **//visibility:public**: Can be used by any target
- **//visibility:private**: Only usable within the same package
- **//some/package:__pkg__**: Only usable within the specified package

## 🐛 Troubleshooting

### Common Issues

**"No module named 'math_utils'"**
- Ensure you're using the correct import path: `from utils.math_utils import add`
- Check that the dependency is properly declared in BUILD files

**"Target not found"**
- Verify the target name in your BUILD file
- Check that the target exists in the specified package

**"Build failed"**
- Run `bazel clean` and try again
- Check the error messages for specific issues

### Getting Help

```bash
# Show detailed build information
bazel build //:main --verbose_failures

# Show dependency graph
bazel query --noimplicit_deps "deps(//:main)" --output=graph

# Show build configuration
bazel info
```

## 📚 Learning Resources

- [Bazel Official Documentation](https://bazel.build/docs)
- [Python Rules for Bazel](https://github.com/bazelbuild/rules_python)
- [Bazel Tutorial](https://bazel.build/start)
- [Bazel Best Practices](https://bazel.build/rules/best-practices)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass: `bazel test //...`
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy Building with Bazel! 🎉** 
