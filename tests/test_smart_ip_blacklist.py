"""Tests for smart-ip-blacklist."""

import pytest
from smart_ip_blacklist import blacklist


class TestBlacklist:
    """Test suite for blacklist."""

    def test_basic(self):
        """Test basic usage."""
        result = blacklist("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            blacklist("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = blacklist(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
