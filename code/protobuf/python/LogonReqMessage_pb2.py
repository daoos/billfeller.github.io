# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LogonReqMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='LogonReqMessage.proto',
  package='',
  serialized_pb='\n\x15LogonReqMessage.proto\"1\n\x0fLogonReqMessage\x12\x0e\n\x06\x61\x63\x63tID\x18\x01 \x02(\x03\x12\x0e\n\x06passwd\x18\x02 \x02(\tB\x02H\x03')




_LOGONREQMESSAGE = _descriptor.Descriptor(
  name='LogonReqMessage',
  full_name='LogonReqMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acctID', full_name='LogonReqMessage.acctID', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='passwd', full_name='LogonReqMessage.passwd', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=25,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['LogonReqMessage'] = _LOGONREQMESSAGE

class LogonReqMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGONREQMESSAGE

  # @@protoc_insertion_point(class_scope:LogonReqMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003')
# @@protoc_insertion_point(module_scope)