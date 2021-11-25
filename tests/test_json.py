from openforbc_benchmark.json import BenchmarkInfo, CommandInfo, PresetInfo


def test_benchmark_serialization() -> None:
    benchmark = BenchmarkInfo(
        "name",
        "desc",
        None,
        [CommandInfo("echo Hello world")],
        None,
        CommandInfo("echo {}"),
        False,
    )
    assert isinstance(benchmark, BenchmarkInfo)


def test_benchmark_deserialization() -> None:
    from json import loads

    json = r"""
    {
        "name": "Dummy Benchmark",
        "description": "Prints something to the output",
        "run_command": "echo Hello world!",
        "setup_command": {
            "command": "echo",
            "env": {
            "INSTALL": "1",
            "ENVIRONMENT": "production"
            },
            "workdir": "presets"
        },
        "cleanup_command": {
            "command": [
            "echo",
            "daw"
            ]
        },
        "stats": {
            "data_1": {
            "regex": "data: (\\d+)",
            "file": "test/output.log"
            }
        }
    }
    """
    benchmark = BenchmarkInfo.deserialize(loads(json))
    assert isinstance(benchmark, BenchmarkInfo)


def test_benchmark_preset() -> None:
    preset = PresetInfo(
        "--config=gpu_48x48.json", [CommandInfo("init.sh --preset=gpu_48x48.json")]
    )
    assert isinstance(preset, PresetInfo)


def test_benchmark_preset_deserialization() -> None:
    from json import loads

    json = r"""
    {
        "args": "--config=preset_57.conf",
        "init_command": "setup_preset.sh preset_57.conf",
        "post_command": "setup_preset.sh --teardown"
    }
    """
    preset = PresetInfo.deserialize(loads(json))
    assert isinstance(preset, PresetInfo)


def test_command() -> None:
    command = CommandInfo("/bin/true")
    assert isinstance(command, CommandInfo)


def test_command_deserialize() -> None:
    assert isinstance(CommandInfo.deserialize("/bin/echo Hello"), CommandInfo)
    assert isinstance(
        CommandInfo.deserialize({"command": "/bin/true", "env": {"GPU": "CUDA"}}),
        CommandInfo,
    )
    assert isinstance(
        CommandInfo.deserialize(
            {"command": ["echo", "hello world"], "env": {"GPU": "CUDA"}}
        ),
        CommandInfo,
    )
    assert isinstance(
        CommandInfo.deserialize(
            {
                "command": ["echo", "hello world"],
                "env": {"GPU": "CUDA"},
                "workdir": "presets/gpu",
            }
        ),
        CommandInfo,
    )
