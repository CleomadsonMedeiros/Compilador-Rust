from abc import abstractmethod
from abc import ABCMeta


class Program():
  def __init__(self, main):
    self.main = main
  def accept(self, visitor):
    visitor.visitProgram(self)

class MainF():
  def __init__(self, blockStatement):
    self.blockStatement = blockStatement
  def accept(self, visitor):
    visitor.visitMainFunction(self)

class StatementListStatement():
  def __init__(self, statement):
    self.statement = statement
  def accept(self, visitor):
    visitor.visitStatementListStatement(self)

class StatementList():
  def __init__(self, statement, statementList):
    self.statement = statement
    self.statementList = statementList
  def accept(self, visitor):
    visitor.visitStatementList(self)

class DefFunction():
  def __init__(self, paramList, returnType, blockStatement):
    self.paramList = paramList
    self.returnType = returnType
    self.blockStatement = blockStatement
  def accept(self, visitor):
    visitor.visitDefFunction(self)

class DefFunctionUnit():
  def __init__(self, id, blockStatement):
    self.id = id
    self.blockStatement = blockStatement
  def accept(self, visitor):
    visitor.visitDefFunctionUnit(self)

class FunctionCall():
  def __init__(self, id):
    self.id = id
  def accept(self, visitor):
    visitor.visitFunctionCall(self)

class FunctionCallIdList():
  def __init__(self, id, idList):
    self.id = id
    self.idList = idList
  def accept(self, visitor):
    visitor.visitFunctionCallIdList(self)

class IdListIdNumIdList():
  def __init__(self, idNum, idList):
    self.idNum = idNum
    self.idList = idList
  def accept(self, visitor):
    visitor.visitIdListIdNumIdList()

class IdListIdNumFunctionCall():
  def __init__(self, idNumFunctionCall):
    self.idNumFunctionCall = idNumFunctionCall
  def accept(self, visitor):
    visitor.visitIdListIdNumFunctionCall(self)