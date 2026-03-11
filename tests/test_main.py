def test_simple():
    assert 1 + 1 == 2

def test_uv_working():
    import sys
    # 验证是否使用的是我们指定的 Python 3.12
    assert sys.version_info.major == 3
    assert sys.version_info.minor == 12