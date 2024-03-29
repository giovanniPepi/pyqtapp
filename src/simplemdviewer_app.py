#! /usr/bin/env python3

import os
import sys
import signal
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from simplemdviewer.md_converter import MdConverter


def main():
    """Initializes and manages application execution"""
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    """Listens to Ctrl+C to close the app"""
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    """Handles KDE style out of Plasma"""
    if not os.environ.get("QT_QUICK_CONTROLS_STYLE"):
        os.environ["QT_QUICK_CONTROLS_STYLE"] = "org.kde.desktop"

    qmlRegisterType(MdConverter, 'org.kde.simplemdviewer',
                    1, 0, 'MdConverter')

    base_path = os.path.abspath(os.path.dirname(__file__))
    url = QUrl(f'file://{base_path}/qml/main.qml')
    engine.load(url)

    if len(engine.rootObjects()) == 0:
        quit()

    app.exec()


if __name__ == "__main__":
    main()

