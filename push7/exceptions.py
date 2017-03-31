# encoding: utf8


class Push7BaseException(Exception):
    pass


class ClientErrorException(Push7BaseException):
    pass


class ServerErrorException(Push7BaseException):
    pass


class UnauthorizedException(ClientErrorException):
    pass


class ForbiddenException(ClientErrorException):
    pass


class NotFoundException(ClientErrorException):
    pass


class MethodNotAllowedException(ClientErrorException):
    pass
