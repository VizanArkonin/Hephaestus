"""
Socket server - GPIO board calls routing library.
"""
from board_controller.common.packets.packet_status import PacketStatus
from board_controller.common.utils import generic_response_validator
from board_controller.server import __server as server


@server.route(packet_name="GetGPIOBoardStatus")
def status(client, data):
    """
    GPIO board status processor.

    :param client: ClientThread instance
    :param data: Decrypted and deserialized packet dict
    :return: None
    """
    status = data["payload"]["status"]
    errors = data["errors"]
    if status == PacketStatus.SUCCESS.value:
        client.client_gpio_status = status
        print(client.client_gpio_status)
    elif status == PacketStatus.FAILED.value:
        if errors:
            client.log("error", "{0} Client - GetGPIOBoardStatus route processing errors:")
            for error in errors:
                client.log("error", error)
            return
    else:
        client.log("error", "{0} Client - Unknown status response: {0}".format(status))


@server.route(packet_name="SetGPIOPinMode")
def set_mode(client, data):
    """
    Validates if client GPIO pin mode change was successful

    :param client: ClientThread instance
    :param data: Decrypted and deserialized packet dict
    :return: None
    """
    generic_response_validator(client, data, "SetGPIOPinMode")


@server.route(packet_name="SetGPIOPinOutput")
def set_output(client, data):
    """
    Validates if client GPIO pin output change was successful

    :param client: ClientThread instance
    :param data: Decrypted and deserialized packet dict
    :return: None
    """
    generic_response_validator(client, data, "SetGPIOPinOutput")


@server.route(packet_name="SetGPIOPinLock")
def set_lock(client, data):
    """
    Validates if client GPIO pin output change was successful

    :param client: ClientThread instance
    :param data: Decrypted and deserialized packet dict
    :return: None
    """
    generic_response_validator(client, data, "SetGPIOPinLock")