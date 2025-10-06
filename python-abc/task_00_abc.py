#!/usr/bin/env python3
"""Defines abstract Animal class and its subclasses Dog and Cat."""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals.""" 
    
    @abstractmethod
    def speak(self):
        """Abstract method to be implemented by subclasses."""
        pass