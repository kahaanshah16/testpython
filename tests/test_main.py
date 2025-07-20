"""
Tests for the main module.
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import greet, add_numbers


class TestGreet:
    """Test cases for the greet function."""
    
    def test_greet_with_name(self):
        """Test greeting with a specific name."""
        result = greet("Alice")
        assert result == "Hello, Alice! Welcome to my Python project."
    
    def test_greet_with_empty_string(self):
        """Test greeting with an empty string."""
        result = greet("")
        assert result == "Hello, ! Welcome to my Python project."


class TestAddNumbers:
    """Test cases for the add_numbers function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        result = add_numbers(5, 3)
        assert result == 8
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        result = add_numbers(-5, -3)
        assert result == -8
    
    def test_add_zero(self):
        """Test adding zero to a number."""
        result = add_numbers(5, 0)
        assert result == 5
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        result = add_numbers(3.14, 2.86)
        assert result == 6.0 