from pymqpcf import get_version


def test_get_version_reports_version() -> None:
    assert get_version()
