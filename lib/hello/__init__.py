# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: proto/example.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class Greeting(betterproto.Message):
    """Greeting represents a message you can tell a user."""

    message: str = betterproto.string_field(1)
