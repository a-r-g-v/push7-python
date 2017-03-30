# encoding: utf8


class ClientErrorException(Exception):
    pass


class ServerErrorException(Exception):
    pass


class UnauthorizedException(ClientErrorException):
    pass


class ForbiddenException(ClientErrorException):
    pass


class NotFoundException(ClientErrorException):
    pass


class MethodNotAllowedException(ClientErrorException):
    pass
