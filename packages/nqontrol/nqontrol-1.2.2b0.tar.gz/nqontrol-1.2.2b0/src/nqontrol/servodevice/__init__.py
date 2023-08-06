"""Main part of ServoDevice."""
# pylint: disable=import-outside-toplevel,too-few-public-methods,cyclic-import,too-many-arguments,too-many-branches
import json
import logging as log
import os
import sys
from pathlib import Path

from ADwin import ADwin, ADwinError
from openqlab.analysis.servo_design import ServoDesign

from nqontrol.general import MockADwin, errors, settings


class ServoDevice:
    """
    A ServoDevice is the whole device, containing 8 (default can be changed) single servos.

    With this object you can control one ADwin device and manage all servos of this device.

    Parameters
    ----------
    deviceNumber: :obj:`int`
        Number of the ADwin device on this system.
        The number can be skipped when loading a ServoDevice from file.

        You have to set it using the tool `adconfig`.
        See [installation](install) for configuration details.
    readFromFile: :obj:`str`
        Select a filename if you want to open a whole ServoDevice with all servos from a saved json file.
    keep_state: :obj:`bool`
        Do not change the state of a running ADwin device.
    """

    from ._general import (
        _DEFAULT_PROCESS,
        _DONT_SERIALIZE,
        _JSONPICKLE,
        __repr__,
        _bootAdwin,
        _greaterControlRegister,
        _lockControlRegister,
        reboot,
        servoDesign,
        timestamp,
        workload,
    )
    from ._loadsave import (
        _applySettingsDict,
        _backupSettingsFile,
        _getSettingsDict,
        _sendAllToAdwin,
        _writeSettingsToFile,
        loadDeviceFromJson,
        loadServoFromJson,
        saveDeviceToJson,
    )
    from ._monitors import disableMonitor, enableMonitor, monitors
    from ._servo_handling import (
        _list_servos_str,
        addServo,
        list_servos,
        removeServo,
        servo,
        servo_iterator,
    )

    # The init method has to be here, otherwise mypy dies.
    def __init__(
        self,
        deviceNumber=0,
        readFromFile=None,
        reboot=False,
        keep_state=False,
        adw=None,
    ):
        """Create a new ServoDevice object."""
        if deviceNumber is None and readFromFile is None:
            raise errors.UserInputError(
                "You have to set a deviceNumber if you do not load a ServoDevice from a file!"
            )
        log.info(f"deviceNumber: {deviceNumber}")

        raiseExceptions = 1
        self._servoDesign: ServoDesign = ServoDesign()  # The dummy servo design object
        self._servos = [None] * settings.NUMBER_OF_SERVOS
        self._monitors = [None] * settings.NUMBER_OF_MONITORS

        if (
            readFromFile is not None
            and os.path.isfile(readFromFile)
            and deviceNumber is None
        ):
            with open(readFromFile, "r") as file:
                data = json.load(file)
            if not data.get(self.__class__.__name__):
                raise Exception("Wrong file format.")
            self.deviceNumber = data[self.__class__.__name__]["deviceNumber"]
        else:
            self.deviceNumber = deviceNumber

        if adw is None:
            if deviceNumber == 0:
                log.warning("Running with mock device!")
                self.adw = MockADwin(deviceNumber)
            else:
                self.adw = ADwin(deviceNumber, raiseExceptions)
        else:
            self.adw = adw

        try:
            self._bootAdwin(self._DEFAULT_PROCESS, reboot=reboot)
        except ADwinError as e:
            if e.errorNumber in (2001, 11):
                raise errors.DeviceError("No device connected!")
            log.error(e)
            self.adw = MockADwin(deviceNumber)
            self._bootAdwin(self._DEFAULT_PROCESS)

        if readFromFile is not None and os.path.isfile(readFromFile):
            log.warning(f"Loaded from: {readFromFile}")
            self.loadDeviceFromJson(readFromFile, keep_state=keep_state)

        # Adding servos
        for i in range(1, settings.NUMBER_OF_SERVOS + 1):
            if self._servos[i - 1] is None:
                self.addServo(channel=i, keep_state=keep_state)
