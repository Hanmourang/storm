#!/usr/bin/env python
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:utf8strings
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import logging
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def sendSupervisorAssignments(self, assignments):
    """
    Send node specific assignments to supervisor

    Parameters:
     - assignments
    """
    pass

  def getLocalAssignmentForStorm(self, id):
    """
    Get local assignment for a storm

    Parameters:
     - id
    """
    pass

  def sendSupervisorWorkerHeartbeat(self, heartbeat):
    """
    Send worker heartbeat to local supervisor

    Parameters:
     - heartbeat
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def sendSupervisorAssignments(self, assignments):
    """
    Send node specific assignments to supervisor

    Parameters:
     - assignments
    """
    self.send_sendSupervisorAssignments(assignments)
    self.recv_sendSupervisorAssignments()

  def send_sendSupervisorAssignments(self, assignments):
    self._oprot.writeMessageBegin('sendSupervisorAssignments', TMessageType.CALL, self._seqid)
    args = sendSupervisorAssignments_args()
    args.assignments = assignments
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_sendSupervisorAssignments(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = sendSupervisorAssignments_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.aze is not None:
      raise result.aze
    return

  def getLocalAssignmentForStorm(self, id):
    """
    Get local assignment for a storm

    Parameters:
     - id
    """
    self.send_getLocalAssignmentForStorm(id)
    return self.recv_getLocalAssignmentForStorm()

  def send_getLocalAssignmentForStorm(self, id):
    self._oprot.writeMessageBegin('getLocalAssignmentForStorm', TMessageType.CALL, self._seqid)
    args = getLocalAssignmentForStorm_args()
    args.id = id
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getLocalAssignmentForStorm(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = getLocalAssignmentForStorm_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.e is not None:
      raise result.e
    if result.aze is not None:
      raise result.aze
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getLocalAssignmentForStorm failed: unknown result")

  def sendSupervisorWorkerHeartbeat(self, heartbeat):
    """
    Send worker heartbeat to local supervisor

    Parameters:
     - heartbeat
    """
    self.send_sendSupervisorWorkerHeartbeat(heartbeat)
    self.recv_sendSupervisorWorkerHeartbeat()

  def send_sendSupervisorWorkerHeartbeat(self, heartbeat):
    self._oprot.writeMessageBegin('sendSupervisorWorkerHeartbeat', TMessageType.CALL, self._seqid)
    args = sendSupervisorWorkerHeartbeat_args()
    args.heartbeat = heartbeat
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_sendSupervisorWorkerHeartbeat(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = sendSupervisorWorkerHeartbeat_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.aze is not None:
      raise result.aze
    return


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["sendSupervisorAssignments"] = Processor.process_sendSupervisorAssignments
    self._processMap["getLocalAssignmentForStorm"] = Processor.process_getLocalAssignmentForStorm
    self._processMap["sendSupervisorWorkerHeartbeat"] = Processor.process_sendSupervisorWorkerHeartbeat

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_sendSupervisorAssignments(self, seqid, iprot, oprot):
    args = sendSupervisorAssignments_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = sendSupervisorAssignments_result()
    try:
      self._handler.sendSupervisorAssignments(args.assignments)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except AuthorizationException as aze:
      msg_type = TMessageType.REPLY
      result.aze = aze
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("sendSupervisorAssignments", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getLocalAssignmentForStorm(self, seqid, iprot, oprot):
    args = getLocalAssignmentForStorm_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getLocalAssignmentForStorm_result()
    try:
      result.success = self._handler.getLocalAssignmentForStorm(args.id)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except NotAliveException as e:
      msg_type = TMessageType.REPLY
      result.e = e
    except AuthorizationException as aze:
      msg_type = TMessageType.REPLY
      result.aze = aze
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("getLocalAssignmentForStorm", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_sendSupervisorWorkerHeartbeat(self, seqid, iprot, oprot):
    args = sendSupervisorWorkerHeartbeat_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = sendSupervisorWorkerHeartbeat_result()
    try:
      self._handler.sendSupervisorWorkerHeartbeat(args.heartbeat)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except AuthorizationException as aze:
      msg_type = TMessageType.REPLY
      result.aze = aze
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("sendSupervisorWorkerHeartbeat", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class sendSupervisorAssignments_args:
  """
  Attributes:
   - assignments
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'assignments', (SupervisorAssignments, SupervisorAssignments.thrift_spec), None, ), # 1
  )

  def __init__(self, assignments=None,):
    self.assignments = assignments

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.assignments = SupervisorAssignments()
          self.assignments.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('sendSupervisorAssignments_args')
    if self.assignments is not None:
      oprot.writeFieldBegin('assignments', TType.STRUCT, 1)
      self.assignments.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.assignments)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class sendSupervisorAssignments_result:
  """
  Attributes:
   - aze
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'aze', (AuthorizationException, AuthorizationException.thrift_spec), None, ), # 1
  )

  def __init__(self, aze=None,):
    self.aze = aze

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.aze = AuthorizationException()
          self.aze.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('sendSupervisorAssignments_result')
    if self.aze is not None:
      oprot.writeFieldBegin('aze', TType.STRUCT, 1)
      self.aze.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.aze)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getLocalAssignmentForStorm_args:
  """
  Attributes:
   - id
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
  )

  def __init__(self, id=None,):
    self.id = id

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getLocalAssignmentForStorm_args')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.id)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getLocalAssignmentForStorm_result:
  """
  Attributes:
   - success
   - e
   - aze
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Assignment, Assignment.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'e', (NotAliveException, NotAliveException.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'aze', (AuthorizationException, AuthorizationException.thrift_spec), None, ), # 2
  )

  def __init__(self, success=None, e=None, aze=None,):
    self.success = success
    self.e = e
    self.aze = aze

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = Assignment()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.e = NotAliveException()
          self.e.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.aze = AuthorizationException()
          self.aze.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getLocalAssignmentForStorm_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.e is not None:
      oprot.writeFieldBegin('e', TType.STRUCT, 1)
      self.e.write(oprot)
      oprot.writeFieldEnd()
    if self.aze is not None:
      oprot.writeFieldBegin('aze', TType.STRUCT, 2)
      self.aze.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.e)
    value = (value * 31) ^ hash(self.aze)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class sendSupervisorWorkerHeartbeat_args:
  """
  Attributes:
   - heartbeat
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'heartbeat', (SupervisorWorkerHeartbeat, SupervisorWorkerHeartbeat.thrift_spec), None, ), # 1
  )

  def __init__(self, heartbeat=None,):
    self.heartbeat = heartbeat

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.heartbeat = SupervisorWorkerHeartbeat()
          self.heartbeat.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('sendSupervisorWorkerHeartbeat_args')
    if self.heartbeat is not None:
      oprot.writeFieldBegin('heartbeat', TType.STRUCT, 1)
      self.heartbeat.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.heartbeat)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class sendSupervisorWorkerHeartbeat_result:
  """
  Attributes:
   - aze
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'aze', (AuthorizationException, AuthorizationException.thrift_spec), None, ), # 1
  )

  def __init__(self, aze=None,):
    self.aze = aze

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.aze = AuthorizationException()
          self.aze.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('sendSupervisorWorkerHeartbeat_result')
    if self.aze is not None:
      oprot.writeFieldBegin('aze', TType.STRUCT, 1)
      self.aze.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.aze)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
