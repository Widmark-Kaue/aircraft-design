#!/usr/bin/env python3
class AircraftDesignError(Exception):
    def __init__(self, message) -> None:
        self.message = message

        super().__init__(message)
