# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/player_id.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()



DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/player_id.proto',
  package='api',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x13\x61pi/player_id.proto\x12\x03\x61pi\"\x16\n\x08PlayerId\x12\n\n\x02id\x18\x01 \x01(\t'
)




_PLAYERID = _descriptor.Descriptor(
  name='PlayerId',
  full_name='api.PlayerId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.PlayerId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=50,
)

DESCRIPTOR.message_types_by_name['PlayerId'] = _PLAYERID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerId = _reflection.GeneratedProtocolMessageType('PlayerId', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERID,
  '__module__' : 'api.player_id_pb2'
  # @@protoc_insertion_point(class_scope:api.PlayerId)
  })
_sym_db.RegisterMessage(PlayerId)


# @@protoc_insertion_point(module_scope)
