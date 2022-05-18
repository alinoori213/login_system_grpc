# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10proto/auth.proto\x12\x0e\x61uthentication\"/\n\x0cLoginRequest\x12\r\n\x05phone\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\".\n\rLoginResponse\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\"C\n\rSignupRequest\x12\r\n\x05phone\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x11\n\tpassword2\x18\x03 \x01(\t\"/\n\x0eSignupResponse\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\"/\n\x10LoginCodeRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\"#\n\x11LoginCodeResponse\x12\x0e\n\x06status\x18\x02 \x01(\x05\"!\n\x10\x43heckUserRequest\x12\r\n\x05phone\x18\x01 \x01(\t\"2\n\x11\x43heckUserResponse\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\"0\n\x11SignupCodeRequest\x12\r\n\x05phone\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\"3\n\x12SignupCodeResponse\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\"*\n\x19ResetPasswordCheckRequest\x12\r\n\x05phone\x18\x01 \x01(\t\"J\n\x1aResetPasswordCheckResponse\x12\r\n\x05token\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\",\n\x1bResetPasswordConfirmRequest\x12\r\n\x05token\x18\x01 \x01(\t\"?\n\x1cResetPasswordConfirmResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t2\xf8\x04\n\x0e\x41uthentication\x12\x44\n\x05Login\x12\x1c.authentication.LoginRequest\x1a\x1d.authentication.LoginResponse\x12G\n\x06Signup\x12\x1d.authentication.SignupRequest\x1a\x1e.authentication.SignupResponse\x12P\n\tLoginCode\x12 .authentication.LoginCodeRequest\x1a!.authentication.LoginCodeResponse\x12S\n\nSignupCode\x12!.authentication.SignupCodeRequest\x1a\".authentication.SignupCodeResponse\x12P\n\tCheckUser\x12 .authentication.CheckUserRequest\x1a!.authentication.CheckUserResponse\x12k\n\x12ResetPasswordCheck\x12).authentication.ResetPasswordCheckRequest\x1a*.authentication.ResetPasswordCheckResponse\x12q\n\x14ResetPasswordConfirm\x12+.authentication.ResetPasswordConfirmRequest\x1a,.authentication.ResetPasswordConfirmResponseb\x06proto3')



_LOGINREQUEST = DESCRIPTOR.message_types_by_name['LoginRequest']
_LOGINRESPONSE = DESCRIPTOR.message_types_by_name['LoginResponse']
_SIGNUPREQUEST = DESCRIPTOR.message_types_by_name['SignupRequest']
_SIGNUPRESPONSE = DESCRIPTOR.message_types_by_name['SignupResponse']
_LOGINCODEREQUEST = DESCRIPTOR.message_types_by_name['LoginCodeRequest']
_LOGINCODERESPONSE = DESCRIPTOR.message_types_by_name['LoginCodeResponse']
_CHECKUSERREQUEST = DESCRIPTOR.message_types_by_name['CheckUserRequest']
_CHECKUSERRESPONSE = DESCRIPTOR.message_types_by_name['CheckUserResponse']
_SIGNUPCODEREQUEST = DESCRIPTOR.message_types_by_name['SignupCodeRequest']
_SIGNUPCODERESPONSE = DESCRIPTOR.message_types_by_name['SignupCodeResponse']
_RESETPASSWORDCHECKREQUEST = DESCRIPTOR.message_types_by_name['ResetPasswordCheckRequest']
_RESETPASSWORDCHECKRESPONSE = DESCRIPTOR.message_types_by_name['ResetPasswordCheckResponse']
_RESETPASSWORDCONFIRMREQUEST = DESCRIPTOR.message_types_by_name['ResetPasswordConfirmRequest']
_RESETPASSWORDCONFIRMRESPONSE = DESCRIPTOR.message_types_by_name['ResetPasswordConfirmResponse']
LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'proto.auth_pb2'
  # @@protoc_insertion_point(class_scope:authentication.LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE,
  '__module__' : 'proto.auth_pb2'
  # @@protoc_insertion_point(class_scope:authentication.LoginResponse)
  })
_sym_db.RegisterMessage(LoginResponse)

SignupRequest = _reflection.GeneratedProtocolMessageType('SignupRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPREQUEST,
  '__module__' : 'proto.auth_pb2'
  # @@protoc_insertion_point(class_scope:authentication.SignupRequest)
  })
_sym_db.RegisterMessage(SignupRequest)

SignupResponse = _reflection.GeneratedProtocolMessageType('SignupResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPRESPONSE,
  '__module__' : 'proto.auth_pb2'
  # @@protoc_insertion_point(class_scope:authentication.SignupResponse)
  })
_sym_db.RegisterMessage(SignupResponse)

LoginCodeRequest = _reflection.GeneratedProtocolMessageType('LoginCodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINCODEREQUEST,
  '__module__' : 'proto.auth_pb2'
  # @@protoc_insertion_point(class_scope:authentication.LoginCodeRequest)
  })
_sym_db.RegisterMessage(LoginCodeRequest)

