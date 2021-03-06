# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streaming_proto/streaming_pi.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='streaming_proto/streaming_pi.proto',
  package='pi',
  syntax='proto3',
  serialized_pb=_b('\n\"streaming_proto/streaming_pi.proto\x12\x02pi\"\x16\n\tPiRequest\x12\t\n\x01n\x18\x01 \x01(\x05\"&\n\nPiResponse\x12\t\n\x01n\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01\x32:\n\x0bPiCaculator\x12+\n\x04\x43\x61lc\x12\r.pi.PiRequest\x1a\x0e.pi.PiResponse\"\x00(\x01\x30\x01\x62\x06proto3')
)




_PIREQUEST = _descriptor.Descriptor(
  name='PiRequest',
  full_name='pi.PiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n', full_name='pi.PiRequest.n', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=64,
)


_PIRESPONSE = _descriptor.Descriptor(
  name='PiResponse',
  full_name='pi.PiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n', full_name='pi.PiResponse.n', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='pi.PiResponse.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['PiRequest'] = _PIREQUEST
DESCRIPTOR.message_types_by_name['PiResponse'] = _PIRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PiRequest = _reflection.GeneratedProtocolMessageType('PiRequest', (_message.Message,), dict(
  DESCRIPTOR = _PIREQUEST,
  __module__ = 'streaming_proto.streaming_pi_pb2'
  # @@protoc_insertion_point(class_scope:pi.PiRequest)
  ))
_sym_db.RegisterMessage(PiRequest)

PiResponse = _reflection.GeneratedProtocolMessageType('PiResponse', (_message.Message,), dict(
  DESCRIPTOR = _PIRESPONSE,
  __module__ = 'streaming_proto.streaming_pi_pb2'
  # @@protoc_insertion_point(class_scope:pi.PiResponse)
  ))
_sym_db.RegisterMessage(PiResponse)



_PICACULATOR = _descriptor.ServiceDescriptor(
  name='PiCaculator',
  full_name='pi.PiCaculator',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=106,
  serialized_end=164,
  methods=[
  _descriptor.MethodDescriptor(
    name='Calc',
    full_name='pi.PiCaculator.Calc',
    index=0,
    containing_service=None,
    input_type=_PIREQUEST,
    output_type=_PIRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PICACULATOR)

DESCRIPTOR.services_by_name['PiCaculator'] = _PICACULATOR

# @@protoc_insertion_point(module_scope)