LoginCodeResponse = _reflection.GeneratedProtocolMessageType('LoginCodeResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINCODERESPONSE,
  '__module__' : 'proto.auth_pb2'
  # @@protoc_insertion_point(class_scope:authentication.LoginCodeResponse)
  })
_sym_db.RegisterMessage(LoginCodeResponse)

CheckUserRequest = _reflection.GeneratedProtocolMessageType('CheckUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKUSERREQUEST,
  '__module__' : 'proto.auth_pb2'
  # @@protoc_insertion_point(class_scope:authentication.CheckUserRequest)
  })
_sym_db.RegisterMessage(CheckUserRequest)

CheckUserResponse = _reflection.GeneratedProtocolMessageType('CheckUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKUSERRESPONSE,
  '__module__' : 'proto.auth_pb2'
  # @@protoc_insertion_point(class_scope:authentication.CheckUserResponse)
  })
_sym_db.RegisterMessage(CheckUserResponse)

SignupCodeRequest = _reflection.GeneratedProtocolMessageType('SignupCodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPCODEREQUEST,
  '__module__' : 'proto.auth_pb2'
  # @@protoc_insertion_point(class_scope:authentication.SignupCodeRequest)
  })
_sym_db.RegisterMessage(SignupCodeRequest)

SignupCodeResponse = _reflection.GeneratedProtocolMessageType('SignupCodeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPCODERESPONSE,
  '__module__' : 'proto.auth_pb2'
  # @@protoc_insertion_point(class_scope:authentication.SignupCodeResponse)
  })
_sym_db.RegisterMessage(SignupCodeResponse)

ResetPasswordCheckRequest = _reflection.GeneratedProtocolMessageType('ResetPasswordCheckRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETPASSWORDCHECKREQUEST,
  '__module__' : 'proto.auth_pb2'
  # @@protoc_insertion_point(class_scope:authentication.ResetPasswordCheckRequest)
  })
_sym_db.RegisterMessage(ResetPasswordCheckRequest)

ResetPasswordCheckResponse = _reflection.GeneratedProtocolMessageType('ResetPasswordCheckResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESETPASSWORDCHECKRESPONSE,
  '__module__' : 'proto.auth_pb2'
  # @@protoc_insertion_point(class_scope:authentication.ResetPasswordCheckResponse)
  })
_sym_db.RegisterMessage(ResetPasswordCheckResponse)

ResetPasswordConfirmRequest = _reflection.GeneratedProtocolMessageType('ResetPasswordConfirmRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETPASSWORDCONFIRMREQUEST,
  '__module__' : 'proto.auth_pb2'
  # @@protoc_insertion_point(class_scope:authentication.ResetPasswordConfirmRequest)
  })
_sym_db.RegisterMessage(ResetPasswordConfirmRequest)

ResetPasswordConfirmResponse = _reflection.GeneratedProtocolMessageType('ResetPasswordConfirmResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESETPASSWORDCONFIRMRESPONSE,
  '__module__' : 'proto.auth_pb2'
  # @@protoc_insertion_point(class_scope:authentication.ResetPasswordConfirmResponse)
  })
_sym_db.RegisterMessage(ResetPasswordConfirmResponse)

_AUTHENTICATION = DESCRIPTOR.services_by_name['Authentication']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOGINREQUEST._serialized_start=36
  _LOGINREQUEST._serialized_end=83
  _LOGINRESPONSE._serialized_start=85
  _LOGINRESPONSE._serialized_end=131
  _SIGNUPREQUEST._serialized_start=133
  _SIGNUPREQUEST._serialized_end=200
  _SIGNUPRESPONSE._serialized_start=202
  _SIGNUPRESPONSE._serialized_end=249
  _LOGINCODEREQUEST._serialized_start=251
  _LOGINCODEREQUEST._serialized_end=298
  _LOGINCODERESPONSE._serialized_start=300
  _LOGINCODERESPONSE._serialized_end=335
  _CHECKUSERREQUEST._serialized_start=337
  _CHECKUSERREQUEST._serialized_end=370
  _CHECKUSERRESPONSE._serialized_start=372
  _CHECKUSERRESPONSE._serialized_end=422
  _SIGNUPCODEREQUEST._serialized_start=424
  _SIGNUPCODEREQUEST._serialized_end=472
  _SIGNUPCODERESPONSE._serialized_start=474
  _SIGNUPCODERESPONSE._serialized_end=525
  _RESETPASSWORDCHECKREQUEST._serialized_start=527
  _RESETPASSWORDCHECKREQUEST._serialized_end=569
  _RESETPASSWORDCHECKRESPONSE._serialized_start=571
  _RESETPASSWORDCHECKRESPONSE._serialized_end=645
  _RESETPASSWORDCONFIRMREQUEST._serialized_start=647
  _RESETPASSWORDCONFIRMREQUEST._serialized_end=691
  _RESETPASSWORDCONFIRMRESPONSE._serialized_start=693
  _RESETPASSWORDCONFIRMRESPONSE._serialized_end=756
  _AUTHENTICATION._serialized_start=759
  _AUTHENTICATION._serialized_end=1391
# @@protoc_insertion_point(module_scope)
